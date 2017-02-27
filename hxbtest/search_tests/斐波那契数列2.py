#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printFibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return printFibo(n-1)+printFibo(n-2)

a = raw_input("请输入一个数字：");
num = int(a)

print printFibo(num)