#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 12:05:01
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from threading import Thread
import time
from random import randint
def job(name, delay, repeat):
    print(f'Job: {name} started, delay:{delay}, repeat:{repeat}')
    while repeat > 0 :
        time.sleep(delay)
        ctime = time.ctime(time.time())
        print(f'{name}: {ctime}, repeat in {repeat}')
        repeat -= 1
    print(f'Job: {name} completed.')

def main():
    t1 = Thread(target=job, args=('job1',randint(1,4),randint(1,10)))
    t2 = Thread(target=job, args=('job2',randint(1,4),randint(1,10)))
    t3 = Thread(target=job, args=('job3',randint(1,4),randint(1,10)))
    t4 = Thread(target=job, args=('job4',randint(1,4),randint(1,10)))
    threads = [t1, t2, t3, t4]
    for t in threads:
        t.start()
if __name__ == "__main__":
    main()

