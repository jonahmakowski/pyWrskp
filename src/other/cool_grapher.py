m = int(input('What is the rate of change?'))
b = int(input('What is number zero?'))
x = 1
threshold = int(input('What x are you looking for?')) + 1
while True:
    while x < threshold:
        print()
        print()
        number = m * x
        number += b
        print(number)
        print(x)
        if threshold > 1000000:
            if threshold > 1000000000000:
                x += 100000000000
            else:
                x += 10
        else:
            x += 1
    cont = input('x = {}, would you like to continue? y/n\nif y, x will increase by 100'.format(x - 1))
    if cont == 'n':
        break
    else:
        threshold += 100
