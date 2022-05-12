import time
import random


def monster_fight(monster_name, monster_health, monster_damage_range, player_username, player_health, player_items):
    print('A {} is fighting you, {}!'.format(monster_name, player_username))
    print('It has {} health!'.format(monster_health))
    print('It can do from {} to {} damage!'.format(monster_damage_range[0], monster_damage_range[1]))

    while player_health >= 1 and monster_health >= 1:
        print('What attack would you like to use?')
        print('Here are your options:')
        for item in player_items:
            print('Name: {}, Damage: {}'.format(item['name'], item['damage']))
        current_correct = False
        current_attack_name = input('choose one\n')
        for item in player_items:
            if item['name'] == current_attack_name:
                current_attack_damage = int(item['damage'])
                current_correct = True

        if current_correct:
            print('You did {} damage!'.format(current_attack_damage))

            time.sleep(0.5)

            monster_health -= current_attack_damage

            print('The monster now has {} health!'.format(monster_health))
            if monster_health < 1:
                break

            monster_damage = random.randint(monster_damage_range[0], monster_damage_range[1])

            print('the monster does {} damage!'.format(monster_damage))

            time.sleep(1)
            player_health -= monster_damage

            print('you now have {} health!'.format(player_health))

    if player_health <= 0:
        print('You Died!')
        exit(0)
    elif monster_health <= 0:
        print('Good Job!')
        print('you beat the {}!'.format(monster_name))
        return player_health


health = 100
items = []

print('Welcome To My Game!')
time.sleep(1)

username = input('Stranger: What is your username, brave adventurer?\n')

time.sleep(1)

print()
print()

print('Stranger: Welcome to Alglia {}!'.format(username))

time.sleep(1)

why = input('Stranger: What brings you here?\nthe challange?\n')

if why != 'the challenge' and why != 'yes':
    print('{} is not allowed'.format(why))
    print('code is terminated')
    exit(4913901809481390841)

print('Stranger: I knew it!')
print()
print('Stranger: I will tell you what is happening, a group of monstors has come and have been attacking the village for months now, the poorer people are running out of food, we need help, fast')
print('Stranger: I think you might just be the help we need!')
print('Stranger: My name is Bob')
print('Bob: Come, you can sleep in my house tonight!')
time.sleep(2)

print()
print('Bob: WAKE UP!!!')
time.sleep(0.5)
print('Bob: We need your help, there is a dhfai attacking us!')
print('Bob: Here is a sword...')

time.sleep(0.5)

print()
print('YOU GOT A SWORD!')
items.append({'name': 'Sword', 'damage': '10'})

time.sleep(0.5)

health = monster_fight('dhfai', 50, [10, 25], username, health, items)

time.sleep(0.5)

print('Thanks for helping us!')
print('let me heal you')

time.sleep(2)

health = 100

print('There you are!')
print('Good job out there!')
print('I think it is time you go out on your own!')