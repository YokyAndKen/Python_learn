import random
num = int(random.randint(1, 10))
guess1 = int(input("猜测1"))


if guess1 == num:
    print("true")
else:
    if guess1 > num:
        print("big")
    else:
        print("small")

    guess2 = int(input("猜测2"))

    if guess2 == num:
        print("true2")
    else:
        if guess2 > num:
            print("big")
        else:
            print("small")
    print(f"trueValue:{num}")
