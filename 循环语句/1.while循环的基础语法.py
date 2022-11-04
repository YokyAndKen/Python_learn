i = 0
while i < 10:
    print("yoky")
    i += 1


# 练习
flag = 0
j = 1
while j <= 100:
    flag = flag + j
    j += 1

print("flag", flag)


# while 循环猜数字案例

import random
num = int(random.randint(1, 10))
flag = True
count = 1
while flag:
    guess_num = int(input("请输入数字"))
    if guess_num == num:
        print(f"yes,  count={count}")
        flag = False
    else:
        if guess_num < num:
            print("小了")
        else:
            print("大了")
        count += 1