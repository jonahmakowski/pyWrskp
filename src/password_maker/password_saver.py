import json
import os

try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')
passwords = []


def add_password(password, website):
    global passwords
    passwords.append({'website':website, 'password':password})


def print_passwords(pyWrskp):
    global passwords
    try:
        with open(pyWrskp + '/docs/txt-files/passwords.txt') as json_file:
            passwords += json.load(json_file)
    except:
        pass

    if passwords != []:
        for item in passwords:
            print('{}:   {}'.format(item['website'], item['password']))

    if passwords == []:
        print("you don't have any passwords saved!")


def save_passwords(pyWrskp):
    with open(pyWrskp + '/docs/txt-files/passwords.txt', 'w') as outfile:
        json.dump(passwords, outfile)


print_passwords(pyWrkspLoc)
add = input('would you like to add any passwords? (y/n)')
if add == 'y':
    password = input('what is your password?')
    website = input('what webiste is this password being used by?')
    add_password(password, website)
    save_passwords(pyWrkspLoc)
    print('your password, {} has been added to your saved passwords!'.format(password))
