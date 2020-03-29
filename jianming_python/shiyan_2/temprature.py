#!/usr/bin/env python3
#定义运行程序为python3
fahrenheit = 0 #定义变量fahrenheit的初始值为0
print("Fahrenheit Celsius") 
while fahrenheit <= 250:  #while循环
    celsius = (fahrenheit - 32) / 1.8  # 转换为摄氏度
    print("{:5d} {:7.2f}".format(fahrenheit , celsius)) #使用format函数输出结果
    fahrenheit = fahrenheit + 25 #每个循环加25
