import os
import json
import datetime


class Log:
    def __init__(self, save_loc=None):
        self.log = []
        save_loc = os.getcwd() + '/save_loc.txt'
        self.save_locs = self.load(save_loc)
        self.loc = os.environ["HOME"]
        new_or_old = input('Do you need a new txt file?')
        if new_or_old == 'new':
            self.name = self.loc + input('Where do you want the logs to be stored?')
            self.save_locs.append(self.name)
        else:
            print('your options are:')
            if len(self.save_locs) > 0:
                for i in range(len(self.save_locs)):
                    print('Option number: {}, loc: {}'.format(i, self.save_locs[i]))
            else:
                print('There are no options')
                print('Ending program')
                exit(404)
            save_num = int(input('What is the save number?'))
            self.name = self.save_locs[save_num]
            try:
                self.log = self.load(self.name)
                print('loading info')
            except FileNotFoundError:
                print('Creating new txt file')
        self.save(save_loc, self.save_locs)
        self.mainloop()
    
    def load(self, loc):
        with open(loc) as json_file:
            item = json.load(json_file)
        return item
    
    def save(self, loc, item):
        with open(loc, 'w') as outfile:
            json.dump(item, outfile)
    
    def mainloop(self):
        while True:
            do = input('What do you want to do?')
            if do == 'add':
                self.add()
                break
            elif do == 'read':
                self.read()
                break
            elif do == 'clear':
                self.clear()
                break
            else:
                print('This is not an option')
                print('Try again')
    
    def add(self):
        log_info = input('What do you want to add to the log?\n')
        time = datetime.datetime.now()
        time = time.strftime("%d/%m/%y %H:%M")
        time = datetime.datetime.strptime(time, "%d/%m/%y %H:%M")
        time = "{:d}:{:02d}".format(time.hour, time.minute)
        date = {'day': datetime.datetime.now().day,
                'month': datetime.datetime.now().month,
                'year': datetime.datetime.now().year}
        current_log = {'time': time, 'date': date, 'info': log_info}
        self.log.append(current_log)
        self.save(self.name, self.log)
        post_date = '{}-{}-{}'.format(current_log['date']['month'],
                                      current_log['date']['day'],
                                      current_log['date']['year'])
        print('your message, {} and the time and date, {}, {}, have been saved!'.format(log_info, post_date, time))
    
    def read(self):
        self.log = self.load(self.name)
        print('Date\ttime\tInfo')
        unreadable = 0
        for item in self.log:
            try:
                post_date = '{}-{}-{}'.format(item['date']['month'], item['date']['day'], item['date']['year'])
                print('{}\t{}\t{}'.format(post_date, item['time'], item['info']))
            except KeyError:
                unreadable += 1
                # print('No information can be taken from this log entry, this might be from an older version')
        if unreadable > 0:
            print('\n\n')
            print('There are {} log entries that were either from an older version, or were entered directly into '
                  'the txt file'.format(unreadable))
    
    def clear(self):
        self.log = []
        self.save(self.name, self.log)


log = Log()
