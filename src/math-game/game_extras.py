from random import randint

def add(max_num, min_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 + num2
    return num1, num2, a

def sub(max_num, min_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 - num2
    return num1, num2, a

def multi(max_num, min_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 * num2
    return num1, num2, a

def div(max_num, min_num):
    num1 = randint(max_num, min_num)
    num2 = randint(max_num, min_num)
    a = num1 / num2
    return num1, num2, a