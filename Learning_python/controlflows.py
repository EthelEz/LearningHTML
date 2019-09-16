# Greater than
1 > 2

# Less than
1 < 2

# Greater than or Equal to
1 >= 1

# Less than or Equal to
1 <= 1

# Equality
1 == 1
1 == "1"  #Returns False
'hi' == 'bye'  #Returns False

# Inequality
1 != 2

# Logical Operators in Python
# AND
(1 > 2) and (2 > 3)

# OR
(1 > 2) or (2 > 3)

# You can also have multiple logical operators

# NESTED IF statements
if 1 < 2:
    print('Yes')
    if 9 < 4:
        print('Lies')
if 9 < 2:
    print('Hey Yes!')
elif 3 == 3:
    print('elif ran!')
else:
    print('Ngwo')

d = {'Sam':2, "aladice": 4, "coach":8}
for item in d:
    print(item)
    print(d[item])
    print('Hey')

# ITEARTING through turple or what is commonly called turple unpacking
# mypairs = [()] This is a list of Turples
mypairs = [(1,2),(3,4),(5,6)]
for item in mypairs:
    print(item)

for (k, k2) in mypairs: #This is turple unpacking.
    print(k2)
    print(k)

# WHILE LOOP allows us to continue performing an action until the condition is True
i = 1

while i < 5:
    print('i is: {}'.format(i))
    i = i+1

# Another important function to know is RANGE function
# the function can generate an integer based on a starting pt and an ending pt.
# Note that range(5) is just a generator. the advantage is that it saves lists in memory.
for k in range(11):
    print(k)

# Practical EG of list comprehension
u = [1,2,3,4,5]
out = []
for num in u:
    out.append(num**2)
print(out)

# The above code can be rewritten in a single line, as in:
out_comprehend = [num**2 for num in u]  #This is list comprehension
print(out_comprehend)
