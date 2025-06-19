import json


class Notes:
    def __init__(self, name="data3.jonahtext"):
        self.notes = []
        self.name = name

    def add_note(self, note):
        self.notes.append(note)

    def print_notes(self):
        try:
            with open(self.name) as json_file:
                self.notes += json.load(json_file)
        except:
            pass
        if self.notes != []:
            for item in self.notes:
                print("{}".format(item))
        if self.notes == []:
            print("you don't have any notes saved!")

    def save_notes(self):
        with open(self.name, "w") as outfile:
            json.dump(self.notes, outfile)

    def clear(self):
        self.notes = []
        self.save_notes()


if __name__ == "__main__":
    n = Notes()
    n.print_notes()
    add = input("would you like to add any note? (y/n/c)")
    if add == "y":
        info = input("what is your note?")
        n.add_note(info)
        n.save_notes()
        print('your note, "{}" has been added to your saved notes!'.format(info))
    elif add == "c":
        n.clear()
