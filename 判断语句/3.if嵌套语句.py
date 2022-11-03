if int(input("输入身高")) > 120:
    print("height>120, need price")
    print("vip?")

    if int(input("输入vip等级")) > 3:
        print("vip>3,free")
    else:
        print("need ticket")
else:
    print("free")