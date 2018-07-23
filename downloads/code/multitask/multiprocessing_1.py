#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 13:30:50
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def main():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
if __name__ == "__main__":
    main()

