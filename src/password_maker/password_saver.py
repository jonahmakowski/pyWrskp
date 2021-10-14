import json

passwords = []

def add_password(password, website):
    global passwords
    passwords.append({'website':website, 'password':password})

def print_passwords():
    global passwords
    try:
        with open('data2.txt') as json_file:
            passwords += json.load(json_file)
    except:
        pass
    if passwords != []:
        for item in passwords:
            print('{}:   {}'.format(item['website'], item['password']))
    if passwords == []:
        print("you don't have any passwords saved!")

def save_passwords():
    with open('data2.txt', 'w') as outfile:
        json.dump(passwords, outfile)

print_passwords()
add = input('would you like to add any passwords? (y/n)')
if add == 'y':
    password = input('what is your password?')
    website = input('what webiste is this password being used by?')
    add_password(password, website)
    save_passwords()
    print('your password, {} has been added to your saved passwords!'.format(password))
