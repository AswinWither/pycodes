n = int(input("Enter number of students: "))  

result = {}  

for i in range(n):  

   print("Enter Details of student No.", i+1)  

   rno = int(input("Roll No: "))  

   name = input("Name: ")  

   marks = int(input("Marks: "))  

   result[rno] = [name, marks]    

print(result)  

# Display names of students who have got marks more than 75  

for student in result:  

   if result[student][1] > 75:  

       print(result[student][0])  