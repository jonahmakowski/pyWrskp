from random import randint

print('Main Homework:')
guessed = False
secret = randint(0, 100)
name = input('What is your name?\n')
while True:
    guesses = input('How many guesses would you like {}?\n'.format(name))
    if guesses.isdigit():
        guesses = int(guesses)
        break
    else:
        print('Wow {} you really are a student!'.format(name))
        print('That is obviously supposed to be a number, you should be ashamed of yourself.')

print('Welcome to guess my number {}! You have {} guesses! The number is betweeen 0, and 100'.format(name, guesses))

for i in range(1, guesses + 1):
    while True:
        guess = input('Guess #{}?\n'.format(i))
        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print('Wow {} you really are a student!'.format(name))
            print('That is obviously supposed to be a number, you should be ashamed of yourself.')
    if guess == secret:
        print('Good job! You won on guess number {}'.format(i))
        guessed = True
        break
    elif guess > secret:
        print('To high')
    elif guess < secret:
        print('To low')

if not guessed:
    print('You failed')
    print('The number was {} you STUDENT!'.format(secret))

'''
--------------------------------------------------------------------------------------------------------
Starting here is John's extra homework for me
Both methods I have created will print exactly this (assuming you set 10 lines):
          *
         * *
        * * *
       * * * *
      * * * * *
     * * * * * *
    * * * * * * *
   * * * * * * * *
  * * * * * * * * *
 * * * * * * * * * *
  * * * * * * * * *
   * * * * * * * *
    * * * * * * *
     * * * * * *
      * * * * *
       * * * *
        * * *
         * *
          *
--------------------------------------------------------------------------------------------------------
'''
input('Press enter to continue to additional homework')

for i in range(300):
    print()

while True:
    lines = input('How many lines would you like {}?\n'.format(name))
    if lines.isdigit():
        lines = int(lines)
        break
    else:
        print('Wow {} you really are a student!'.format(name))
        print('That is obviously supposed to be a number, you should be ashamed of yourself.')

print('Way One, Cheaty (no abs() used)')
diamond = ''
star = ' *'
space = ' '

for line in range(1, lines+1):
    diamond += space*(lines-line)
    diamond += star*line
    diamond += '\n'
for line in range(1, lines):
    diamond += space*line
    diamond += star*(lines - line)
    diamond += '\n'
print(diamond)  # THE ONLY PRINT

print('Way 2, with abs()')
input('Press enter to continue')

for i in range(-lines+1, lines):
    space_amount = abs(i)
    star_amount = lines-abs(i)
    print(space*space_amount+star*star_amount)  # THE ONLY PRINT
