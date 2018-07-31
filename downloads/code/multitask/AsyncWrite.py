#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 12:25:39
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import threading
import time
from random import randint

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    def run(self):
        with open(self.out, 'a') as f_h:
            f_h.write(self.text + '\n')
            time.sleep(randint(1,5))
        print(f'Finished background file write to {self.out}')
def main():
    message = input("Enter a string: ")
    
    background = AsyncWrite(message,'out.txt')
    background.start()
    print('The program can continue while it writes another thread')
    print('100 + 400 = ', 100 + 400)
    background.join()
    print('waited until thread was complete')
    print('Program end')

    
if __name__ == "__main__":
    main()

