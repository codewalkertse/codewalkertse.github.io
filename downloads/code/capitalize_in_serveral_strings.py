#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 09:50:38
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

def capitalize_sentense(s,sep=None):
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))

def capitalize_the_first(s):
    return s.capitalize()

def main():
    s = 'Et mollJJDKitia et iJJDJkdn. digKKDJnissimos kdjkdjHHSJ.'
    out = capitalize_sentense(s,sep='. ')
    print(out)
    
    out = capitalize_the_first(s)
    print(out)

if __name__ == "__main__":
    main()