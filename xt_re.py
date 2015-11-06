#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#re测试

import re

m=re.compile(r'(te)st(?= )')
s=m.search('it is a test text')
print(s.group(1))
g=s.group(0)
print(g)
