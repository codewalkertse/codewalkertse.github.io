#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 22:10:15
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import asyncio

async def find_divisibles(inrange, div_by):
    print(f'finding nums in range {inrange} divisible by {div_by}')
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 500 == 0:
            await asyncio.sleep(0.0001)
    print(f'Done w/ nums in range {inrange} divisible by {div_by}')
    return located

async def main():
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1, divs2, divs3
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        # loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()
