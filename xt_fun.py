#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def xt_sum(*args):
    s=0
    for i in args:
        s+=i
    return s
    
print(xt_sum(2,3,4))

def xt_powx(*args,**kwargs):
    s=args[0]**kwargs['x']
    return s

print(xt_powx(5,x=3))
