class MathClickerGame:
    def __init__(self):
        self.coin = 0
        self.owned_power_ups = []
        self.other_power_ups = [{'name': 'double coin income', 'price': 10}]
        self.mainloop()

    def mainloop(self):
        i = 1
        while True:
            double = self.if_inside_list(self.owned_power_ups, 'double coin income')
            info = int(input('What is {} + {}'.format(i, i)))
            if info == i + i:
                if double:
                    print('you got 2 coins')
                    self.coin += 2
                elif not double:
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
        print('name, price')

        for item in self.other_power_ups:
            print(item['name'], ', ', item['price'])

        buy = input('What would you like to buy? (name or none)')

        if buy == 'none':
            print('closing shop')
            return

        for i in range(len(self.other_power_ups) - 1):
            if buy == self.other_power_ups[i]['name']:
                print('are you sure?')
                print('This costs {} coin(s)'.format(self.other_power_ups[i]['price']))
                sure = input('y/n')
                if sure == 'y':
                    if self.coin < self.other_power_ups[i]['price']:
                        print('you do not have enough money')
                        return
                    print('item bought')
                    print('the power up(s) you have now are:')
                    self.owned_power_ups.append(self.other_power_ups[i]['name'])
                    self.coin -= self.other_power_ups[i]['price']
                    for item in self.owned_power_ups:
                        print(item)
                    del self.other_power_ups[i]
                else:
                    print('ok, closing shop')
                    return

    def if_inside_list(self, lis, item):
        for i in lis:
            if i == item:
                return True
        return False


if __name__ == "__main__":
    game = MathClickerGame()
