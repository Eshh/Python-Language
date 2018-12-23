lst = []
while True:
    s = input("Please enter the name: ")
    if s == 'end':
        break
    lst.append(s)


print(f"Given list of names are {lst[:]}")
print('After Sorting')
print(sorted(lst))
lengths = []

for n in lst:
    lengths.append(len(n))

print(f"Their respective lengths are {lengths[:]}")
