

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

