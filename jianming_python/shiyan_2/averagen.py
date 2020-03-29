#!/usr/bin/env python3 
#设置该脚本的运行程序为python3
N = 10 #定义变量N为10
sum = 0 #定义sum变量初始值为0（顺带赋予了整数int类型，但是后续可以改动）
count = 0
print("please input 10 numbers:")
while count < N:  #while循环，满足条件就一直循环，不满足停止
    number = float(input()) #将输入的字符串用float函数转为浮点数并赋值给number变量
    sum = sum + number #每次循环都将sum加上一个number的赋值
    count = count + 1 #每循环一次给count变量加1
average = sum / N  #while循环结束后将sum除以N求平均数并赋值给变量average
print("N = {}, Sum = {}".format(N, sum))  #{}表示先留空不写，然后将format函数格式化后的内容填入前面的大括号，大括号的位置与后面format括号里的变量顺序一致
print("Avervage = {:.2f}".format(average)) #{}表示先留空不写，{}中的:.2f表示将浮点数保留两位小数
