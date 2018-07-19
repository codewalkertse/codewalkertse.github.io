#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-18 17:30:13
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

class Init(object):
    def __init__(self, value):
        print('Init')
        self.value = value


class Add2(Init):
    def __init__(self, value):
        super(Add2, self).__init__(value)
        print('Add2')
        # self.value += 2
        self.value = 2 + self.value


class Mul5(Init):
    def __init__(self, value):
        super(Mul5, self).__init__(value)
        print('Mul5')
        # self.value *= 5
        self.value = self.value * 5


class Pro(Mul5, Add2):
    pass


class Incr(Pro):
    def __init__(self, value):
        super(Incr, self).__init__(value)
        # self.value += 1
        self.value = self.value + 1


def main():
    i = Incr(5)
    print(i.__class__.__mro__)
if __name__ == "__main__":
    main()

1. take the head of the first list, i.e L[B1][0];
2. if this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head of the next list and take it, if it is a good head.
3. Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class C and will raise an exception.1.

每次找到一个只指向别人的点 (学术性说法：入度为0)，记录下来；然后忽略掉这个点和它所指出去的线，再找到下一个只指向别人的点，记录下来，直到剩最后一个点，所有记录的点的顺序就是拓扑顺序