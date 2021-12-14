from coder import coderDecoder

code = coderDecoder()

message = input('What is your message?\n')
while True:
    key = int(input('what is the key? (from 1 to {})\n'.format(len(info.abcs))))
    if key >= 1 and key < len(info.abcs):
        break
    else:
        print('inccorrect number')

code.add_vars(message, key)

code_decode = input('Would you like to code or decode?')
if code_decode == 'code':
    code.code()
elif code_decode == 'decode':
    code.decode()