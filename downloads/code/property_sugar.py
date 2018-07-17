#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-17 23:36:36
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import datetime
class CurrentDate(object):
    def __get__(self, instance, owner):
        return datetime.date.today()
    def __set__(self, instance, value):
        raise NotImplementedError("Can't change the current date.")

class Example(object):
    date = CurrentDate()

e = Example()
print(e.date)
# raise a exception: NotImplementedError: Can't change the current date.
#e.date = datetime.date.today() 

class Example2(object):
    def __init__(self, name):
        self.name = name

    @property
    def password(self):
        raise AttributeError("Cant's get value of password")

    @password.setter
    def password(self, password):
        self.password_hash = password

e2 = Example2('Alice')
e2.password = 'your_password'
#print(e2.password) #AttributeError: Cant's get value of password
