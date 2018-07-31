#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-30 10:21:42
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from threading import Thread
from time import process_time, sleep, time_ns

flag = 0

def do_something(name, sec):
    print(f'Do {name} in {sec}')
    sleep(sec)
    print(f'completed {name} after {sec}s.')

def main():
    start = time_ns()
    have_supper = Thread(name='have_supper', target=do_something, args=('have_supper', 2))
    watch_tv = Thread(name='watch_tv', target=do_something, args=('watch_tv', 10))

    have_supper.setDaemon(True)
    have_supper.start()

    watch_tv.setDaemon(True)
    watch_tv.start()

    have_supper.join(3)
    watch_tv.join(4)
    print(f'Subthread done in {time_ns()-start} seconds')
if __name__ == '__main__':
    start = time_ns()
    main()
    print(f'Main done in {time_ns()-start} seconds')
