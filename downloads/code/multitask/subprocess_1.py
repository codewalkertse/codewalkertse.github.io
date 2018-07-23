#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-22 13:36:59
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import os
import subprocess
def main():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
if __name__ == "__main__":
    main()

