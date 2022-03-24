import sys
import json
import random
import os
sys.path.append('../coder-decoder')
from coder import CoderDecoder as CD


class Sender:
    def __init__(self):
        self.remote_coder = CD(print_info=False)
        self.remote_coder_2 = CD(print_info=False)
        self.remote_coder_3 = CD(print_info=False)

    def create_note(self):
        print('What would you like the password to be?')
        password = input('The person who decodes this needs to know it')
        message = input('What is the message that you would like to send?')
        key = random.randint(0, len(self.remote_coder.abcs) - 1)

        self.remote_coder.add_vars(message, key)
        message = self.remote_coder.code()

        self.remote_coder_2.add_vars(password, key)
        password = self.remote_coder_2.code()

        self.remote_coder_3.add_vars(str(key), 15)
        key = self.remote_coder_3.code()

        save_dic = {'asuydhausdhuashd': password, 'sdifhuegtsydftyas': message, 'asdyatsdftras': key}
        with open('message.txt', 'w') as outfile:
            json.dump(save_dic, outfile)

    def read_note(self):
        try:
            with open('message.txt') as json_file:
                dic = json.load(json_file)
        except FileNotFoundError:
            print('There is no file like this (make sure it is called message.txt)')
            exit(404)

        self.remote_coder_3.add_vars(dic['asdyatsdftras'], 15)
        key = int(self.remote_coder_3.decode())

        password = input('What is the password?')

        self.remote_coder_2.add_vars(dic['asuydhausdhuashd'], key)
        password_check = self.remote_coder_2.decode()

        if password != password_check:
            print('password incorrect deleting file')
            os.remove("message.txt")
            exit(500)

        self.remote_coder.add_vars(dic['sdifhuegtsydftyas'], key)
        message = self.remote_coder.decode()

        print('The message in this file is:')
        print(message)
        print('destroying file')
        os.remove('message.txt')


if __name__ == '__main__':
    sender = Sender()
    do = input('What do you wish to do?')
    if do == 'create':
        sender.create_note()
    elif do == 'read':
        sender.read_note()
