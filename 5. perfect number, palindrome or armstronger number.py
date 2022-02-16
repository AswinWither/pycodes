num=int(input("Enter number: "))
check=int(input("Enter the number code of what you want to check from the following\n 1.Perfect Number\n 2. Armstrong Number\n 3. Palindrome\n "))

def perfect_number(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

def Armstrong_Number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

def isPalindrome(num):
    temp = num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10

    if temp == num:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
    
if check == 1:
    perfect_number(num)
elif check == 2:
    Armstrong_Number(num)
elif check == 3:
    isPalindrome(num)
else:
    print("Option not defined")