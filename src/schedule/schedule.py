import os
import json


class Schedule:
    def __init__(self):
        try:
            self.pyWrskp = os.environ["PYWRKSP"]
        except KeyError:
            self.pyWrksp = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                                    '\nPlease enter the pwd for the pyWrskp repo not including the '
                                                    '"home" section')
        self.name = self.pyWrksp + '/docs/txt-files/data5.txt'
        info = input('What would you like to do? \noptions: print, create, or empty (p/c/e)')
        if info == 'c':
            self.create()
        elif info == 'p':
            self.show()
        elif info == 'e':
            self.empty()
    
    def create(self):
        start_time = input('What is the start time for this event?\nplease use 24hr clock')
        end_time = input('What is the end time for this event?\nplease use 24hr clock')
        name = input('What is the name of this event?')
        all_events = self.read()
        if all_events is None:
            all_events = []
        all_events.append({'start time': start_time, 'end time': end_time, 'name': name})
        with open(self.name, 'w') as outfile:
            json.dump(all_events, outfile)
    
    def read(self):
        try:
            with open(self.name) as json_file:
                info = json.load(json_file)
            info = sorted(info, key=lambda i: i['start time'], reverse=True)
        except:
            info = None
        
        return info
    
    def show(self):
        events = self.read()
        if events is None or events == []:
            print('you have no events saved')
        else:
            print('Name, start, end')
            for item in events:
                print('{}, {}, {}'.format(item['name'], item['start time'], item['end time']))

    def empty(self):
        with open(self.name, 'w') as outfile:
            json.dump([], outfile)


s = Schedule()
