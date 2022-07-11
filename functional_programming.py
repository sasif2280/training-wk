# higher order functions in python
# demo program for higher order functions

def num1(num):
    return num


def num2(num):
    a = 5
    return a+num


def call(num1, num2):
    c = num2(num1(5))
    return c


print(call(num1, num2))
