class AnimalChoser:
    def __init__(self):
        self.options = [{'name': 'bulldog', 'type': 'dog', 'info': ['fur', 'pet']}]
        self.atturbites = [{'name': 'fur', 'y/n': ''}, {'name': 'pet', 'y/n': ''}]
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

        for item in self.options:
            if item['info'] == self.correct_atturbites:
                print('your animal is {}'.format(item['name']))
                break


game = AnimalChoser()
