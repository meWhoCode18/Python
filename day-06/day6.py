# Day 6 -- learning about dictionaries in python
#create a dict with name , age, course, semester

student = {
    "name": "Krish",
    "age": 17,
    "course": "Computer Engineering",
    "semester": 3
}

#access value using key values
print("accessing elements using dict :", student.get("name"))

#adding values in a dict
student["Specialization"] = "PYTHON"
print(student)

#updating or modifying an element in a dict
student["course"] = "Computer Science and Engineering"
print(student)

#checks whether a key exists or a key value pair exists
#we ll use condition
if "name" in student:
    print("name exists")

#Printing length of the dictionary

print("Length of the dict is : " ,(len(student)))