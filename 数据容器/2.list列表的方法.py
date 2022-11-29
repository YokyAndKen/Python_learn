mylist = ['ken', 'yoky']


# 查询列表中元素的下标索引
index = mylist.index('yoky')

# 查询列表中元素的下标索引  --  如果元素不存在于列表中会报错
# index1 = mylist.index('hello')   --报错

print(index)

# print(index1)   --报错


# 修改列表中元素的值
mylist[1] = 'Yoky'

print(mylist)


# 在列表中插入元素，列表.insert(下标索引，传入的元素）
mylist.insert(1,'luv')

print(mylist)

# 在列表的尾部追加指定元素   列表.append(元素)
mylist.append('forever')
print(mylist)

# 在列表的尾部追加一批元素，列表.extend(其他的数据容器)
mylist.extend([9,22])
print(mylist)

# 删除元素，del列表[下标]  |  列表.pop(下标)  <-- 可以获取到被删除的元素
del mylist[-1]
print(mylist)

element = mylist.pop(-1)
print(mylist)
print(element)

# 删除某元素在列表中的第一个匹配项  |  删除指定内容的元素   列表.remove(元素)
mylist.remove('forever')
print(mylist)

# 清空列表  列表.clear()
mylist.clear()
print(mylist)

# 统计某元素在列表中的数量   列表.count(元素)
mylist.extend(['ken','luv', 'yoky', 'ken'])
count = mylist.count('ken')
print(count)

# 统计列表中总共有多少个元素  len(列表)
print(len(mylist))




