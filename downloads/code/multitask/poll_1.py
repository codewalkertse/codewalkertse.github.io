#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 13:46:51
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from multiprocessing import Pool
import os, time, random
core_num = 4
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def main():

    print('Parent process %s.' % os.getpid())
    p = Pool(core_num)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('\nAll subprocesses done.')

if __name__ == "__main__":
    main()

