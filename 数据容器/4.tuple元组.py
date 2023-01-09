# 元组的定义
  #  是一个只读的list，所以当我们需要在程序内封装数据，并且不允许数据被篡改，就使用元组

# 定义元组
t1 = (1, 'hello', True)
t2 = ()
t3 = tuple()

print(f"t1的类型是{type(t1)}， 内容是{t1}")
# 定义单个元素的元组
# 定义单个元素的元组，必须要在后面写一个空的逗号
t4 = ('hello', )
print(f"t4的类型是{type(t4)}， 内容是{t4}")

# 嵌套
t5 = ((1,2,3), (4,5,6))
# 利用下标从元组中取出元素
print(t5[1][2])
# 元组的操作： index查找方法
t6 = ('ken', 'luv', 'yoky')
index = t6.index('yoky')
print(index)
# 元组的操作： count统计方法
t7 = ('ken', 'luv', 'yoky', 'yoky', 'yoky', 'yoky')
num = t7.count('yoky')
print(num)
# 元组的操作： len函数统计元组元素数量
leng = len(t7)
print(leng)
# 元组的遍历： while
num = 0
while index < len(t7):
    print(t7[num])
    num += 1
# 元组的遍历：for
for element in t7:
    print(f" for {element}")