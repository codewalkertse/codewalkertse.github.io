#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date : 2018-07-07 17:23:04
# @Author : Simon (simon.xie@codewalker.meg)
# @Link : http://www.codewalker.me
# @Version : 1.0.0
import os
def hailstone(n):
  hai_list = []
  while n > 1:
    hai_list.append(n)
    if n%2:
    #奇数
      n = 3*n + 1
    else:
    #偶数
      n = n//2
  else:
    hai_list.append(1)
  return hai_list
def print_result(r):
  length=len(r)
  print('list:{list}\nlength:{length}'.format(list=r,length=length))

if __name__ == "__main__":
  print_result(hailstone(7))
  print('*'*80) 
  print_result(hailstone(27))