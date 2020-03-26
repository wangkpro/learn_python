#逢7跳过
for a in range(1,101):
    if a % 7 == 0:#除以7余数为0
        continue
    elif a % 10 == 7:#除以10余数为0
        continue
    elif a // 10 == 7:#除以10取整数为7
        continue
    else:
        print(a)
