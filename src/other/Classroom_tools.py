from random import randint as r


class Classroom:
    def __init__(self):
        self.roster = []
        self.teacher = ''
        self.princaple = ''
        self.school_name = ''
        self.add_roster()

    def add_roster(self):
        print('Enter all of the students names:')
        while True:
            name = input('')
            if name == '':
                break
            self.roster.append(name)

    def team_maker(self):
        num_of_teams = input('How many teams would you like?')
        teams = []
        for i in range(int(num_of_teams)):
            teams.append([])
        roster_copy = self.roster
        
        while len(roster_copy) >= int(num_of_teams):
            for item in teams:
                person_num = r(0, len(roster_copy) - 1)
                person_name = roster_copy[person_num]
                del roster_copy[person_num]
                item.append(person_name)
        
        if len(roster_copy) > 0:
            i = 0
            while len(roster_copy) > 0:
                teams[i].append(roster_copy[0])
                del roster_copy[0]
                i += 1
        
        team_num = 0
        for item in range(len(teams)):
            print('Team {}'.format(team_num + 1))
            for i in range(len(teams[team_num])):
                print(teams[team_num][i])
            team_num += 1
            print('\n\n')

    def math_game(self):
        print('WELCOME TO')
        print("JONAH'S MATH GAME!")
        print('entering nothing will end the game!')
        coins = 0
        while True:
            opration = r(1, 4)
            num_1 = r(0, 9999999)
            num_2 = r(0, 9999999)
            if opration == 1:
                opration = '+'
                question = '{} {} {}'.format(num_1, opration, num_2)
                a = str(num_1 + num_2)
            elif opration == 2:
                opration = '-'
                question = '{} {} {}'.format(num_1, opration, num_2)
                a = str(num_1 - num_2)
            elif opration == 3:
                opration = '*'
                question = '{} {} {}'.format(num_1, opration, num_2)
                a = str(num_1 * num_2)
            elif opration == 4:
                opration = '/'
                question = '{} {} {}'.format(num_1, opration, num_2)
                a = str(num_1 / num_2)
            else:
                print('error')
                question = 'error'  # this is to solve an error found by pycharm
                a = 'error'  # this is to solve an error found by pycharm
                exit(404)
            g = input('What is ' + question + '?')
            if g == '':
                break
            elif g == a:
                print('Good job you got it correct! you earned 10 coins')
                coins += 10
                print('You now have {} coins'.format(coins))
            else:
                print('You got it incorrect, you lost 5 coins')
                coins -= 5
                print('You now have {} coins'.format(coins))

        print('GAME OVER')
        print('You have {} coins right now'.format(coins))


testing_class = Classroom()
do = input('What do you want to do?')
if do == 'team maker':
    testing_class.team_maker()
elif do == 'math game':
    testing_class.math_game()
