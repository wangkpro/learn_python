#!/usr/bin/env python3
sticks = 21#棍子的总数是21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
#提醒有21根棍子，你可以每次拿1-4根棍子
print("Whoever will take the last stick will loose")
#提醒谁拿到最后一根棍子谁输

while True:
    print("Sticks left:", sticks)#输出目前剩余的棍子数量
    if sticks == 1:
        print("You took the last stick, you loose")#如果棍子数量等于1提示你输了
        break#退出while循环
    sticks_taken = int(input("Take sticks(1-4):"))#用input函数输入拿的棍子数，并用int函数转化为整数
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")#如果选的棍子数不符合要求，提示错误的选择
        continue
    print("Computer took:", (5 - sticks_taken), "\n")#电脑选择
    sticks -= 5 #每个循环棍子减5个
