#!/usr/bin/env python3
x = int(input("Please enter an integer:"))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:#注意冒号
    print("Single")
else:#注意冒号
    print("More")
