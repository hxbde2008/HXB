#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools

f = lambda x:x*x
print f(5)

int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')