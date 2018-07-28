#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-27 22:46:42
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from  string import Template

class MyTemplate(Template):
    delimiter = '#'


def main():
    cart = []
    cart.append(dict(
        item='Coke',
        price=8,
        qty=3
    ))
    cart.append(dict(
        item='Cake',
        price=4,
        qty=4
    ))
    cart.append(dict(
        item="Apple",
        price=1,
        qty=5
    ))
    t = Template("$qty x $item per $price")
    total = 0
    for item in cart:
        print(t.substitute(item))
        total += item['price'] * item['qty']
    print(f'Total: {total}')
if __name__ == "__main__":
    main()