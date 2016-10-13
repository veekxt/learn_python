#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def x_cal(a, b, f):
    return f(a) + f(b)
def f1(a):
    return a+1;

print(x_cal(1, 2, f1));
