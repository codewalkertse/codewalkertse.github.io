#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 12:08:03
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0


'''

Given a string, return the count of the number of times that a substring length 2 appears 
in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''


def last2(str):
    if not str:
        return 0
    target = str[-2:]
    source = [str[i:i+2] for i in range(len(str))]
    count = 0
    for i in source:
        if target == i:
            count += 1
    return count - 1


def main():
    print(last2('axxxaaxx'))


if __name__ == "__main__":
    main()
