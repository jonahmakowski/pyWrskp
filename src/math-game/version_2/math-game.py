from random import randint
from time import sleep

class MathGame:
    def __init__(self, high, low, end=10):
        self.high = high
        self.low = low
        self.money = 0
        self.correct = 0
        self.incorrect = 0
        self.end = end
    
    def mainloop(self):
        while self.incorrect < self.end:
            num = randint(1, 4)
            
            if num == 1:
                self.add()
            elif num == 2:
                self.subtract()
            elif num == 3:
                self.multiply()
            elif num == 4:
                self.divide()
            
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
        while True:
            try:
                ask = int(input('What is {} + {}?\n'.format(num1, num2)))
                break
            except:
                print('That is not a number!')
        
        earned = randint(1, 5)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('Inccorect!')
            print('The correct awnser is {}'.format(a))
            self.incorect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
            
    
    def subtract(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 - num2
        while True:
            try:
                ask = int(input('What is {} - {}?\n'.format(num1, num2)))
                break
            except:
                print('That is not a number!')
        
        earned = randint(1, 7)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('Inccorect!')
            print('The correct awnser is {}'.format(a))
            self.incorect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
    
    def multiply(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 * num2
        while True:
            try:
                ask = int(input('What is {} * {}?\n'.format(num1, num2)))
                break
            except:
                print('That is not a number!')
        
        earned = randint(1, 10)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('Inccorect!')
            print('The correct awnser is {}'.format(a))
            self.incorect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)
    
    def divide(self):
        num1 = randint(self.low, self.high)
        num2 = randint(self.low, self.high)
        a = num1 / num2
        while True:
            try:
                ask = int(input('What is {} / {}?\n'.format(num1, num2)))
                break
            except:
                print('That is not a number!')
        
        earned = randint(1, 15)
        
        if ask == a:
            print('Good Job!!!')
            print('You earned {} money!'.format(earned))
            self.money += earned
            self.correct += 1
            sleep(0.5)
        else:
            print('Inccorect!')
            print('The correct awnser is {}'.format(a))
            self.incorect += 1
            print('You lost {} money'.format(earned))
            self.money -= earned
            sleep(0.5)

math = MathGame(int(input('What would you like the largest number to be?')), int(input('What would you like the lowest number to be?')))
math.mainloop()