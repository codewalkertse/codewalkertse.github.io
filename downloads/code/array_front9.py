#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 13:31:05
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

from random import randint

# function tool
# create a list with random int
def random_list(list_length=False):
    if list_length:
        return [randint(0,10) for _ in range(list_length)]
    return False

def array_front9(target):
    rl = random_list(randint(0,10))
    if not target:
        return rl,False
    if not rl:
        return rl,False
    # source = [rl[i:i+3] for i in range(len(rl))]
    # for i in source:
    #     if target == i:
    #         return rl,True
    # return rl,False
    
    # Also see:
    for i in range(len(rl)-2):
        if rl[i]==1 and rl[i+1]==2 and rl[i+2]==3:
            return rl,True
    return rl,False


def main():
    count = 0
    target = [1,2,3]
    while True:
        '''
        s for source
        r for result
        '''
        s, r = array_front9(target)
        if r:
            print(f'Found {target} in {s} by running {count} times') 
            break
        count += 1


if __name__ == "__main__":
    for _ in range(10):
        main()
