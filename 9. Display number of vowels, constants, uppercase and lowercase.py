s = input("Enter any string :")
vowel = consonent = uppercase = lowercase= 0
for i in s:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
         vowel = vowel +1
    else:
         consonent = consonent + 1
    if i.isupper() :
        uppercase = uppercase + 1
         
    if i.islower():
        lowercase = lowercase + 1
         
print("Total number of vowel:",vowel)
print("Total number of consonent:",consonent)
print("Total number of uppercase letter:",uppercase)
print("Total number of lowercase letter:",lowercase)