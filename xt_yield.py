#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#next() 下一个
f=fib(100)
for i in range(100):
    print(i,':',f.__next__())
    
#直接迭代
f=fib(100)
for i in f:
    print(i)