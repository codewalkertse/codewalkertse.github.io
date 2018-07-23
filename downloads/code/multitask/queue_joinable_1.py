#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 14:23:38
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

from multiprocessing import Process,JoinableQueue
import time,random
def consumer(q):
    while True:
        res = q.get()
        print('消费者拿到了 %s' %res)
        q.task_done()
def producer(seq, q):
    for item in seq:
        time.sleep(random.randrange(1,2))
        q.put(item)
        print('生产者做好了 %s' %item)
    q.join()
def main():
    q = JoinableQueue()
    seq = ('包子%s' %i for i in range(5))
    p = Process(target=consumer, args=(q, ))
    p.daemon = True #设置为守护进程，在主线程停止时p也停止，但是不用担心，producer内调用q.join保证了consumer已经处理完队列中的所有元素
    p.start()
    producer(seq, q)
    print('主线程')
if __name__ == "__main__":
    main()

