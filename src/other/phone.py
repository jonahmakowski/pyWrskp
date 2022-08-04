import time
import datetime
import json

class Phone:
    def __init__(self):
        self.log = {}
        self.fetch_log()
        self.password = self.log['password']
        self.username = self.log['username']
        self.name = self.log['name']
        self.login()
        self.do()
    
    def login(self):
        passtest = input('What is your phone password?')
        print('Checking passwords,')
        time.sleep(1)
        print('Looking for hacks,')
        time.sleep(1)
        if passtest == self.password:
            return
        else:
            print('That password is incorrect')
            time.sleep(10)
            exit()
    
    def do(self):
         print('Welcome Back, {} ({})'.format(self.username, self.name))
         now = datetime.datetime.now()
         self.log['loginDate'].append(str(now))
         self.push_log()
         option = input('What would you like to do?')
         if option == 'send uncoded message' or option == 'sum':
             self.send_uncoded_message()
         
    def fetch_log(self):
        with open('../../docs/txt-files/phone_log.txt') as json_file:
                self.log = json.load(json_file)
    
    def push_log(self):
        with open('../../docs/txt-files/phone_log.txt', 'w') as outfile:
            json.dump(self.log, outfile)
    
    def send_uncoded_message(self):
        now = str(datetime.datetime.now())
        message = input('What is your message?')
        location = input('What is the location or name?')
        try:
            with open(location, 'w') as outfile:
                json.dump(message, outfile)
            self.log['messages'].append({'Date': now, 'message': message, 'location_created_at': location})
            self.push_log()
        except:
            print('{} is not a valid location'.format('location'))

Jphone = Phone()