"""
I know I have an older team maker, but I thought I would use what I have learned so far to make a brand new one!

Here it is:
"""

from random import randint


class TeamMaker:
    def __init__(self, t=None, d=None, pr=True):
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

    def ask_t(self):
        t = input('What type would you like?\n')
        return t

    def ask_l(self):
        d = []
        print("Enter a list of the people's names if nothing is inputed, the list will stop")
        while True:
            l_add = input('')
            if l_add == '':
                break
            d.append(l_add)
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

    def show(self):
        team_num = 1
        for item_large in self.teams:
            print('Team {}'.format(team_num))
            for item in item_large:
                print(item)
            team_num += 1


teams = TeamMaker()
