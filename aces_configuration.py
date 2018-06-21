#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os


def removeExists():
    path = "./text"
    if (os.path.exists(path)):
        os.remove(path)

def generateConfiguration():

    str = "hello"
    file = open("text", "x")
    file.write(str)
    file.close()

if __name__ == "__main__" :
    print("组态图代码开始生成")
    removeExists()
    generateConfiguration()

