i = 1
for i in range(1, 11):
    print(f"the {i} day")
    for j in range(1, 11, 2):
        print(f"the {j} flowers")

print(f"success! the {i} day")

# for循环九九乘法表练习
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {j * i}\t", end="")
    print("")