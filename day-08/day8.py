#day 8 of python learning journey 
#today we ll learn about functions

#function -- is a reusable block of code that can be executed when it is called


#Task 1 — using function


#greeting using function

def greeting(name):
    return name + " Welcome to day 8 of the python journey"

print(greeting("Krish"))

#task 2 was to add two numbers in a function
def add(a, b):
    return a + b

print(add(5,2))

#task 3 calculating the area of a rectangle using function
def calculate_area(length, width):
    area = length * width
    return area

print("AREA : ", calculate_area(5,8))

#task 4 introduce yourself using function
def introduce(name, age):
    print("NAME : ", name)
    print("AGE : " , age)

introduce("Krish", 17)


#task 4
#taking 5 subjects marks as input as integers  
subject1 = int(input("Enter marks of the subject1 : "))
subject2 = int(input("Enter marks of the subject2 : "))
subject3 = int(input("Enter marks of the subject3 : "))
subject4 = int(input("Enter marks of the subject4 : "))
subject5 = int(input("Enter marks of the subject5 : "))

total = subject1 + subject2 + subject3 + subject4 + subject5 

#calculating total marks using function
def calculate_total():
    total = subject1 + subject2 + subject3 + subject4 + subject5 
    return total 

print("TOTAL MARKS : " ,calculate_total())

def calculate_percentage(number_of_subjects, total):
    percentage = total / number_of_subjects
    return percentage

print("PERCENTAGE : ",calculate_percentage(5, total))