#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

t = [1, 3, 'shet', 1.11, 'rad']
a = random.choice(t)
print a
b = random.randrange(1, 100, 1)
print b
print random.random()
random.shuffle(t)
print t
print random.uniform(1, 1)
hi = '''hello'''
print hi
