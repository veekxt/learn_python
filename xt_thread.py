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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()