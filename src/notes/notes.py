import json

notes = []

def add_note(note):
    global passwords
    notes.append(note)

def print_notes():
    global notes
    try:
        with open('data3.txt') as json_file:
            notes += json.load(json_file)
    except:
        pass
    if notes != []:
        for item in notes:
            print('{}'.format(item))
    if notes == []:
        print("you don't have any notes saved!")

def save_notes():
    with open('data3.txt', 'w') as outfile:
        json.dump(notes, outfile)

print_notes()
add = input('would you like to add any note? (y/n)')
if add == 'y':
    note = input('what is your note?')
    add_note(note)
    save_notes()
    print('your note, "{}" has been added to your saved notes!'.format(note))