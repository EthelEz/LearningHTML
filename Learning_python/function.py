# def my_func(param1='default'):
#     """
#     This is the DOCSTRING
#     """
#     print('My first python function! {}'.format(param1))
#
# my_func()
#
# def hello():
#     """
#     function that prints hello.
#     """
#     print("Hello")
#
# hello()
#
# def addNum(num1, num2):
#     return num1 + num2
#
# result = addNum(2, 3)
# result1 = addNum("2", "3")
# print(result)
# print(result1)
#
# def addNumb(n1, n2):
#     if type(n1) == type(n2) == type(10):
#         return n1 + n2
#     else:
#         return 'We are sorry, we work with integers'
# # print(addNum(2, 5))
# re = addNumb('hel', 'jh')
# print(re)


# Lambda Expression explained.
int = ([1,1,2,3,1])
int =([1,1,2,4,1])
int = ([1,1,2,1,2,3])

def array_check(n, m, o):
    for num in int:
        if (n) == 1 and (m) == 2 and (o) == 3:
            return "Number is: {x}".format(x=True)
    return 'False is: {y}'.format(y=False)

print(array_check(1,2,3))

# This code is written as thus by the trainer:
def array_Check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and num[i+2]==3:
            return True
    return False

# Given a string, return a new string made of every other character starting
# with the first, eg
# 1) "Hello" yields "Hlo"
# 2) Hi yields 'H'
# 3) Heeololeo yields 'Hello'

def string_bits(str):
    result = " "
    for i in range(len(str)):
        if i%2 == 0:
            result = result + str[i]
    return result

print(string_bits('Heeololeo'))

# Problem 3: Given two strings, return True if either of the strings appears at the every
# end of the other string, ignoring case sensitivities.
# EG: end_other('Hiabc', 'abc') -> True
#     end_other('ABC', 'HiaBc') -> True
#     end_other('abc', 'ABXabd') -> False

def end_other(a, b):

    a = a.lower()
    b = b.lower()
    # return (b.endswith(a) or a.endswith(b)) #This is the most pythonic way of coding this.
    return a[-(len(b)):] == b or a == b[-len(a):]

print(end_other('Hiabc', 'abd'))

def double_char(mystring):
    result = " "
    for char in mystring:
        result += char*2  #add to the string character * 3
    return result

print(double_char('The'))

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)  #Here fix_teen is a helper function to avoid repeated code
                                                    #or the dry code principle, which says, don't repeat urself.
def fix_teen(n):
    if n [13, 14, 17, 18, 19]:
        return 0
    return n


# Return the number of even integers in a given array.
def count_even(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

print(count_even([2,2,4,3,4]))
