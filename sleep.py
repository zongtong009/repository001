# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:44:10 2018

@author: Administrator
"""
import time
def wait():
    time.sleep(1.1)
	#延时1.1秒
for i in range(50):
    wait()
    print(i)
