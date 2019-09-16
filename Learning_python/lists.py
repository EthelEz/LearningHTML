# list
my_list = ['strangethings', 1, 5, 5, True, 'abcdf', [1, 2, 3, 'hi']]

# list_extend = ['d','s','l']
# my_list.extend(list_extend)
# print(my_list)
#
# print(len(my_list))
#
# print(my_list[0:4])
#
# print(my_list[0::5])

print(my_list[6][3])

# List are totally immutable, meaning you can add sth to the List

postDoc = [2, 5, 8, 'm', 66, 'lady']
postDoc.append('kosi')
print(postDoc)
pop_list = postDoc.pop(3)
print(pop_list)

postDoc.reverse()
print(postDoc)

# List comprehension
matrix = [[1,2,3,4], [4,5,6,7], [8,9,10,11]]
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)
sec_col = [row[1] for row in matrix]
print(sec_col)
third_col = [row[2] for row in matrix]
print(third_col)
fout_col = [row[3] for row in matrix]
print(fout_col)
