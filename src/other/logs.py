import os
import json
import datetime
from dateutil import parser

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
        now = str(datetime.datetime.now())
        self.log.append({'time': now, 'info': log_info})
        self.save()
        print('your message, {} and the time and date, {}, have been saved!'.format(log_info, now))
    
    def read(self):
        self.load()
        print('Date\tTime\tInfo')
        for item in self.log:
            print('{}\t{}\t{}'.format(item['time'], item['info']))


log = Log(pyWrksp)
