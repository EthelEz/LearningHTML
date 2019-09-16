# This is the last data structure we'd be discussing here
# Turples are immutable sequences. the act like a
# list but you cant index sth from a turple and try to change it.
#
# Sets are unordered collections of unique elements
# Booleans are True or False statements, which can also be represented with 0 or 1 syntaxes

# Booleans
True
False

# Turples  The diff btw this & list is that they're immutable.List & strings are not.
t = (1,2,3)
print(t[1])

# t[0] = 'new'  you'd get TypeError

# Sets. This only takes in unique elements. If I add 2 3 times, it'd only output 2 once
x = set()
x.add(1)
x.add(2)
x.add(0.2)
x.add(5)
print(x)

# Exercise
s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[4:])
print(s[::-1])


l = [3, 7, [1,4,'hello']]
print(l[2][2])

l[2][2] ='goodbye'
print(l)

d1 = {'simply_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}

print(d1['simply_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
z = set(mylist)
print(z)

m = "Hello my dog's name is {name} and it is {age} years old".format(name = "sammi",age = 4)
print(m)

n = "Hello my dog's name is {a} and it is {b} years old".format(b="sammi",a = 4)
print(n)
