#!/usr/bin/python
# -*- coding: UTF-8 -*-

M,N = raw_input("请输入2个数字：\n").split();
m = int(M)
n = int(N)
if m%n == 0:
    print "YES"
else:
    print "NO"