import json
class notes:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def print_notes():
        try:
            with open('data3.txt') as json_file:
                self.notes += json.load(json_file)
        except:
            pass
        if self.notes != []:
            for item in self.notes:
                print('{}'.format(item))
        if self.notes == []:
            print("you don't have any notes saved!")

    def save_notes():
        with open('data3.txt', 'w') as outfile:
            json.dump(self.notes, outfile)

n = notes()
n.print_notes()
add = input('would you like to add any note? (y/n)')
if add == 'y':
    info = input('what is your note?')
    n.add_note(info)
    n.save_notes()
    print('your note, "{}" has been added to your saved notes!'.format(note))