#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-16 17:17:42
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0
class P(object):                                
    def __init__(self, v):   
        print('init P') # A0 step 1.1  
        self.data = v                                         
    def __get__(self, ins, cls):   
        print(f'from ins:{ins.__dict__} get {self.data} & cls:{cls}')  # B0   
        return self.data                
    def __set__(self, ins, v): 
        print(f'save {v} to {ins.__dict__}')    # step 2.1.1      
        self.data = v                   
    def __delete__(self, ins):          
        del self.data                   
class Person():                                
    name = P('Alice')   # A0 step 1                    
    def __init__(self, v):  # A0 step 2
        print('init name')           
        self.name = v       # A0 step 2.1
                            # Call P when set name = v and cover 'Alice' to 'Bob'. 
                            # Notice: Now we're NOT create instance for Person
        print('init street')                 
        self.street = v     # A0 step 3

obj = Person('Bob') #  step A0 init P before init Person 
print(f'Does obj have name? { hasattr(obj, "name") }')
print('-'*20)
print(f'obj has:{obj.__dict__}')    # obj has no name, because of P hold name variable???    
print(f'Does obj have name? { hasattr(obj, "name") }')
print(f'Now will get name:{obj.name}') # B0. Because of descript name
                                    # So call P.__get__ first before get name's value
print('-'*20)
print('Now will get street:{obj.street}')   # We are NOT descript street
                                            # so will not call any func from P
obj.name = 'Charley'    # call P.__set__ again
                        # Notice: instance obj has no name, because of P hold name variable
print(f'Does obj have name? { hasattr(obj, "name") }')
print(f'get name from {obj}: {obj.name}')
print(f'del name')
del obj.name
print(f'Does obj have name? { hasattr(obj, "name") }')
obj.name = 'Doggie' # set name = Doggie
print(f'Does obj have name? { hasattr(obj, "name") }')
print('-'*20)
print(type(obj).__dict__['name'].__get__(obj, type(obj)))
print('-'*20)
print(type(obj).__dict__['name'].__get__(obj, type(obj)) is obj.name)
# In fact call obj.name is transfering to call type(obj).__dict__['name'].__get__(obj, type(obj))