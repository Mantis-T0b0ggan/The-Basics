message = 'Hello World'

# variables are usually lower case and as descriptive as possible
# EXAMPLE my_message = 'Hello World' ----- my_message being the variable

# if you have a string with a ' in it - E.G 'Bobby's World'
# this would cause an error as the string ends at y in Bobby
# To get around this - 'Bobby\'s World' -- \ is escape
# Python would now know the ' after y is not closing out the string

# Another way to do this is by using double quotes
# If you know your string has a single ' in it you can use double quote to work around

# If you want to find characters in a string use len(). Ex: print(len(message))

# To access characters individually we use Indexing []
# print(message[0]) -- this would print the first character in the string. 0 based 

# Slicing ::
# to access range of characters [:] indexing
# print(message[0:5]) - This would print Hello 
# index 0 = H, index 1 = e, index 2 = l, etc...
# If you are starting from index 0 you can leave the start index blank [:5]

# Method is a function that belongs to an object - Pretty much the same as a function

# To lower or uppercase a string you use the .lower() or .upper() -- print(message.lower())
# To count the number of char in a string use .count() -- print(message.count())
# To count the number of chars in a single word of a string -- print(message.count())
# To find the INDEX of where certain characters can be found use .find() -- print(message.find())
# Example -- print(message.find('World')) would print 6 - Thats because starts at the 6th index of our message variable
# if using .find() and it receives info that doesnt exist -- it will default to print -1

# To replace characters in a string --
# replace() method -- takes two arguments. First argument-what we want to replace :: second argument-what to replace the first argument with
# Example message.replace('World', 'Universe') 
# When you do this you need a new variable to hold the new value of the string to return -- new_message = message.replace('World', 'Universe')
# can use the same variable if you're making adjustments like this - rather than new_message we would keep it as message variable to store the new string

# Concat -- bring strings together -- use +
# Example - print(message + ' ' + 'Welcome!')
# Formatted strings - used ALOT -- message = '{}, {}. Welcome!'.format(greeting, name) - This is if we had two variables greeing and name
# fstrings - python 3.6 and higher -
# message = f'{greeting}, {name}. Welcome!' Does the same thing as using .format instead you put f in front of the string to format
# Can write code in the place holder -- f'{greeting.lower()}, {name.upper()}. Welcome!'

# If you need to see everything avaialbe use the dir function -- print(dir(message) -- shows you all functions you can do with that passed argument
# in this case the argument is a string variable called message

# Help function -- need to run it on a class not a variable
# Example -- print(help(str)) shows everything avaialbe to do on a string -- also print(help(str.lower())) - shows what this function does exactly 
# Very helpful if you forget what a method or somethig does