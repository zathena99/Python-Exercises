import sys
students = {}
for i in range(3):
    print("Enter student number for classmate " + str(i+1) + ":")
    num = int(input())
    print("Enter first name for classmate " + str(i+1) + ":") 
    name = input()
    students[num] = name

print("Student Information:")
for num, name in students.items():
    print("Student Number: " + str(num) + ", Name: " + name)

if len(students) >= 3:
    third_key = list(students.keys())[2] 
    del students[third_key]
else:
    print("Not enough entries to delete the third entry.")
    
print("Enter your student number:")
your_num = int(input())
print("Enter your first name:")  
your_name = input()
students[your_num] = your_name

print("Updated Student Information:")
for num, name in students.items():
    print("Student Number: " + str(num) + ", Name: " + name)