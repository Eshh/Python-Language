# List is Mutable
# it is a collection of values which can be accessed by index

demo = [1, 2, 3]  # List definition

heterogeneous_list = ['abc', 1, 'a']

print(type(demo))

#  List is iterable

for n in demo:
    print(n)

# accessing by index
print(heterogeneous_list[0])

# can be sliced

print(demo[0:])

# Basic methods in List class

demo.append(4)  # adds element at the end
print(demo[0:])

demo.extend([5, 6])  # adds a new iterable at the end of the list
print(demo[:])

demo.insert(6, 'inserted element')   # adds element at given index
print(demo[:])

demo[0], demo[6] = demo[6], demo[0]  # swapping two elements like regular swap, so cool na
print(demo[:])

demo.remove(1)  # removes given element from the list,if not found,returns error,if repeated,1st element is removed
print(demo[:])

print(demo.pop())  # removes and returns element at given index,if no index is give,removes last element and returns it
print(demo[:])

heterogeneous_list.clear()  # deletes entire list
print(heterogeneous_list[:])

# we can add new lists to a list
listoflists = [[1, 2], ['hi']]
print(listoflists[:])
# we can access like double dimensional array
print(listoflists[1][0])

print(demo.index(2))  # returns the index of given element,if not found raises an error
# we can optionally provide start and end indexes to look for

print(demo.index(2, 0))  # implies starts checking for 2 from 3rd index

print(demo.count(1))      # returns no of times given element appears in the list,if not found raises Valueerror

# to remove one or more items- del method
del demo[0]

demo.insert(0, 1)

print(demo[:])

sortdemo = [2, 4, 1, 7, 3]
s = sorted(sortdemo)
print(s[:])    # in place sorting i.e doesnt change original,sorting can be customized using key overriding
print(sortdemo[:])

print(listoflists.reverse())  # reverses in place

c = demo.copy()  # makes a copy of the list
print(c[:])

# List Comparisons

print(demo == c)  # order should be same too
print(demo > c)
print(sum(demo))  # sum of elements in list,only works for homogeneous lists with integers

eg = ['esh']
eg2 = ['war']
print(eg + eg2)  # list concatenation,gives another list

print(len(demo))  # length of a list

# List Comprehension

squares = [n * n for n in range(1, 4)]
print(squares[:])
