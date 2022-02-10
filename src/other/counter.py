count_type = input('What count type would you like to use?\n')
if count_type == 'with spaces':
    string = input('Paste what you want to count\n')
    string = list(string)

    print('Here is the length of your text:')
    print(len(string))
else:
    string = input('Paste what you want to count\n')
    string = list(string)
    
    for item in string:
        if item == ' ':
            del item
    
    print('Here is the length of your text:')
    print(len(string))