#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

r=urllib.request.urlopen('http://veekxt.com')
f=open('tmp.txt','w')
f.write(r.read().decode('utf-8'))

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
r=urllib.request.Request(url='http://www.useragentstring.com/',headers=headers)
s=urllib.request.urlopen(r)
f=open('tmp2.html','w')
f.write(s.read().decode('utf-8'))
