from random import randint

letter = input('Would you like letters? (ex. A, B, C)')
num = input('Would you like numbers? (ex. 1, 2, 3)')
sc = input('Would you like special chars? (ex. @, %, &)')
super_c = input('Would you like super special chars (ex. ←, ↑, →), \nsome websites may not allow this, if it does not work turn this off')
length = int(input('how long would you like your password to be?'))

chars = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
scs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', '`', '{', '}', '[', ']', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '|']
super_s_c = ['←', '↑', '→', '↓', '·', '•', '●', '–', '‽', '‖', '«', '»', '‘', '„', '✅', '❤️', '⌘', '', '⌥', '⌫', '∞', '™', '¼', '½', '¾', 'À', 'Á', 'Â', 'Ã',
             'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'æ', 'Ħ',
             'ĳ', 'Œ', 'œ', '☚', '☛', '★', '☆', '♠', '♣', '♥', '♦', '♪', '♫', '♀']

if letter == 'y':
    chars += letters
if num == 'y':
    chars += nums
if sc == 'y':
    chars += scs
if super_c == 'y':
    chars += super_s_c

password = ''

for i in range(length):
    loc = randint(0, len(chars) - 1)
    password += chars[loc]

print(password)
save = input('Would you like to save your password to data2.txt? (y/n)')

if save == 'y':
    website = input('what webiste will this password be used by?')
    from Password_saver import add_password, save_passwords
    add_password(password, website)
    save_passwords()
    print('your password, {} has been added to your saved passwords!'.format(password))