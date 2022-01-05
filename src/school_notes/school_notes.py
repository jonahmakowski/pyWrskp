import os
import datetime
import json

try:
    pyWrksp = os.environ["PYWRKSP"]

except KeyError:
    pyWrksp = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                         '\nPlease enter the pwd for the pyWrskp repo not including the '
                                         '"home" section')
    # pyWrskp = '/Users/jonahmakowski/Desktop/Github/pyWrskp'  #for debug, so you don't have to enter info


class SchoolNotes:
    def __init__(self, pywrskploc):
        self.pywrskploc = pywrskploc
        self.name = pywrskploc + '/docs/txt-files/school_notes.txt'

    def add(self):
        now = datetime.datetime.now()

        date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        print("current time is: " + current_time)
        print("today's date is: " + date)
        note = input('What is the note?\n')
        teacher = input("What is the teacher's name?\n")
        self.group = {'date': date, 'current_time': current_time, 'note': note, 'teacher': teacher}
        self.save()


    def save(self, custom=False):
        if not custom:
            self.read()
            self.all_events.append(self.group)
        with open(self.name, 'w') as outfile:
            json.dump(self.all_events, outfile)

    def read(self):
        with open(self.name) as json_file:
            self.all_events = json.load(json_file)

        return self.all_events

    def p(self):
        self.read()
        self.all_events = sorted(self.all_events, key=lambda i: i['date'], reverse=True)
        print('date, time, teacher, note')
        for item in self.all_events:
            print('{}, {}, {}, {}'.format(item['date'], item['current_time'], item['note'], item['teacher']))

    def empty(self):
        self.all_events = []
        self.save(custom=True)


s = SchoolNotes(pywrskploc=pyWrksp)
do = input('Would you like to add, print or empty?')
if do == 'add':
    s.add()
elif do == 'print':
    s.p()
elif do == 'empty':
    s.empty()
