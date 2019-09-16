# STRINGS

# BASICS
# 'hello', "hello", " I'm Eke "

# INDEXING
# This is basically grabbing sth from string sequence

mystring = 'ABCDEFG'
print(mystring[-1])

# SLICING
# slicing is broken into; the beginning, end and the step-size.
mystring = 'ABCDEFG'

print(mystring[2:5])
print(mystring[::2])
print(mystring[:2:])
print(mystring[2::])

# NB: Strings are immutable. This means you cant assign a value to STRINGS
# for EG: mystring[0] = 'X'
eze = 'Hello world, where are you guys at?'
# BASIC METHODS
# Upper
print(mystring.upper())
print(mystring.lower())
print(mystring.capitalize())
print(eze.split())
print(eze.split('w'))

# PRINT FORMATING
d = "Insert another string here: {}".format("Insomnia it is?")
print(d)

f = "Item one: {y}, Item two: {x}".format(y='one', x='two')
print(f)
