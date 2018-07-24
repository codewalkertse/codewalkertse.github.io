#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 23:17:23
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import asyncio
import json
import os
import time
from random import randint
from urllib.request import Request, urlopen

import aiohttp
import async_timeout


async def download_coroutine(url, headers, session):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            path = '/Users/codewalkertes/Desktop/tmp/'
            filename = path + os.path.basename(url) + '.pdf'
            with open(filename, 'wb') as f_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            return await response.release()

async def url_list(url, headers):
    req = Request(url, headers=headers)
    data = urlopen(req).read()
    d = json.loads(str(data, encoding='utf-8'))
    urls = d['data']
    return urls

async def run(loop,url_api, headers):
    urls = await url_list(url_api,headers)
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine(url, headers, session) for url in urls]
        await asyncio.gather(*tasks)

def main(url_api):
    start_time = time.clock()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gb2312,utf-8',
               'User-Agent': 'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'Keep-alive'
               }
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop,url_api,headers))
    loop.close()
    t = time.clock()-start_time
    print('total time cost:%f.2' % t)

if __name__ == '__main__':
    transactionid = 14639
    url_api = 'http://api.hellomoney.com/index.php?c=FadadaTool&a=contract&transactionid=' + str(transactionid)
    main(url_api)