#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_call_info(fun):
    def foo(*args,**kwargs):
        print("you call a fun named: "+fun.__name__)
        fun(*args,**kwargs)
        return 0
    return foo

@add_call_info
def xt_print(a):
    print(a)

xt_print('hello,world')
