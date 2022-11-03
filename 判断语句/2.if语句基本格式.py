age = 22

if age >= 18:
    print("adult")



# if else 判断练习：
age = input("请输入年龄")
age = int(age)
if age >= 18:
    print(f"your age is {age}, already adult, ticket price = 10")
else:
    print("teenager")


# if elif else 判断练习：
name = input("请输入姓名")
age1 = int(input("age"))
if name == "yoky":
    print("yoky")
elif age1 == 20:
    print("20")
else:
    print("else")

# 数字猜测练习
num = int(input("请输入你想的数字"))
if int(input("请输入你猜的数字1")) == num:
    print("猜对了")
elif int(input("不对，再猜一次")) == num:
    print("猜对了")
elif int(input("不对，再猜一次")) == num:
    print("猜对了")
else:
    print(f"全部猜错了，我想的是： {num}")

