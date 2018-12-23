# Accept a list and place all even numbers on the left and odd numbers on the right

l = []
while True:
    n = int(input("Please enter a number,press 0 to stop: "))
    if n == 0:
        break

    l.append(n)

print(f"Given list of numbers is: {l[:]}")
print()

i = 0
temp = []
for n in l:
    if n % 2 == 0:
        temp.insert(i, n)
        i += 1
    elif n % 2 != 0:
        temp.append(n)

l = temp.copy()
print("The modified list with even numbers on the left and odd numbers on the right is")
print(l[:])
