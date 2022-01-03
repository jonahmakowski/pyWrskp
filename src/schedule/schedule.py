import json


class Schedule:
    def __init__(self):
        info = input('What would you like to do? \noptions: print, create, or empty (p/c/e)')
        if info == 'c':
            self.create()
        elif info == 'p':
            self.show()
        elif info == 'e':
            self.remove()
    
    def create(self):
        start_time = input('What is the start time for this event?\nplease use 24hr clock')
        end_time = input('What is the end time for this event?\nplease use 24hr clock')
        name = input('What is the name of this event?')
        all_events = self.read()
        if all_events is None:
            all_events = []
        all_events.append({'start time': start_time, 'end time': end_time, 'name': name})
        with open('data5.txt', 'w') as outfile:
            json.dump(all_events, outfile)
    
    def read(self):
        try:
            with open('data5.txt') as json_file:
                info = json.load(json_file)
        except:
            info = None
        
        return info
    
    def show(self):
        events = self.read()
        if events is None or events == []:
            print('you have no events saved')
        else:
            print('Name:\t\tstart:\t\tend:')
            for item in events:
                print('{}\t\t{}\t\t{}'.format(item['name'], item['start time'], item['end time']))

    def remove(self):
        with open('data5.txt', 'w') as outfile:
            json.dump([], outfile)


s = Schedule()
