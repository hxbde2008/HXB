#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar
import datetime
import time

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;

a = datetime.date.today()
c = str(a) + " 00:00:00"
print a
print c

b = time.asctime(time.localtime(time.time()))
print "本地时间为 :", b