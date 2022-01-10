coin = 0
i = 1
while True:
    info = int(input('What is {} + {}'.format(i, i)))
    if info == i + i:
        print('you got 1 coin')
        coin += 1
        print('you now have ' + str(coin) + ' coins')
    #print('if you want to get to the shop press c')
    elif info != i + i:
        print('mrrrrrrrrrrrrrr')
        print('wrong')
    i += 1