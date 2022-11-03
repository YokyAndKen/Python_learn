name1 = "yoky"
name2 = "ken"
date = 20210922
message = name1 + " luv %s at %s" % (name2, date)
print(message)

# 字符串快速格式化  比较类似于vue的模板字符串的写法
message2 = (f"{name1} luv {name2} at {date}")
print(message2)