#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = int(raw_input("请输入一个数字："));
a = 0
b = 1
i = 0

while i < num:
    print a
    a, b = b, a+b
    i += 1

