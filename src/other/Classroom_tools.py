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
        
        self.teacher = input("What is your teacher's name?")
        self.princaple = input("What is your princaple's name?")
        
        self.school_name = input('What is your school called?')

    def team_maker(self):
        from random import randint as r
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


Mr_Carter_class = Classroom()
Mr_Carter_class.team_maker()
