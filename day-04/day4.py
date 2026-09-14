# day 4 of learning coding from 30 days of python repo 
#currently just learnt tuple
# I will be performing operations now on that 


#student information 

#task 1 : Create a tuple

# s_info = ("Krish", 18, "Computer Science", "SVIT vasad")

# #indexing specifically positive indexing 
# print(s_info[0])
# print(s_info[1])
# print(s_info[2])
# print(s_info[3])
#task 2 : add subjects and check if subject exists 

# sub = ("DSA", "Python", "ComputerNetworks","OperatingSystem", "ComputerArchitecture")

# print("First subject is : ",  sub[0])

# #Negative indexing 
# print("Last Subject is : ", sub[-1]) 

# #printing length
# print("Length of the tuple is : ", len(sub))

# #check if Python exists
# print("Python" in sub)

# #finding an index of a sub
# print("Index of OperatingSystem : ",sub.index("OperatingSystem"))


#task 3 slicing 

#print first three subjects of the tuple
# print("First three subjects using slicing : ", sub[0:3])

# #print last three subjects of the tuple
# print("Last three subjects using slicing  : ", sub[-3:])

# #print middle subjects of the tuple 
# print("Middle subject of the tuple : ", sub[2:3])

#task 4 

# numbers = (10, 20, 10, 30, 10, 40, 20)

# #show how many times 10 has appeared -- we ll use count() 

# print("How many times does 10 has appeared in the tuple : ", numbers.count(10))


# #show how many times 20 has appeared 
# print("How many times does 20 has appeared in the tuple : ", numbers.count(20))


#task 5 is to loop through the tuple and print it
# for x in sub: 
#     print(x)

#task 6 combine two tuple together
morning_sub = ("DSA", "Python")
evening_sub = ("OperatingSystem", "ComputerNetworks")
#combining tuples here 
combine = morning_sub + evening_sub
print(combine)
