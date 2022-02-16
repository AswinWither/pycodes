n = int(input("How many integers do you want to add to the list? "))
list1 = []

for i in range(0, n):
    i = int(input("Enter number: "))
    list1.append(i)
    if n == 1:
        print("In order to check for integers, list must have at least 2 integers.")
    else:
        continue

print("The largest number is ", max(list1))
print("The smallest number is ", min(list1))

