#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-16 17:17:42
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0
class P(object):                                
    def __init__(self, v):              
        self.data = v                                         
    def __get__(self, ins, cls):        
        return self.data                
    def __set__(self, ins, v):          
        self.data = v                   
    def __delete__(self, ins):          
        del self.data                   
class A():                                
    p = P(2)                          
    def __init__(self, v):              
        self.p = v                      
        self.x = v                                                         
obj = A(1)                              
print(obj.__dict__)                     
print(obj.p)                                                         
obj.p = 3                               
print(obj.p)                            
del obj.p                               
print(hasattr(obj, 'p'))                
obj.p = 4                             
print(hasattr(obj, 'p')) 