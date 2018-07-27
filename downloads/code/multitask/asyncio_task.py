#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-25 17:39:39
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import asyncio
import time
from random import randint

async def job():
    x = randint(1,5)
    print(f'#{x}: Start!')
    await asyncio.sleep(x)
    return f'#{x}: Done after {x}s'

def callback(future):
    print('call back:', future.result())

if __name__ == "__main__":
    tasks = []
    start = time.process_time()
    loop = asyncio.get_event_loop()
    for _ in range(5):
        task = loop.create_task(job())
        task.add_done_callback(callback)
        tasks.append(task)
    
    loop.run_until_complete(asyncio.wait(tasks))
    print(f'Processing in {time.process_time()-start}')

