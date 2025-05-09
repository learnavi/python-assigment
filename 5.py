#taskCreate a Dictionary of Student Marks

stu={"alice": 85,
    "ayush": 90,
    "avi": 99,
    "neha": 88,
    "raj": 76}

a=input('enter the student name')
if a in stu :
     print( stu[a] )
else:
    print('not found in the records')
#task Demonstrate List Slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
x = numbers[0:5]
print(x)
print(list(reversed(x)))
