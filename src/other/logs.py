import os
import json
import datetime

try:
    pyWrksp = os.environ["PYWRKSP"]

except KeyError:
    pyWrksp = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                         '\nPlease enter the pwd for the pyWrskp repo not including the '
                                         '"home" section')


class Log:
    def __init__(self, pywrskp):
        self.log = []
        self.loc = pywrskp
        self.name = self.loc + '/docs/txt-files/logs.txt'
        self.load()
        self.mainloop()
    
    def load(self):
        with open(self.name) as json_file:
            self.log = json.load(json_file)
    
    def save(self):
        with open(self.name, 'w') as outfile:
            json.dump(self.log, outfile)
    
    def mainloop(self):
        while True:
            do = input('What do you want to do?')
            if do == 'add':
                self.add()
                break
            elif do == 'read':
                self.read()
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
        self.save()
        post_date = '{}-{}-{}'.format(current_log['date']['month'],
                                      current_log['date']['day'],
                                      current_log['date']['year'])
        print('your message, {} and the time and date, {}, {}, have been saved!'.format(log_info, post_date, time))
    
    def read(self):
        self.load()
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


log = Log(pyWrksp)
