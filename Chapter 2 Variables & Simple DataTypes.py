

# ############### VARIABLES AND SIMPLE DATA TYPES - Chapter 2 ************** *
# Every variable holds a value which is then associated with that variable

# NAMING VARIABLES should be short, descriptive
# you can use underscores instead of spaces
# Do not use python keywords
# a .py file must start with a letter, usually lowercase

puppy = "Honey is Sleeping"
print(puppy)
#this prints Honey is Sleeping


# CHANGING THE VARIABLE
# You can change the value of a variable at anytime. Python keeps track of the current value.
# Traceback - A record of where the interperter ran into trouble.

brah = "Brie is Cold!"
print(brah)

brah = "Sloppy way to say 'bro'"
print(brah)

message = "Hello Python World!!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course Reader!"
print(message)

########### STRINGS ####################
# Strings - a data TYPE
# A series of characters. Anything inside quotes.
# you can use single or double quotes
# which means you can use apostrophes inside of strings.


# Change the case of words of the string with methods
name = "ada lovelace"
print(name.title())

# the method TITLE() is after the variable
# METHOD is an action that Python can preform on a piece of data.
# Every Method is followed by () b/c methods often need additional information

# Change to uppercase
name = "ada lovelace"
print(name.upper())

# Change name to lowercase
name = "Ada Lovelace"
print(name.lower())

# Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# use + to combine strings

# print a new sentence with the given variables
print("Hello, " + full_name.title() + "!")

#create a message and store it in a variable
message = "Hello, " + full_name.upper() + "!"
print(message)


# ############ ADDING WHITESPACE TO STRINGS WITH TABS OR NEW LINES ############### #
# Whitespace - any non-printing character like spaces, tabs or end-of-line-symbols

# To add a TAB (4 spaces) to your text, use the character combo \t

print("Python")
# Python

print("\tPython")
#     Python

# To add a NEW LINE in a string, use the character combo \n

print("Languages: \nPython\nC\nJavaScript")
# Languages:
# Python
# C
# JavaScript

# Combine New Lines and Tabs
# The string "\n\t" tells Python to move to a new line and start the new line with a tab

# create a one line string to make 4 lines of output
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#     Python
#     C
#     JavaScript


# ############ STRIPPING WHITESPACE ############## #
# Extra whitespace can become confusing or cause unwanted user input errors

# To ensure that there is no whitespace on the right of a string
# use the rstrip() method

favorite_language = ' python '
print(favorite_language)

print(favorite_language.rstrip())

# this removes the extra whitespace temporarily
# To remove it permanently store the stripped value back into the variable

favorite_language = favorite_language.rstrip()
print(favorite_language)


# Remove the White space from the LEFT side use the lstrip() method
# Or strip from BOTH sides using strip()

print(favorite_language.lstrip())
print(favorite_language.strip())

favorite_language = favorite_language.strip()
print(favorite_language)


# ############ NUMBERS ############ #
# Python treats numbers in several different ways

# #### INTEGERS #### #
# Add (+), subtract(-), multiply(*), divide(/)

print(2 + 3)
# 5
print(3 - 2)
# 1
print(2 * 3)
# 6
print(3 / 2)
# 1


# ###### EXPONENTS ** ########## #

print(3 ** 2)
# 9
print(3 ** 3)
# 27
print(10 ** 6)
# 1000000

# Python supports the order of operations

print(2 + 3 * 4)
# 14
print((2 + 3) * 4)
# 20



# ############## FLOATS ############ #
# Python calls any number with a decimal point a FLOAT

print(0.1 + 0.1)
# 0.2
print(0.2 + 0.2)
# 0.4
print(2 * 0.1)
# 0.2
print(2 * 0.2)
# 0.4

# To Use an integer as a string of characters
# by wrapping the variable in a str() function

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
# Happy 23rd Birthday! 


