class coder_decoder:
    def __init__(self, message=None, key=None, code_decode=None):
        self.abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
        if message == None:
            message = input('What is your message?\n')
        if key == None:
            key = int(input('what is the key? (from 1 to 36)\n'))
        if code_decode == None:
            code_decode = input('Would you like to code or decode (code/decode)\n')
        
        if key > len(self.abcs):
            key = len(self.abcs) - 1
                    
        self.message = message.upper()
        self.key = key
        self.code_decode = code_decode
        self.finished = ''
        if self.code_decode == 'code':
            self.code()
        elif self.code_decode == 'decode':
            self.decode()
        else:
            print('imporoper code/decode')
            exit()
    def code(self):
        message = list(self.message)
        new_message = []
        new_message_str = ''
        
        for i in range(len(message)):
            for l in range(len(self.abcs)):
                if self.abcs[l] == message[i]:
                    new_message.append(self.abcs[l + self.key])
        
        for item in new_message:
            new_message_str += item
        
        print('your coded message is {}'.format(new_message_str))
        print('give your friend this info:')
        print('message: {}\ncode: {}'.format(new_message_str, self.key))
        
    def decode(self):
        message = list(self.message)
        new_message = []
        new_message_str = ''
        
        for i in range(len(message)):
            for l in range(len(self.abcs)):
                if self.abcs[l] == message[i]:
                    new_message.append(self.abcs[l - self.key])
        
        for item in new_message:
            new_message_str += item
        
        print('your decoded message is {}'.format(new_message_str))

code = coder_decoder()
