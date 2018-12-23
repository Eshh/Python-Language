# Accept a list of numbers from user and sort it

# First for numbers, 0 to stop the entering
sortintegers = []

while True:
    n = int(input("Please enter a number, Press 0 to stop: "))
    if n == 0:
        break
    sortintegers.append(n)

print(f"The sorted list is {sorted(sortintegers)}")
print(sorted(sortintegers, reverse=True))  # overriding keyword arguments

# same program fro strings

sortstrings = []

while True:
    s = input("Please enter a name, Press end to stop: ")
    if s == 'end':
        break
    sortstrings.append(s)

print(f"The sorted list is {sorted(sortstrings),}")
