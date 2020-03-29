#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number of inputs sold: "))
price = float(input("Enter the price of camera: "))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("Bonus        = {:6.2f}".format(bonus)) #等号左右的空格可以多加
print("Commission   = {:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bonus + commission))
#冒号:表示对大括号中内容格式的限制，如6代表宽度为6即6个空格的位置，.2f表示保留两位小数
