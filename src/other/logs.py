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
    def __init__(self, pyWrskp):
        self.log = []
        self.load()
        self.loc = pyWrskp
        self.name = self.loc + '/docs/txt-files/logs.txt'
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
    
    def read(self):
        self.load()
        print('Time\t\t\tInfo')
        for item in self.log:
            print('{}\t\t\t{}'.format(item['time'], item['info']))


log = Log(pyWrksp)