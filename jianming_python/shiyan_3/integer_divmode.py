#!/usr/bin/env python3
days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days, 30))) #divmod(num1, num2)返回num1/num2的商和余数，*用来拆分元组(tuple)中的数据
