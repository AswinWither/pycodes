def isPalindrome(s):
     
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are
    # equal or not
    if (s == rev):
        return True
    return False

s = input("Enter text to check if it is palindrome and swap its case: ")
print(isPalindrome(s))
print("The swapped case is ", s.swapcase())