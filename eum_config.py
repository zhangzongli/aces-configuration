#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from enum import Enum

# Number = Enum('Number', ('one', 'two', 'three'))

class Number(Enum):
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'


def getValue(name):
    result = ''
    for number in Number:
        if number.name == name :
            result = number.value
            break
    return result

def getName(value):
    result = ''
    for number in Number:
        if number.value == value:
            result = number.name
            break
    return result