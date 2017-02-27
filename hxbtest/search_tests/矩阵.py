#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 这是一个对矩阵进行翻转的程序

#读入行列和转动方向

linNum = raw_input("请依次输入行列和转动方向：\n").split()
lines = int(linNum[0])
lists = int(linNum[1])
diration = int(linNum[2])

#创建对应行列的二维数组(矩阵)
mateix = [[0 for i in range(lists)]for i in range(lines)]

#输入矩阵各元素
for i in range(lines):
    linStr = input("")
    linNum = linStr.split(" ")
    for k in range(lists):
        mateix[i][k] = linNum[k]

#   进行行列变换
if diration == 0: #行变换
    for i in range(int(lines/2)):
        mateix[lines-i-1],mateix[i] = mateix[i],mateix[lines-i-1]
elif diration == 1: #列变换
    for i in range(lines):
        for j in range(int(lists/2)):
            mateix[i][lists-j-1],mateix[i][j] = mateix[i][j],mateix[i][lists-j-1]
else:
    print("error")

#打印输出矩阵
for i in mateix:
    for j in i:
        print(j,",")
    print()