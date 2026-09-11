print("hello world hi " ,end = " ")
print("hello world again! ")


#This is a comment
#of more than one line
#its okay to learn this 

"""
hi 
this is krish 

"""

x = "orange"
y = "orange"
print(x,y)


x = 5 
y = "Krish"
print(x)
print(y)

#global variable 
name = "krish"

def my_func():
    print("my name is", name)

my_func()


x = "awesome"

def py():
    x = "py"

py()
print("python is", x )



#besides this I learnt all the basics of python.
# and other stuff like data types
# operators
# and etc

# now i ll be moving on to control flow statments like if , if else and pass, break and continue statments.


#this is the mini project of day 1
#Student score analyzer 

name = input("Enter your name : ")

Maths = int(input ("Enter your Maths marks out of 100 : "))
ComputerScience = int(input ("Enter your ComputerScience marks out of 100 : "))
Science = int(input("Enter your Science marks out of 100 : "))
SocialScience =int(input ("Enter your SocialScience marks out of 100 : "))
English = int(input("Enter your English marks out of 100 : "))

Total_marks = Maths + ComputerScience + Science + SocialScience + English
Percentage = Total_marks / 500 * 100

print("----- student score -----")
print(name ,"total marks is = ", Total_marks)
print("Percentage = ", Percentage)