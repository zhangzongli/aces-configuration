#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 数字转文本
# 1 -> 01
# 10 -> 10
def intToStr(num):
    result = ""
    if num < 10 :
        result = "0"+str(num)
    else:
        result = str(num)
    return result