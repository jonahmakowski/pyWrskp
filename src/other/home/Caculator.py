A = input('What opration would you like to do?\n* is multiplying, / is dividing, - is subtracting, + is adding\n')

B = int(input('What is the 1st number you want to ' + A  + '?\n'))
C = int(input('What is the 2nd number you want to ' + A  + '?\n'))

if A == ('*'):
    D = B * C

if A == ('/'):
    D = B / C

if A == ('+'):
    D = B + C

if A == ('-'):
    D = B - C

print (str(B) + ' ' + A + ' ' + str(C) + ' ' + '=' + ' ' + str(D))
