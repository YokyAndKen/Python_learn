my_str = "Ken Luv Yoky"

# 通过下标索引取值
print(my_str[2])
print(my_str[-2])
# index方法
value = my_str.index('Luv')
print(value)
# 此处会返回luv单词的起始下标

# replace方法
my_str_2 = my_str.replace('Yoky', 'lyx')
print(my_str_2)
# split方法
my_list = my_str.split('n')
print(my_list)
# strip方法
my_str_space = "    ken luv yoky"
my_str_nospace = my_str_space.strip()
print(my_str_nospace)
# 统计字符串中某字符串出现的次数
#  count
# 统计字符串的长度
#  len