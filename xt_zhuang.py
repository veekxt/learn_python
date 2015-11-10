#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_call_info(fun):
    def foo(*args,**kwargs):
        print("you call a fun named: "+fun.__name__)
        fun(*args,**kwargs)
    return foo

@add_call_info
def xt_print(a):
    print(a)

xt_print('hello,world')
#带参数的装饰器
#简单理解：
#装饰器应该返回一个函数，该函数会以被装饰函数为参数
def foo(arg):
    print(arg)
    def add_call_info(fun):
        def foo(*args,**kwargs):
            print("you call a fun named: "+fun.__name__)
            fun(*args,**kwargs)
        return foo
    return add_call_info
    
@foo('++><++')
def xt_print(a):
    print(a)
    
xt_print('hello,world')
