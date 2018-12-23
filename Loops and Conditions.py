a = 1400
b = 200
c = 300

if a > b:
    print(a)

elif b > a:

    print(b)

else:
    print(c)

# conditional expressions

print(a if a > b else b)

# Loops
# loops have else statement in python
n = 2
while n > 0:

    if n == 3:
        break

    print(n)
    n -= 1

else:
    print("over")

# for loop uses range

for n in range(1, 11):
    print(n, end=" ")

print("")
names = ['python', 'java', 'c']
for n in names:
    print(n)

k = 1
while k < 10:

    if k == 9:
        break
    print(k)
    k += 1
else:
    print("over")

# Enumerate
a = [1, 2, 3, 5, 6]
for i, n in enumerate(a):
    print(i, n)

# Zip

b = [4, 5, 6]
for n in zip(a, b):
    print(n)
    print(type(n))

# Sorted

k = [12, 1, 23, 32, 2, 12, 24, 26]
for n in sorted(k):
    print(n, end=" ")
