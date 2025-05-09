#task  Read a File and Handle Errors

try:
  with open("C:/Users/avi shukla/Documents/sample.txt", "r") as file1:
    print(file1.readline())
    print(file1.readline())
except FileNotFoundError:
  print("the file sample.txt not found")



#task  Write and Append Data to a File
with open('output.txt','w')as file2:
    file2.write('hello,python')

    with open('output.txt', 'r') as file3:
        reading = file3.read()
        print(reading)

with open('output.txt','a')as file4:
    file4.write('learning file handling in python')

    with open('output.txt', 'r') as file5:
        reading = file5.read()
        print(reading)