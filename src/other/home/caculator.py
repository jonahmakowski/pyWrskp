# This is a simple calculator in the shell

def use(num1, t, num2):
    num1 = int(num1)
    num2 = int(num2)
    try:
        if t == '+':
            a = num1 + num2
            q = '{} + {}'.format(num1, num2)
        elif t == '-':
            a = num1 - num2
            q = '{} - {}'.format(num1, num2)
        elif t == '*':
            a = num1 * num2
            q = '{} * {}'.format(num1, num2)
        elif t == '/':
            a = num1 / num2
            q = '{} / {}'.format(num1, num2)
        elif t == '**':
            a = num1 ** num2
            q = '{} ** {}'.format(num1, num2)
        elif t == '^':
            from math import sqrt
            a = sqrt(num1)
            q = '√{}'.format(num1)
        else:
            a = "ISSUE CODE CAN NOT FIND NUMBERS NECESSARY, TALK TO THE OWNER OF THIS WEBSITE"
            q = a
    except:
        q = "ISSUE"
        a = "ISSUE"
    return q, a


c, d = use(input('What is the first number?'), input('What is the type?'), input('what is the other number?'))
print(c + ' = ' + str(d))
