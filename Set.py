# Set is a collection of unique elements,defined by curly braces

sett = {1, 2, 3}

# NOTE: Set is an unordered collection,so there is no proper sequence
# So when we print,same order wont be preserved
# This is because sets internally uses HASHING to store as elements are already unique
print(sett)

# print(set[0]) Cannot be accessed by indexing..coz there is no order in the set,therefore no indexing

# If we give duplicate elements,they are ignored
s = {1, 2, 1, 3, 2, 4, 5, 4}
print(s)
# NOTE if we want to define an empty set,we need to use normal braces,coz eg: s = {} becomes an empty dictionary
# and also empty tuple however has an , in it

settt = {}
print(type(settt))  # Type dictionary

settt = ()
print(type(settt))  # Type Tuple

properset = set()
print(type(properset))

# Membership operators in and not in are applicable in set

family = {'eshwar', 'durga', 'lokesh', 'eswari'}

print('eshwar' in family)
print('lucy' in family)

# Sets are Mutable we can add/remove elements using following methods

methods = {1, 2, 3, 4, 5}
methods.add(6)
print(methods)
methods.remove(1)  # If not found,returns a KeyError
print(methods)
print(methods.pop())  # we cant predict which element can be popped

s.clear()
print(s)

methods.discard(2)  # Only difference from remove is that it wont raise an error if the element is not found
print(methods)

# Basic mathematical set operations can be performed on sets

d1 = {1, 2, 3}
d2 = {4, 5, 6}
print(d1 | d2)   # Union of 2 sets
print(d1 & d2)   # Intersection of two sets
print(d1 - d2)   # Difference between two sets
print(d1 ^ d2)   # Exclusive OR
print(d1.isdisjoint(d2))   # Checks if caller is disjoint with callee
print(d1.issubset(d2))      # Checks if callee is a subset to caller

print(d1.issuperset(d2))   # Checks if one is superset to other

# Unpacking can be done more elegantly

unpack = set("Eshwar")
print(unpack)

# Set Comprehension

comprehendedset = {c for c in 'Eshwar Prasad'}
print(comprehendedset)
