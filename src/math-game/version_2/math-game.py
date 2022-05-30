from random import randint
from time import sleep


class MathGame:
    def __init__(self, high, low, fl=False, end=10):
        self.high = high
        self.low = low
        self.money = 0
        self.correct = 0
        self.incorrect = 0
        self.end = end
        self.fl = fl
        self.error = False
    
    def mainloop(self):
        while self.incorrect < self.end:
            self.error = False
            num = randint(1, 4)
            
            if num == 1:
                self.add()
            elif num == 2:
                self.subtract()
            elif num == 3:
                self.multiply()
            elif num == 4:
                self.divide()

            if not self.error:
                print('STATS:')
                print('\tMoney: {}'.format(self.money))
                print('\tCorrect: {}'.format(self.correct))
                print('\tIncorrect: {}'.format(self.incorrect))
                sleep(3)
                print('\n')
                print('\n')
    
    def add(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 + num2
        
        if (isinstance(a, float) and self.fl) or (a < 0 and self.fl):
            self.error = True
            return
        
        while True:
            try:
                ask = int(input('What is {} + {}?\n'.format(num1, num2)))
                break
            except ValueError:
                print('That is not a number!')
        
        earned = randint(1, 5)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('Incorrect!')
            print('The correct answer is {}'.format(a))
            self.incorrect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
            
    def subtract(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 - num2
        
        if (isinstance(a, float) and self.fl) or (a < 0 and self.fl):
            self.error = True
            return
        
        while True:
            try:
                ask = int(input('What is {} - {}?\n'.format(num1, num2)))
                break
            except ValueError:
                print('That is not a number!')
        
        earned = randint(1, 7)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('incorrect!')
            print('The correct answer is {}'.format(a))
            self.incorrect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
    
    def multiply(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 * num2
        
        if (isinstance(a, float) and self.fl) or (a < 0 and self.fl):
            self.error = True
            return
        
        while True:
            try:
                ask = int(input('What is {} * {}?\n'.format(num1, num2)))
                break
            except ValueError:
                print('That is not a number!')
        
        earned = randint(1, 10)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('incorrect!')
            print('The correct answer is {}'.format(a))
            self.incorrect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
    
    def divide(self):
        num1 = randint(self.low, self.high)

        while True:
            num2 = randint(self.low, self.high)
            if num2 != 0:
                break
        a = num1 / num2
        
        if (isinstance(a, float) and self.fl) or (a < 0 and self.fl):
            self.error = True
            return
        
        while True:
            try:
                ask = int(input('What is {} / {}?\n'.format(num1, num2)))
                break
            except ValueError:
                print('That is not a number!')
        
        earned = randint(1, 15)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('incorrect!')
            print('The correct answer is {}'.format(a))
            self.incorrect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)


math = MathGame(int(input('What would you like the largest number to be?')),
                int(input('What would you like the lowest number to be?')),
                fl=True)
math.mainloop()
