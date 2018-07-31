#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 12:05:01
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import threading
import time
from random import randint
tLock = threading.Lock()
def job(name, delay, repeat):
    print(f'Job: {name} started, delay:{delay}, repeat:{repeat}')
    tLock.acquire()
    print(f'{name} has acquired the lock')
    while repeat > 0 :
        time.sleep(delay)
        ctime = time.ctime(time.time())
        print(f'{name}: {ctime}, repeat in {repeat}')
        repeat -= 1
    print(f'{name} is releasing the lock')
    tLock.release()
    print(f'Job: {name} completed.')

def main():
    t1 = threading.Thread(target=job, args=('job1',randint(1,4),randint(1,10)))
    t2 = threading.Thread(target=job, args=('job2',randint(1,4),randint(1,10)))
    t3 = threading.Thread(target=job, args=('job3',randint(1,4),randint(1,10)))
    t4 = threading.Thread(target=job, args=('job4',randint(1,4),randint(1,10)))
    threads = [t1, t2, t3, t4]
    for t in threads:
        t.start()
if __name__ == "__main__":
    main()

