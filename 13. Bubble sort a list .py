def sortList(array):
	for item in range(len(array)):
		for j in range(0, (len(array) - item - 1)):
			if array[j] > array[j + 1]:
				(array[j], array[j + 1]) = (array[j + 1], array[j])

numbers = []
n = int(input("Enter Number of elements"))
for i in range(0,n):
    i = int(input("Enter number: "))
    numbers.append(i)

sortList(numbers)
print("Sorted list is: ", numbers)