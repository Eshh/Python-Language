summ = 0
count = 0

print("Enter a number,Press zero to exit: ")

while True :
    n = int(input())

    if n == 0:
        break
    elif n < 0:  # ignoring negative numbers
        pass

    else:
        summ += n
        count += 1

print("Average of given {} numbers is {}".format(count, summ/count))
