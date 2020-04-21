#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Interger: "))
    if n < 0:
        continue #这里返回到循环开始处执行，应该是第三行
    elif n == 0:
        break #n=0时退出循环
    print("Square is", n ** 2)#这种字符和数字之间会多1个空格
    print("Square is",n ** 2)#这种会多1个空格
    print("square is"+str(n ** 2))#这种不会多出空格
print("Goodbye")
