#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#re测试

import re

m=re.compile(r'(te)st(?= )')
s=m.search('it is a test text')
print(s.group(1))
g=s.group(0)
print(g)

#等价，search搜索第一个
s=re.search(r'(te)st(?= )','it is a test text')
print(s.group(1))
g=s.group(0)
print(g)

#findall  返回所有匹配字符串
s=re.findall(r'is','it is a test text is one ')
print(s)

#split 使用正则分割字符串
s=re.split(r',','it,is,a,test,text')
print(s)

#sub使用正则替换
s=re.sub(r',','-','it,is,a,test,text')
print(s)

#subn使用正则替换但返回元组
s=re.subn(r',','-','it,is,a,test,text')
print(s)

#为所有非数字和字母加转义
s=re.escape('http://www.veek_xt.com')
print(s)

