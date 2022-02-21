from time import sleep


class Game:
    def __init__(self, debug=False, health=200, jonah=True):
        self.number = 1
        self.number_killed = 1
        self.health = health
        self.attacks = [{'name':'blast', 'damage min':1, 'damage max':20},
                        {'name':'punch', 'damage min':5, 'damage max':10},
                        {'name':'super blast', 'damage min':-100, 'damage max':300}]
        self.debug = debug
        self.name = input('What is your name?\n')
        
        if jonah == True and self.name == 'Jonah':
            self.health = health * 3
            for item in self.attacks:
                if item['damage min'] > 0:
                    item['damage min'] = item['damage min'] * 10
                if item['damage min'] < 0:
                    item['damage min'] = item['damage max'] - 1
                if item['damage max'] > 0:
                    item['damage max'] = item['damage max'] * 10
                if item['damage max'] < 0:
                    item['damage max'] = item['damage min'] - 1
                
            if self.debug:
                print('debug info: self.name == Jonah, so cheat mode has been enabled')
        
        self.print_info()
        
        if self.debug:
            print('debug info: self.print_info, done')
        
        sleep(2)
        while True:
            self.choose_bad()
            
            if self.debug:
                print('debug info: self.choose_bad, done \nnum {}'.format(self.number))
                
            self.number += 1
    
    def print_info(self):
        print('Hello {}!'.format(self.name))
        print('You have {} health'.format(self.health))
        print('Weapons you can use:')
        for item in self.attacks:
            print('\t{} ({} - {} damage)'.format(item['name'], item['damage min'], item['damage max']))
        print('Bad Guys:')
        print('\tGLOP - 10-20 attack damage - 50 health')
        print('\tBlock - 50 attack damage - 20 health')
    
    def choose_bad(self):
        from random import randint
        
        num = randint(1,2)
        if self.debug:
            print('debug info: num in self.choose_bad is {}'.format(num))
        if num == 1:
            self.glop()
            self.number_killed += 1
        elif num == 2:
            self.block()
            self.number_killed += 1
        elif self.debug:
            print('debug info: issue, code could not find nums nessary\nsection: self.choose_bad')
        print('\n')
    
    def glop(self):
        from random import randint
        monster_health = 50
        print('you meet a Glop!')
        while monster_health > 0 and self.health > 0:
            skip = False
            attack = input('What attack do you use {}? \n'.format(self.name))
            attack = attack.lower()
            if self.debug:
                print('debug info: attack input = {}'.format(attack))
            for item in self.attacks:
                if item['name'] == attack:
                    attack_dic = item
                    break
                else:
                    attack_dic = False
            if attack_dic == False:
                print('{} is not an attack name'.format(attack))
                print('Printing info again:')
                print('\n')
                self.print_info()
                skip = True
            
            if not skip:
                damage = randint(attack_dic['damage min'], attack_dic['damage max'])
                print('The Glop lost {} health'.format(damage))
                monster_health -= damage
                print('The Glop now has {} health'.format(monster_health))
                damage = randint(10, 20)
                print('The monster did {} damage'.format(damage))
                self.health -= damage
                print('You now have {} health'.format(self.health))
        if self.health <= 0:
            print('you died!')
            print('GAME OVER')
            print('You killed {} bad guys'.format(self.number_killed))
            exit()
        else:
            print('GOOD JOB!')
            print('You killed the Glop with {} health to spare!'.format(self.health))
            print('You killed {} bad guys so far'.format(self.number_killed))
    
    def block(self):
        from random import randint
        monster_health = 20
        print('you meet a block!')
        while monster_health > 0 and self.health > 0:
            skip = False
            attack = input('What attack do you use {}? \n'.format(self.name))
            attack = attack.lower()
            if self.debug:
                print('debug info: attack input = {}'.format(attack))
            for item in self.attacks:
                if item['name'] == attack:
                    attack_dic = item
                    break
                else:
                    attack_dic = False
            if attack_dic == False:
                print('{} is not an attack name'.format(attack))
                print('Printing info again:')
                print(']n')
                self.print_info()
                skip = True
            
            if not skip:
                damage = randint(attack_dic['damage min'], attack_dic['damage max'])
                print('The block lost {} health'.format(damage))
                monster_health -= damage
                print('The block now has {} health'.format(monster_health))
                damage = 50
                print('The monster did {} damage'.format(damage))
                self.health -= damage
                print('You now have {} health'.format(self.health))
        if self.health <= 0:
            print('you died!')
            print('GAME OVER')
            print('You killed {} bad guys'.format(self.number_killed))
            exit()
        else:
            print('GOOD JOB!')
            print('You killed the block with {} health to spare!'.format(self.health))
            print('You killed {} bad guys so far'.format(self.number_killed))


User = Game(debug=True) # add debug = True for debug info
