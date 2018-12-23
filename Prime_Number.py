# Accepting a number and determining wether its prime or composite number

num = int(input("Please enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("its a composite number")
        break
else:
    print("Its a prime number")
