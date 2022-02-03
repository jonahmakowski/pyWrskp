# This char "#" makes the rest of the line a comment and the computer ignores it

"""This is a other way to right comments
as this can be many lines"""

print()  # prints the item in the bracket

var1 = input()  # takes input from the question put in the bracket (this saves as a string)

var2 = int(input())
'''takes input from the question put in the bracket (this saves as a int), the int() part takes the
 input and turns it into an int, if it is a word, like "Hello", it will return an error, if it is a float like "0.5" it 
 will also return an error'''

var3 = float(input())
'''takes input from the question put in the bracket (this saves as a float), the float() part takes the input and turns
 it into a float, if it is a word, like "Hello", it will return an error, if it is a int like "1" it will make the int,
  "1" into "1.0"'''

var4 = str(1 + 2)  # this will add 1 + 2 and save it as a string, so this would look like "3" in string form

var5 = 0  # makes a var that is = to the integer "0"

var6 = 'Hello World'  # makes a var that is = to the string "Hello world"

var7 = 0.5  # makes a var that is = to the float "0.5"

var8 = [var1, var2, var3, var4, var5, var6, var7]  # This makes a var = to a list of all of the other vars

for i in range(3):  # means do 3 times "i" is a counter
    print('hi')

for item in var8:  # means for every item in var8 (a list), do this, item is the current item that is going through
    print(item)
