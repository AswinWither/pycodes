n = int(input("How many integers do you want to add to the list? "))
list1 = []

for i in range(0, n):
    i = int(input("Enter number: "))
    list1.append(i)

index = int(input("Enter an element to search: "))
index = index + 1
if(index not in list1):
    print("Element not found")
else:
    print("Element is at ", list1.index(index))