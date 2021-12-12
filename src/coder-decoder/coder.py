class coder_decoder:
    def __init__(self, message=None, key=None, code_decode=None, print_info=True):
        self.abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '.', ',', '']
        if print_info:
            if message == None:
                message = input('What is your message?\n')
            if key == None:
                key = int(input('what is the key? (from 1 to {})\n'.format(len(self.abcs))))
            if code_decode == None:
                code_decode = input('Would you like to code or decode (code/decode)\n')
            
        if key > len(self.abcs):
            key = len(self.abcs) - 1
                    
        self.message = message.upper()
        self.key = key
        self.code_decode = code_decode
        self.finished = ''
        self.print_info = print_info
        if self.code_decode == 'code':
            self.code()
        elif self.code_decode == 'decode':
            self.decode()
        else:
            print('Incorrect code/decode')
            print('exiting code')
            return 'Error: incorrect code/decode'
    def code(self):
        message = list(self.message)
        new_message = []
        new_message_str = ''
        
        for i in range(len(message)):
            for l in range(len(self.abcs)):
                if self.abcs[l] == message[i]:
                    try:
                        new_message.append(self.abcs[l + self.key])
                    except:
                        pass
        for item in new_message:
            new_message_str += item
        
        if self.print_info:
            print('your coded message is {}'.format(new_message_str))
            print('give your friend this info:')
            print('message: {}\ncode: {}'.format(new_message_str, self.key))
        return new_message_str
        
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
        
        if self.print_info:
            print('your decoded message is {}'.format(new_message_str))
        return new_message_str

code = coder_decoder()
