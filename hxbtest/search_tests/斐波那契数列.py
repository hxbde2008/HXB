#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printFibo(number):
    a = 0
    b = 1
    i = 1

    while i < number:
        a, b = b, a+b
        i += 1
    return b

a = raw_input("请输入一个数字：");
num = int(a)

if num == 0:
    print 0
elif num == 1:
    print 1
else:
    print printFibo(num)

