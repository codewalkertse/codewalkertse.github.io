#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 13:30:50
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import time
import random
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print('%s running' %self.name)
        time.sleep(random.randrange(1,8))
        print('%s stop' %self.name)

def main():
    p1 = MyProcess('1')
    p2 = MyProcess('2')
    p3 = MyProcess('3')
    p4 = MyProcess('4')
    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')
if __name__ == "__main__":
    main()

