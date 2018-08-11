#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 13:01:21
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

from random import randint
import asyncio

# function tool
# create a list with random int
async def random_list(list_length=False):
    if list_length:
        return [randint(0,10) for _ in range(list_length)]
    return False

async def array_front9():
    rl = await random_list(randint(0,10))
    if not rl:
        return rl,False
    if 9 in rl[0:4]:
        return rl, True
    return rl,False

def callback(future):
    # print('call back:', future.result())
    s, c = future.result()
    print(f'First 4 chars has 9 is **{c}** in {s}')   


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = []
    for _ in range(10):
        task = loop.create_task(array_front9())
        task.add_done_callback(callback)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
