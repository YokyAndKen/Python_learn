# 函数不写return语句就是返回none

def say_hi():
    print('yoky')

result = say_hi()

print(f"result的值：{result}")
print(f"result的类型：{type(result)}")