#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stu(object):
    def __init__(self,n):
        self._name=n

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name=value

a=Stu('XieTao')
print(a.name)
a.name='XieErTao'
print(a.name)

