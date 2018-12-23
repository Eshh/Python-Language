
lst = []
count = 0

while count <= 5:
    name = input("Please enter a name: ")
    lst.append(name)
    count += 1

for l in lst:
    print(l)

sum = 0
count = 0
for l in lst:
    sum += len(l)
    count += 1

avg = sum / count
print(avg)

# another exercise to check wether given number is a valid mobile no or not

no = input("Enter the mobile number: ")
if len(no) == 10:
    print("Its a valid mobile number!")
else:
    print('Its an invalid mobile number')
