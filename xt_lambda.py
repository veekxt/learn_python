#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a=list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

def wt():
    return lambda x:x*x
    
print(list(map(wt(),[1,2,3])))
