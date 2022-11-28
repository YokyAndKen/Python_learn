# 局部变量和全局变量

def testA():
    num = 100
    print(num)

testA()
num = 1000
def testB():
    # 在函数体内部可以修改全局变量,但只在函数内部有用，在函数外部num还是原值，里面和外面的没有任何联系
    num = 200
    print(num)
testB()

def testC():
    # 在函数体内部可以修改全局变量,但只在函数内部有用，在函数外部num还是原值，里面和外面的没有任何联系
    # 但是可以通过global关键字将函数内部的变量设置为全局变量，这时候就可以在函数内部更改全局变量的值了
    global num
    num = 500
    print(num)
testC()

print(num)