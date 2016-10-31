#!/usr/bin/python
# -*- coding: UTF-8 -*-

a, b = "Hello World!", "世界你好"
hxb = ['hxb', 888, 1.32, '上山打老虎', 3.3]
hxb[1] = 1000
dc = {'name': 'hxb', 'code': '12345', 'work': '上山打老虎'}
if ( a in hxb ):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"
print a
print b
print a+b
print a[0:5]
print a[0]
print hxb[3]
print dc.keys()
print dc.values()
print a is not b
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i