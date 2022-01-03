import json

class Schedule:
    def __init__(self):
        self.pyWrskp = input('What is the dir of the pyWrskp repo\n')
        info = input('What would you like to do? \noptions: print, create(p/c)')
        if info == 'c':
            self.create()
        elif info == 'p':
            self.show()
    
    
    def create(self):
        start_time = input('What is the start time for this event?\nplease use 24hr clock')
        end_time = input('What is the end time for this event?\nplease use 24hr clock')
        name = input('What is the name of this event?')
        all_events = read()
        if all_events == None:
            all_events = []
        all_events.append({'start time':start_time, 'end time':end_time, 'name':name})
        with open(self.pyWrskp + '/src/docs/txt-files/data5.txt', 'w') as outfile:
            json.dump(all_events, outfile)
    
    
    def read(self):
        try:
            with open(self.pyWrskp + '/src/docs/txt-files/data5.txt') as json_file:
                info = json.load(json_file)
        except:
            info = None
        
        return info
    
    
    def show(self):
        events = self.read()
        if events == None or events == []:
            print('you have no events saved')
        else:
            print('Name:\t\tstart:\t\tend')
            for item in events:
                print('{}\t\t{}\t\t{}'.format(item['name'], item['start time'], item['end time']))