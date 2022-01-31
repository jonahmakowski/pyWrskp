class AnimalChoser:
    def __init__(self):
        self.options = [{'name': 'bulldog', 'info': ['fur', 'pet', 'dog', 'short snout']},
                        {'name': 'human', 'info': ['hair', 'two legs', 'short snout']}]
        self.atturbites = [{'name': 'fur', 'y/n': ''},
                           {'name': 'pet', 'y/n': ''},
                           {'name': 'dog', 'y/n': ''},
                           {'name': 'short snout', 'y/n': ''},
                           {'name': 'hair', 'y/n': ''},
                           {'name': 'two legs', 'y/n': ''}]
        self.correct_atturbites = []
        print('The current options for this game are:')
        for item in self.options:
            print(item['name'])
        self.guess()

    def guess(self):
        for item in self.atturbites:
            yes_or_no = input('is this animal/does it have {} (y/n)?'.format(item['name']))
            item['y/n'] = yes_or_no

        for item in self.atturbites:
            if item['y/n'] == 'y':
                self.correct_atturbites.append(item['name'])

        choosen = False

        for item in self.options:
            item['info'] = sorted(item['info'])

        self.correct_atturbites = sorted(self.correct_atturbites)

        for item in self.options:
            if item['info'] == self.correct_atturbites:
                print('your animal is {}'.format(item['name']))
                choosen = True
                break

        if not choosen:
            print("This program can figure out what you choose, make sure it is on this list:")
            for item in self.options:
                print(item['name'])

            print('debug info:')
            print('self.correct_atturbites:')
            print(self.correct_atturbites)
            print('self.options:')
            print(self.options)


game = AnimalChoser()
