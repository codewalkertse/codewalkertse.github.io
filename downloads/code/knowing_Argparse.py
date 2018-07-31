#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 11:01:21
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0
import argparse


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def main():
    parser = argparse.ArgumentParser(description="Calculate fibonacci")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quit', action='store_true')
    parser.add_argument(
        'num', help='The fibonacci number you wish to calculate.', type=int)
    parser.add_argument(
        '-o', '--output', help='Output result into a file', action='store_true')
    args = parser.parse_args()
    num = args.num
    result = fib(num)
    output_result = f'The {num}th fibonacci is {result}'
    if args.verbose:
        print(output_result)
    elif args.quit:
        print(result)
    else:
        print(f'Fib({num})={result}')
    if args.output:
        with open('fibonacci.txt', 'a') as f_h:
            f_h.write('\n' + output_result)


if __name__ == "__main__":
    main()