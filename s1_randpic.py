#!/usr/bin/env python3
# coding=utf-8

# https://github.com/veekxt/tieba_good_backup

import sys
import urllib.request
import re
import os
import queue
import threading

import socket

import hashlib
import pickle

socket.setdefaulttimeout(20)

HIQ = False
LZ = True

f_log = open("last.log", "w", encoding="utf-8")

# 全局变量,一个公共资源字典
PUB_SRC = {}


def saveStr(mystr, myfile):
    '''把字符串保存到文件'''
    fh = open(myfile, "w", encoding="utf-8")
    fh.write(mystr)
    fh.close


def get_html(url, code="utf-8"):
    '''获取请求url的返回页面,默认utf-8解码'''
    for i in range(3):
        try:
            page = urllib.request.urlopen(url, timeout=10)
            break
        except Exception as e:
            print("%s连接出错:" + str(e) % url)
    html = page.read().decode(code, errors='ignore')
    return html


def get_cid(tieba):
    '''获取精品贴分类和对应cid'''
    url = "http://tieba.baidu.com/f?kw=%s&tab=good" % urllib.parse.quote(tieba)
    page = get_html(url)
    tmp = re.findall(r'(?<=cid=)\d+?.+?">.+?(?=<)', page)
    rel = []
    for i in tmp:
        rel.append(tuple(i.split('" class="j_good_tag">')))
    return rel


def get_list(cid, tieba):
    '''从指定贴吧和分类(cid)获取帖子列表'''
    tieba_name_url = urllib.parse.quote(tieba)
    url = "http://tieba.baidu.com/f?kw=%s&tab=good&cid=%s" % (
        tieba_name_url, cid)
    page = get_html(url, "utf-8")
    # 确定最大页数
    max_pn = re.compile(r'(?<=pn=)\d+(?=" class="last)').findall(page)
    if len(max_pn) != 0:
        max_pn = int(max_pn[0])
    else:
        max_pn = 0
    rel_lst = []
    # 匹配区域,包含了作者,标题,帖子id
    tieba_list = re.compile(r'<a href="/p/.+?"\stitle=".+?".+?title=".+?"', re.DOTALL)
    for i in range(0, max_pn + 1, 50):  # i作为页数变量,实际上不是页数,而是50*(页数-1)
        print("查找分类 %s 中的第 %s 页主题" % (cid, int(i / 50 + 1)))
        url = url + "&pn=%d" % i
        page = get_html(url, "utf-8")
        rel_code = tieba_list.findall(page)
        rel_lst.extend(rel_code)
        # Todu,没有任何帖子
    # 进一步提取结果,并放入字典中
    re_id_tmp = re.compile(r'(?<=<a href="/p/)\d+?(?=(\?fr=good"|"))')
    re_title_tmp = re.compile(r'(?<=title=").+?(?=" t)')
    re_autor_tmp = re.compile(
        r'(?<=title="主题作者:\s).+?(?=")|(?<=title=")吧刊(?=")')
    mes = []  # 最终结果
    for i in rel_lst:
        try:
            tmp1 = (re_id_tmp.search(i).group(), re_autor_tmp.search(i).group(),
                    re_title_tmp.search(i).group())
            mes.append(tmp1)
            print("找到主题: " + re_title_tmp.search(i).group())
        except:
            print("一个标题匹配失败")

    return mes


def do_page(src, page, path, pic_quality, dict_src, page_count):
    '''处理一个页面,参数分别为:资源文件url列表, 页面, 保存文件的基础路径, 图片质量
    使用一个目录图片,文件使用数字顺序命名
    任务包括:保存资源文件,替换资源和页数链接,删除垃圾信息'''

    media_dir = path + "img/"
    if page_count == 1:
        if not os.path.exists(media_dir): os.mkdir(media_dir)
    page = page.replace("pb_list_pager", "")  # 禁止页码奇怪的跳转
    login_remind = re.compile(
        r'(?<=</div></div></div>)<div.*?id="guide_fc".*?</div></div>')
    try:
        page = page.replace(login_remind.search(page).group(), "")  # 删除未登录提示
    except:
        pass
    for i in src:
        if "&pn=" in i or "?pn=" in i:
            pn = int(i.split("=")[-1])
            page = page.replace(i, "pn_%d.html" % pn, 1)

        if ".css" in i:
            if i in PUB_SRC:
                cssName = "../../pub/" + str(PUB_SRC[i]) + ".css"
                page = page.replace(i, cssName.replace(path, ""))
        elif ".js" in i:
            if i in PUB_SRC:
                jsName = "../../pub/" + str(PUB_SRC[i]) + ".js"
                page = page.replace(i, jsName.replace(path, ""))
        elif ('jpg' in i or 'gif' in i or 'png' in i or 'jpeg' in i) and (
                'http://' in i) and '/forum/pic/item/' not in i and '/tb/cms' not in i and 'taobaocdn.com' not in i:
            if i not in dict_src[0]:
                if ("sign=" in i and pic_quality == True):
                    reGq = re.compile(r'.*/')
                    fGq = reGq.search(i)
                    imggq = i.replace(
                        fGq.group(), "http://imgsrc.baidu.com/forum/pic/item/")
                else:
                    imggq = i
                imgName = media_dir + str(dict_src[1]) + ".jpg"
                try:
                    urllib.request.urlretrieve(imggq, imgName)
                except:
                    print("一个图片错误，记录在last.log")
                    f_log.write("下载错误：" + imggq + '\n')
                dict_src[0][i] = imgName
                dict_src[1] = dict_src[1] + 1
            else:
                imgName = dict_src[0][i]
            page = page.replace(i, imgName.replace(path, ""))
    saveStr(page, path + "pn_%d.html" % page_count)
    return page


def down_from_queue(q):
    while not q.empty():
        i = q.get()
        do_page(*i)


def down_one_tz(tb_code, mydir, only_lz=False, pic_quality=True):
    '''下载一整个帖子,参数:贴子号码, 根目录, 是否只看楼主, 是否使用高质量图片
    会在mydir目录下创建 p_<贴子号码> 目录,每一页命名为pn_<页数>.html'''

    base_url = "http://tieba.baidu.com/p/%s?see_lz=%d&pn=" % (
        tb_code, int(only_lz))

    main_page = get_html(base_url + "1")
    print("==开始下载:http://tieba.baidu.com/p/%s" % (tb_code))

    try:
        page_code = re.compile(r'(?<=<span class="red">)\d*?(?=</span>)')
        page_sum = int(page_code.search(main_page).group())
    except:
        if (only_lz == False):
            return
        else:
            pass
        print("你开启了只看楼主但一楼被删除,取消一个只看楼主http://tieba.baidu.com/p/%s" % tb_code)
        down_one_tz(tb_code, mydir, False, HIQ)
        return
    dict_src = [{}, 0]
    root_dir = mydir + "p_%s/" % tb_code
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    epage = queue.Queue(maxsize=0)
    for page_count in range(1, 1 + page_sum):
        url = base_url + str(page_count)
        main_page = get_html(url)
        tb_media = re.compile(
            r'(?<=src=").*?(?=")|(?<=href=").*?(?=")|(?<=data-tb-lazyload=").*?(?=")')
        rel = tb_media.findall(main_page)
        epage.put((rel, main_page, root_dir, pic_quality, dict_src, page_count))
        print("==%s 的第 %d 页,共 %d 页==" % (tb_code, page_count, page_sum))
    for i in range(10):
        tmp = threading.Thread(target=down_from_queue, args=(epage,))
        tmp.start()


def make_main_index(cids, tieba, has0):
    '''制作主索引文件'''
    mydir = tieba + "_精品/"
    if not os.path.exists(mydir):
        os.mkdir(mydir)
    f = open(mydir + "index.html", "w", encoding="utf-8")
    f.write(
        '<!DOCTYPE html><html><head><meta charset="utf-8"><title>贴吧精品</title><style type="text/css">#main{width:500px;color: #000;text-align:center;margin: 0 auto;}h2{margin-top:auto;text-align:center;}p{margin-top:25px;font-size: 18px;}</style></head><body><h2>%s吧精品贴分类</h2><div id=main>' %
        tieba)
    for i in cids:
        f.write(
            '<p><a target="_blank" href="%s/index.html">%s</a></p>' %
            (i[0], i[1]))
    if has0 == 1:
        f.write(
            '<p><a target="_blank" href="%s/index.html">%s</a></p>' %
            (0, "未分类精品"))
    f.write('</div></body></html>')
    f.close()
    return


def make_cid_index(cid, cid_list, tieba):
    '''某个分类的索引'''
    mydir = tieba + "_精品/%s/" % cid
    if not os.path.exists(mydir):
        os.makedirs(mydir)
    f = open(mydir + "index.html", "w", encoding="utf-8")
    f.write(
        '<!DOCTYPE html><html><head><meta charset="utf-8"><title>贴吧精品</title><style type="text/css">#main{margin-left:50px;color:#000;}h2{margin-top:auto;text-align:center;}p{margin-top:25px;font-size: 18px;}</style></head><body><h2>%s吧精品分类%s</h2><div id=main>' %
        (tieba, cid))
    f.write('<p3><a href="../index.html">返回主页</a><p3>')
    for i in cid_list:
        f.write(
            '<p><a target="_blank" href="http://tieba.baidu.com/p/%s">:原始链接</a>作者:%s : <a target="_blank" href="p_%s/pn_1.html">%s</a></p>' %
            (i[0], i[1], i[0], i[2]))
    f.write('</div></body></html>')
    f.close()
    return


def get_list_from_stdin(prompt):
    s = input(str(prompt) + "，使用单个空格分隔:\n")
    l = s.split(' ')
    return l


def make_down_list(tieba):
    print("==生成下载列表==#")
    cid_s = get_cid(tieba)
    print("分类如下:\n")
    for i in cid_s:
        print(i[0] + " - " + i[1])
    print("0 - 未分类精品贴\n")
    has0 = 0
    cids_down = get_list_from_stdin("输入你想下载的分类编号")
    if '0' in cids_down:
        all_jp = set(get_list(0, tieba))
        has0 = 1
    else:
        all_jp = set()
    cid_s_new = []
    for i in cids_down:
        for j in range(len(cid_s)):
            if cid_s[j][0] == str(i):
                cid_s_new.append((cid_s[j][0], cid_s[j][1]))
    make_main_index(cid_s_new, tieba, has0)  # 制作索引文件
    ilist = []
    for i in range(len(cid_s_new)):
        cid = cid_s_new[i][0]
        print("整理分类: #%s" % cid_s_new[i][0])
        a_cid_list = get_list(cid, tieba)
        make_cid_index(cid, a_cid_list, tieba)  # 制作索引文件
        for i in a_cid_list:
            ilist.append((cid, i[0], i[1], i[2]))
    if '0' in cids_down:
        for i in range(len(cid_s)):
            cid = cid_s[i][0]
            a_cid_list = get_list(cid, tieba)
            all_jp = all_jp - set(a_cid_list)
        if len(all_jp) != 0:
            print("查找未分类精品#")
            make_cid_index("0", list(all_jp), tieba)  # 制作索引文件
            for i in list(all_jp):
                ilist.append((0, i[0], i[1], i[2]))
    return ilist


def down_pub_src(path):
    page = get_html("http://tieba.baidu.com/p/4087941653")
    tb_media = re.compile(
        r'(?<=src=").*?(?=")|(?<=href=").*?(?=")|(?<=data-tb-lazyload=").*?(?=")')
    src_l = tb_media.findall(page)
    cNum = 0
    jNum = 0
    for i in src_l:
        if ".css" in i:
            cssName = path + str(cNum) + ".css"
            PUB_SRC[i] = cNum
            if (not "http://" in i) and (not "https://" in i):
                i = "http:" + i
            urllib.request.urlretrieve(i, cssName)
            print("下载了%d.css" % cNum)
            cNum = cNum + 1
        elif ".js" in i:
            jsName = path + str(jNum) + ".js"
            PUB_SRC[i] = jNum
            if (not "http://" in i) and (not "https://" in i):
                i = "http:" + i
            urllib.request.urlretrieve(i, jsName)
            print("下载了%d.js " % jNum)
            jNum = jNum + 1


def down_from_queue_tz(q, tieba):
    while not q.empty():
        i = q.get()
        tb_code = i[1]
        mydir = tieba + "_精品/%s/" % i[0]
        down_one_tz(tb_code, mydir, LZ, HIQ)


def down_tieba(tieba):
    down_list = make_down_list(tieba)
    print(
        "\n\n共找到 %s 条 精品贴,即将开始下载...\n遇到图片很多的页面可能需要很多时间...\n" %
        len(down_list))
    if not os.path.exists(tieba + "_精品/pub/"):
        os.makedirs(tieba + "_精品/pub/")
    print("下载公共资源")
    down_pub_src(tieba + "_精品/pub/")
    print("公共资源完成")
    qdown = queue.Queue(maxsize=0)
    for i in down_list:
        qdown.put(i)

    qs = queue.Queue(maxsize=0)
    ls_xc = []
    print("创建下载线程")
    for i in range(10):
        tmp = threading.Thread(target=down_from_queue_tz, args=(qdown, tieba))
        tmp.start()
        ls_xc.append(tmp)
    print("创建完成")


def get_real_url(url, try_count=1):
    if try_count > 3:
        return url


if __name__ == "__main__":
    number = 0
    repeat_count = 0
    myhash = hashlib.md5()
    hashset = set()
    while True:
        url = "http://ac.stage3rd.com/S1_ACG_randpic.asp"
        try:
            res = urllib.request.urlopen(url);
        except:
            print("A eeror!")
            continue
        file_type = res.getheader("Content-Type").split("/")[1]
        buf = res.read()
        myhash.update(buf)
        hashstr = myhash.hexdigest()
        if myhash not in hashset:
            print("A Repeating IMG %s" % hashstr)
            repeat_count+=1
            if repeat_count == 20 :
                print("repeating too much, exit")
                with open('s1_rand_pic_hash.pik', 'wb')as f:
                    pickle.dump(hashset, f, -1)
                break
            pass
        else:
            number += 1
            repeat_count = 0
            hashset.add(hashstr)
            open("S1_range_2018/%d.%s" % (number, file_type), 'wb').write(buf)



