import time
import random


def monster_fight(
    monster_name,
    monster_health,
    monster_damage_range,
    player_username,
    player_health,
    player_items,
):
    print("A {} is fighting you, {}!".format(monster_name, player_username))
    print("It has {} health!".format(monster_health))
    print(
        "It can do from {} to {} damage!".format(
            monster_damage_range[0], monster_damage_range[1]
        )
    )

    time.sleep(3)

    while player_health >= 1 and monster_health >= 1:
        current_attack_damage = 0
        print()
        print()
        print()
        print()

        print("What attack would you like to use?")
        print("Here are your options:")
        for item in player_items:
            print("Name: {}, Damage: {}".format(item["name"], item["damage"]))
        current_correct = False
        current_attack_name = input("choose one\n")
        for item in player_items:
            if item["name"] == current_attack_name:
                current_attack_damage = int(item["damage"])
                current_correct = True

        if current_correct:
            print("You did {} damage!".format(current_attack_damage))

            time.sleep(0.5)

            monster_health -= current_attack_damage

            print("The monster now has {} health!".format(monster_health))
            if monster_health < 1:
                break

            monster_damage = random.randint(
                monster_damage_range[0], monster_damage_range[1]
            )

            print("the monster does {} damage!".format(monster_damage))

            time.sleep(1)
            player_health -= monster_damage

            print("you now have {} health!".format(player_health))
            time.sleep(1)

    if player_health <= 0:
        print("You Died!")
        exit(0)
    elif monster_health <= 0:
        print("Good Job!")
        print("you beat the {}!".format(monster_name))
        return player_health


def learn_spell(spell):
    print("you are learn how to cast the {} spell".format(spell))

    for i in range(5):
        time.sleep(0.5)

        print()
        print("Woosh")

        time.sleep(0.5)

        print()
        print("BANG")

        time.sleep(0.5)

        print()
        print("CRASH")

    print("Good Job!")
    time.sleep(0.5)
    print("You have learned the spell!")


def learn_all(dic, objects):
    if dic["type"] == "s":
        del dic["type"]
        learn_spell(dic["name"])
        objects.append(dic)
        return items
    elif dic["type"] == "w":
        del dic["type"]
        objects.append(dic)
        return items
    else:
        print("ERROR")
        exit()


def make_monster(letters):
    creation_health = random.randint(10, 500)

    creation_name = ""
    for i in range(random.randint(1, 50)):
        creation_name += letters[random.randint(0, len(letters) - 1)]

    creation_attack_range = [0, random.randint(1, 200)]

    return creation_name, creation_health, creation_attack_range


abcs = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    " ",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    ".",
    ",",
    "[",
    "]",
    "{",
    "}",
    ":",
    ";",
    "'",
    '"',
    "?",
]


"""
this is the format for the dic below:
{'name': '', 'damage': '', 'type': ''}
"""


unlearned = [
    {"name": "Sword", "damage": "10", "type": "w"},
    {"name": "Flame Tongue", "damage": "20", "type": "s"},
    {"name": "Spear", "damage": "25", "type": "w"},
    {"name": "Flame Dance", "damage": "40", "type": "s"},
    {"name": "Scythe", "damage": "60", "type": "w"},
    {"name": "Lightning Strike", "damage": "120", "type": "s"},
    {"name": "Javelin", "damage": "80", "type": "w"},
    {"name": "Fire dance", "damage": "200", "type": "s"},
]
health = 100
items = []

print("Welcome To My Game!")
time.sleep(1)

username = input("Stranger: What is your username, brave adventurer?\n")

time.sleep(1)

print()
print()

print("Stranger: Welcome to Alglia {}!".format(username))

time.sleep(1)

why = input("Stranger: What brings you here?\nthe challange?\n")

if why != "the challenge" and why != "yes":
    print("{} is not allowed".format(why))
    print("code is terminated")
    exit(4913901809481390841)

print("Stranger: I knew it!")
print()
print(
    "Stranger: I will tell you what is happening, a group of monstors has come and have been attacking the village for months now, the poorer people are running out of food, we need help, fast"
)
print("Stranger: I think you might just be the help we need!")
print("Stranger: My name is Bob")
print("Bob: Come, you can sleep in my house tonight!")
time.sleep(2)

print()
print("Bob: WAKE UP!!!")
time.sleep(0.5)
print("Bob: We need your help, there is a dhfai attacking us!")
print("Bob: Here is a sword...")

time.sleep(0.5)

print()
print("YOU GOT A SWORD!")
learn_all(unlearned[0], items)
del unlearned[0]
print("It Does 10 Damage!")

time.sleep(0.5)

health = monster_fight("dhfai", 50, [10, 25], username, health, items)

time.sleep(0.5)

print("Bob: Thanks for helping us!")
print("Bob: Let me heal you")

time.sleep(2)

if username == "WhiteSwine":
    health = 10000
else:
    health = 500

print("Bob: There you are, your health is now {}!".format(health))
print("Bob: Good job out there!")
print("Bob: I think it is time you go out on your own!")
time.sleep(1)
print("Bob: but first, you need something better than a Sword!")

time.sleep(2)
print("Here is my old wand, it will let you cast spells!")
print("I will teach you how to cast the first, and most basic spell, here")

learn_all(unlearned[0], items)

print("YOU GOT THE SPELL FLAME TONGUE!")
del unlearned[0]
print("It Does 20 Damage!")

while len(unlearned) > 0:
    info_name, info_health, info_damage_range = make_monster(abcs)
    monster_fight(info_name, info_health, info_damage_range, username, health, items)

    print()
    learn_all(unlearned[0], items)
    print("You learned how to use the {}".format(unlearned[0]["name"]))
    print()

print("Good Job!")
print("You Beat the Game!")
