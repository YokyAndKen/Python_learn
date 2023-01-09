# 序列  --  切片

my_list = [0,1,2,3,4,5,6]

# 步长默认为1，可以省略不写
my_list_1 = my_list[1:4]
print(my_list_1)

# 从头开始，到末尾结束，步长为1  开头和结尾和步长1都可以省略
my_list_2 = my_list[:]
print(my_list_2)

# 从头开始，到末尾结束，步长为2
my_list_3 = my_list[: :2]
print(my_list_3)

# 从头开始，到末尾结束，步长为-1
my_list_4 = my_list[::-1]
print(my_list_4)
# 此举相当于将序列反转

# 从3开始到1结束，步长-1
my_list_5 = my_list[3:1:-1]
print(my_list_5)
