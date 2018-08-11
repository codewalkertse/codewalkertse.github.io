#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 12:02:36
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0


def string_bits(str):
    return ''.join([str[x] for x in range(len(str)) if x % 2 == 0])
    # Same as
    # new_str = []
    # for x in range(len(str)):
    #     if x % 2 == 0:
    #         new_str.append(str[x])
    # return ''.join(new_str)


def main():
    print(string_bits('Heeololeo'))


if __name__ == "__main__":
    main()
