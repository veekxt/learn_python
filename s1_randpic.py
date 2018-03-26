#!/usr/bin/env python3
# coding=utf-8

# https://github.com/veekxt/tieba_good_backup

import urllib.request

import hashlib
import pickle

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
        if hashstr in hashset:
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
