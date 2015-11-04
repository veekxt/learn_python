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
    def __init__(self,L,love,site):
        self.L=L
        self.love=love  #私有变量以"_"开头，不能直接访问
        self.__site=site #__开头的变量会被替换为_classname__var 的形式，这里是"_Man__site"
    def del_self(self):
        print('note: you are del a man !')
        del self

m=Man(100,'sss','veekxt.com')
print(m.addr+' is man\'s address')
#访问site
print('m'+'\'s site is '+m._Man__site)  #__site不能访问
#del_self 被子类覆盖
m.del_self()
#但仍有办法到达
m=Man(120,'sy','veekxt.com')#重建
People.del_self(m)
#实际上，class更像是只创建了一个命名空间而已

