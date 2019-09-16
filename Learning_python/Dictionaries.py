my_stuff = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_stuff['key2'])

my_stuff = {'key1':'value1', 123:'value2', 'key3':{'124':[1,2,5,'he']}}
print(my_stuff['key3'])

print(my_stuff['key3']['124'][3].upper())

# How to reassign dictionaries
my_lunch = {'lunch':'pizza', 'bfast':'eggs'}
my_lunch['lunch'] = 'burger'
my_lunch['dinner'] = 'pasta'

print(my_lunch)
