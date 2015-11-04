#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义
class People(object):
    '''A peple class'''
    addr='earth'

    def __init__(self,name,birthday):
        self.name=name
        self.birthday=birthday

    def del_self(self):
        '''delete a People Object'''
        print('note: you are del a people !')
        del self;

#属性引用
print('All people\'s addr is '+People.addr)
print('Help for del_self fun '+People.del_self.__doc__)

#实例化
m=People('veekxt','1994-11-12')
print (m.name+'\'s birthday is ' +m.birthday)

#继承,支持多继承
class Man(People):
    def __init__(self,L):
        self.L=L
    def del_self(self):
        print('note: you are del a man !')
        del self

m=Man(100)
print(m.addr+' is man\'s address')
#del_self 被子类覆盖
m.del_self()
#但仍有办法到达
m=Man(120)#重建
People.del_self(m)
#实际上，class更像是只创建了一个命名空间而已
