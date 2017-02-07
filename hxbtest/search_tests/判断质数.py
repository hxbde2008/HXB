#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = raw_input("请输入一个数字：\n")
while not a.isdigit():
    a=raw_input('不是数字，请重新输入：\n')
num = int(a)
if num < 2:
    print "NO"
else:
    if (0 not in [num % i for i in range(2,num)]):
        print "YES"
    else:
        print "NO"