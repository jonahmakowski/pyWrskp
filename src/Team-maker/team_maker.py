"""
I know I have an older team maker, but I thought I would use what I have learned so far to make a brand new one!

Here it is:
"""

import os
from random import randint
import json

try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')


class TeamMaker:
    def __init__(self, loc, t=None, d=None, pr=True):
        self.name = loc + '/docs/txt-files/team_maker_save.txt'
        if t is None:
            t = self.ask_t()
        if d is None:
            d = self.ask_l()

        self.d = d
        self.teams = []

        if t == '2 teams':
            self.two_teams()
            if pr:
                self.show()

        if t == '4 teams':
            self.four_teams()
            if pr:
                self.show()

        if t == 'partners':
            self.partners()
            if pr:
                self.show()

    def ask_t(self):
        t = input('What type would you like?\n')
        return t

    def ask_l(self):
        d = []
        load = input('would you like to load the list? (y/n)')
        if load == 'n':
            print("Enter a list of the people's names if nothing is entered, the list will stop")
            while True:
                l_add = input('')
                if l_add == '':
                    break
                d.append(l_add)
            save = input('would you like to save this list? (y/n)')
            if save == 'y':
                self.save_list(d)

        elif load == 'y':
            d = self.load()

        else:
            print('{} is an word/char that this code does not allow'.format(load))
            exit(404)

        return d

    def two_teams(self):
        team_1 = []
        team_2 = []
        while len(self.d) > 1:
            person1 = randint(0, len(self.d) - 1)
            team_1.append(self.d[person1])
            del self.d[person1]
            person2 = randint(0, len(self.d) - 1)
            team_2.append(self.d[person2])
            del self.d[person2]

        if len(self.d) == 1:
            print('you have and uneven amount, adding {} to team 1'.format(self.d[0]))
            team_1.append(self.d[0])

        self.teams.append(team_1)
        self.teams.append(team_2)

    def four_teams(self):
        team_1 = []
        team_2 = []
        team_3 = []
        team_4 = []
        while len(self.d) > 3:
            person1 = randint(0, len(self.d) - 1)
            team_1.append(self.d[person1])
            del self.d[person1]

            person2 = randint(0, len(self.d) - 1)
            team_2.append(self.d[person2])
            del self.d[person2]

            person3 = randint(0, len(self.d) - 1)
            team_3.append(self.d[person3])
            del self.d[person3]

            person4 = randint(0, len(self.d) - 1)
            team_4.append(self.d[person4])
            del self.d[person4]

        if len(self.d) == 1:
            team_1.append(self.d[0])

        elif len(self.d) == 2:
            team_1.append(self.d[0])
            team_2.append(self.d[1])

        elif len(self.d) == 3:
            team_1.append(self.d[0])
            team_2.append(self.d[1])
            team_3.append(self.d[2])

        self.teams.append(team_1)
        self.teams.append(team_2)
        self.teams.append(team_3)
        self.teams.append(team_4)

    def partners(self):
        while len(self.d) > 2:
            person1 = randint(0, len(self.d) - 1)
            person_1_name = self.d[person1]
            del self.d[person1]

            person2 = randint(0, len(self.d) - 1)
            person_2_name = self.d[person2]
            del self.d[person2]

            self.teams.append([person_1_name, person_2_name])

        if len(self.d) == 1:
            print('You have an uneven amount of people')
            print('I am making a group of three')
            self.teams[0].append(self.d[0])

    def load(self):
        try:
            with open(self.name) as json_file:
                j = json.load(json_file)
        except FileNotFoundError:
            print('This file does not exist')
            exit(5)
        return j

    def save_list(self, d):
        with open(self.name, 'w') as outfile:
            json.dump(d, outfile)

    def show(self):
        team_num = 1
        for item_large in self.teams:
            print('Team {}'.format(team_num))
            for item in item_large:
                print(item)
            print('\n')
            team_num += 1


if __name__ == "__main__":
    teams = TeamMaker(pyWrkspLoc)
