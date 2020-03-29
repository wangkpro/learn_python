#!/usr/bin/env python3
#指定运行程序
days = int(input("Enter days: "))#input函数提示输入天数，int函数将输入的天数转换成整数
months = days // 30 #//代表取商的整数部分
days = days % 30 #取余数
print("Months = {} Days = {}".format(months, days))
