class MathClickerGame:
    def __init__(self):
        self.coin = 0
        self.owned_power_ups = []
        self.mainloop()

    def mainloop(self):
        i = 1
        while True:
            info = int(input('What is {} + {}'.format(i, i)))
            if info == i + i:
                print('you got 1 coin')
                self.coin += 1
                print('you now have ' + str(self.coin) + ' coins')
            elif info != i + i:
                print('mrrrrrrrrrrrrrr')
                print('wrong')

            shop = input('if you want to get to the shop input c')

            if shop == 'c':
                self.shop()

            i += 1

    def shop(self):
        power_ups = [{'name': 'Testing', 'price': 1}]

        print('name, price')

        for item in power_ups:
            print(item['name'], ', ', item['price'])

        buy = input('What would you like to buy? (name or none)')

        if buy == 'none':
            print('closing shop')
            return

        for i in range(len(power_ups)):
            if buy == power_ups[i]['name']:
                print('are you sure?')
                print('This costs {} coin(s)'.format(power_ups[i]['price']))
                sure = input('y/n')
                if sure == 'y':
                    if self.coin < power_ups[i]['price']:
                        print('you do not have enough money')
                        return
                    print('item bought')
                    print('the power up(s) you have now are:')
                    self.owned_power_ups.append(power_ups[i]['name'])
                    for item in self.owned_power_ups:
                        print(item)
                else:
                    print('ok, closing shop')
                    return


game = MathClickerGame()
