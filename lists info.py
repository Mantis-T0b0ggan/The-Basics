# Lists, Tuples and Sets
# Tuples - sequencial data
# Lists - sequencial data
# Sets - unordered collections with values with no duplicates

# lists [] - couses = [] -- sets a variable courses as a list
# to add to the list put each value you want seperated by a comma
# courses = ['History', 'Math', 'Physics', 'CompSci']
# indexing = print(courses[0]) -- prints History in this case
# if trying to get a value at the end of a list use the index -1
# if you want to print History and Math from the list --
# print(courses[:2]) -- indexing lists stops 1 before the given stop index

# addings item to list
# append() -- adds the given value to the end of the list
# insert() -- takes two arguments - first-index LOCATION you want to inset the value :: second- the value
# courses.insert(0, 'Art')

# extend()
# use when we have multiple values that we want to add to our list EXAMPLE--
# have another list called courses_2 list -- courses.extend(courses_2)
# Adds the values of courses_2 to the end of courses list

# Removing values
# remove() -- courses.remove('Math')
# pop() -- courses.pop() -- pop() returns the value popped off the list. 
# could use this to store the popped value into another variable

# reversing a list
# courses.reverse()
# 