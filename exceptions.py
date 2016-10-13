#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def xt_test():
    try:
        a=1/0
        print('这里不执行')
    except ZeroDivisionError:
        print('You can\'t division zero !')
    finally:
        print('**一定**会被执行')
        
    try:
        a=1/1
        a+[]
    except (ZeroDivisionError,TypeError) as err:
        print('division zero / type error !')
        print(err)
    finally:
        print('**一定**会被执行')

#自定义异常类
def xt_test2():
    class MaxError(Exception):
        def __init__(self,mess):
            self.mess=mess
        def __str__(self):
            return repr(self.mess)
    try:
        a=101
        b=a/3
        if a>100:
            raise MaxError('your a can\'t > 100')
        print('这里不执行')
    except MaxError as e:
        print(e)        #e.args 所有参数列表
    else:               #else 子句
        print('has no MaxError')
    finally:
        print('**一定**会被执行')
        
xt_test()
xt_test2()

print('End main')

