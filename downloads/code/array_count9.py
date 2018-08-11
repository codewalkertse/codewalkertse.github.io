#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 12:51:00
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0





'''
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

from random import randint

# function tool
# create a list with random ints
def random_list(list_length=False):
    if list_length:
        return [randint(0,10) for _ in range(list_length)]
    return False

def array_count9():
    rl = random_list(10)
    count = 0
    for n in rl:
        if n == 9:
            count += 1
    return rl,count


def main():
    for _ in range(10):
        s, c = array_count9()
        print(f'{c} times 9 in {s}')


if __name__ == "__main__":
    main()
