# Tuples are immutable!

tup = ()  # empty tuple

# tup[0] = 1 wont work coz we cant assign to tuple as it is immutable

tup = (1, 2, 3)

#  though we cant change tuples, its possible to give mutable objects such as lists to tuple

list1 = [1, 2, 3]
list2 = ['esh', 'war']

demotup = (list1, list2)

print(demotup)

# print(list1 in tuple) in and not in cannot be used in tuple

# Functions generally return multiple values using a tuple

single = (10,)  # You always give comma for single valued tuples,otherwise they wont behave a tuples
print(single)

# Tuples can be accessed by indexing
print(list1[0])  # So slicing can also be used

# Tuples can also be accessed via unpacking

unpackingdemo = ('hello', 'hi', 'welcome')
n, t, y = unpackingdemo
print(n, t, y)   # Note that no of elements to be unpacked in tuple should be same as the variables provied to pack them

yetAnotherUnpackingDemo = (1, 2, 3, 4)
a, b, c, d = yetAnotherUnpackingDemo

print(a)

# only two methods in tuple

print(tup.count(1))  # To count the number of occurences of provided element

print(tup.index(1))  # To check whats present in the given index value
