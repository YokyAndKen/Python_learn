
# 列表的遍历

# while

mylist = ['ken', 'luv', 'yoky']

def list_while_func(list):
    index = 0
    while index < len(list):
        list[index] = list[index] + '1'
        index += 1
    print(list)

list_while_func(mylist)

mylist2 = ['ken', 'luv', 'yoky']

def list_for_func(list):
    for e in list:
        print(e)

list_for_func(mylist2)