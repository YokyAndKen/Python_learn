i = 1
while i <= 10:
    print(f"今天是第{i}天")
    j = 1
    while j <= 10:
        print(f"this is count{j}")
        j += 1
    print("hold on")
    i += 1
print(f"to{i - 1}")

# 案例 - 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t",  end='')
        j += 1
    i += 1
    print()