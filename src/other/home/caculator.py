# This is a simple caculator in the shell

def use(num1, num2, type):
        try:
            if type == '+':
                a = num1 + num2
                q = '{} + {}'.format(num1, num2)
            elif type == '-':
                a = num1 - num2
                q = '{} - {}'.format(num1, num2)
            elif type == '*':
                a = num1 * num2
                q = '{} * {}'.format(num1, num2)
            elif type == '/':
                a = num1 / num2
                q = '{} / {}'.format(num1, num2)
            elif type == '**':
                a = num1 ** num2
                q = '{} ** {}'.format(num1, num2)
            elif type == '^':
                from math import sqrt
                a = sqrt(num1)
                q = '√{}'.format(num1)
            else:
                a = "ISSUE CODE CAN NOT FIND NUMBERS NESSARY, TALK TO THE OWNER OF THIS WEBSITE"
        except:
            q = "ISSUE"
            a = "ISSUE"
        return q, a
use(input('What is the first number?'), input('What is the type?'), input('what is the other number?'))