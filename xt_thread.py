#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time  
import threading

def print_str(tmp,delay_time):
    while 1:
        print(tmp)
        time.sleep(delay_time)
        
A=threading.Thread(target=print_str,args=('AAAA',1))
B=threading.Thread(target=print_str,args=('BBBB',2))
A.start()
B.start()
