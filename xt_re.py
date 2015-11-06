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
