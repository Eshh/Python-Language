#  Built in functions for Strings
s = 'Eshwar'

print(ord(s[1]))  # Gives ASCII code-ord
print(chr(115))   # Takes ASCII code and returns character-chr

data = 'this String is for testing purpose'

print(data.capitalize())  # returns string with staring capital and rest all lower case

print(data.count('is'))   # returns no of a times a given sub string occurs

print(data.endswith('ose'))  # checks if string ends with given sub string

print(data.find('pyt'))    # checks and returns the sub string and returns -1 if not found
print(data.find('is', 5))   # from given index,it finds too

print(data.index('pur'))    # same like find but returns Valueerror when not found

print(data.isalnum())   # True if all are numbers
print(s.isalpha())      # True if all are aplhabets,even spaces are considered as non alphabets

#  Similarly isdigit,isdecimal,islower,isupper methods


print(data.lower())
print(data.upper())   # Returns a COPY of lower/upper strings as strings are immutable

s = data
print(s)
print(id(s) == id(data)) # Strings with same value point to same adress to save memory space

# Split Method
lst = data.split(" ")    # Takes a seperator and returns a List
for l in lst:
    print(l, end="  ")
print()
demo = 'It was all good 10years passed it is bad now'

# Partition Method,same as split but separator lies in between of each words
lst = demo.partition("10years passed")
for l in lst:
    print(l)
print(type(lst))
print(lst[1])

print(data.replace('is', 'vp'))  # Replaces given sub with provided sub


# Strip method removes the mentioned thing at starting and ending
stripdemo = '     Hi    '
print(stripdemo.strip())
# By default its spaces,we can override it anyway like this

stripdemo = '____hi_____'
print(stripdemo.strip("_"))

# Comparing strings
s1 = 'abc'
s2 = s1
print(s1 == s2)

print( s1 is not s2)