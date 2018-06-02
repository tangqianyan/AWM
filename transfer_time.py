#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name:
#Author: chi xiao
#Mail: 
#Created Time:
############################

import time
import sys
import getopt


def show_time(sec):
    o = time.strftime("%Y-%m-%d %H:%M:%S",sec)
    print(o)

if __name__ == "__main__":
    method = ''
    sec = ''
    try:
        if len(sys.argv) <= 1:
            sys.exit(0)
        options, args = getopt.getopt(sys.argv[1:],"m:s:",
                                      ["method=","sec="])
        for k , v in options:
            if k in ('-m',"--method"):
                method = v
            if k in ('-s',"--sec"):
                sec = time.localtime(float(long(v)))
    except Exception, e:
        print(e)
        sys.exit(1)
    if method == 'sec':
        show_time(sec)
    elif method == 'msec':
        show_time(sec/1000.0)
    sys.exit(0)

