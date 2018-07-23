#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 23:17:23
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import asyncio
import time
async def print_hello():
    # while True:
        print(f"It's time for {time.time()}")
        await asyncio.sleep(3)
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_hello())
         
if __name__ == "__main__":
    main()

