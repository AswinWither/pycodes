num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
num3=int(input("Enter Number 3: "))

def largest(num1, num2, num3):
    if num1>num2 and num1>num3:
        largest_number = num1
    elif num2>num1 and num2>num3:
        largest_number = num2
    else:
        largest_number = num3
    print("The largest number is ", largest_number)

def smallest(num1, num2, num3):
    if num1<num2 and num1<num3:
        smallest_number = num1
    elif num2<num1 and num2<num3:
        smallest_number = num2
    else:
        smallest_number = num3
    print("The smallest number is ", smallest_number)


largest(num1,num2,num3)
smallest(num1, num2, num3)