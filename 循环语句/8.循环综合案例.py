import random
count = 10000
for item in range(20):
    score = int(random.randint(1, 10))
    if score >= 5:
        count -= 1000
        print(f"向员工{item + 1}发放工资1000元，账户余额还剩{ count }元")
    else:
        print(f"aa员工{item + 1}，绩效分{ score }，不发工资，下一位")

print