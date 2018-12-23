
s = 'Eshwar'

print(s[1])
#  s[1] = 'w' Strings are Immutable in python
print(type(s))

# String indexes start from zero from left and -1 from right

print(s[-1])

# Strings support slicing for obtaining sub-strings in which ending number is excluded

print(s[0:5])

print(s[:566])
print(s[0:])

print(s[:4])

print(s[0:56])

# Reverse order slicing starting from -1

print(s[-3:])
print(s[-4:-1])
print(s[::-1])  # Reverse  #  Default Increment for Slicing is 1, :: increments it by 2

#  Strings are iterable

for c in s:
    print(c, end="  ")
print()
print(s[::2])

print(s[0:-2])
print(s[:5])

# other way to increment slicing
print(s[1:6:2])

test = "Xbox | 30 | New"
print(test[0:])

print(test[::-1])
Product = test[0:test.index('|')]
parts = test.split('|')
for p in parts:
    print(p)











