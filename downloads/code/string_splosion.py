#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 12:08:03
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0


'''
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''


def string_splosion(str):
    return ''.join([str[:x+1] for x in range(len(str))])
    # Same as
    # new_str = []
    # for x in range(len(str)):
    #     new_str.append(str[:x+1])
    # return new_str


def main():
    print(string_splosion('Code'))


if __name__ == "__main__":
    main()
