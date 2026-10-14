
name = input("Enter your name: ")
college_id = input("Enter your college ID: ")

subject1 = int(input("Enter marks of OS: "))
subject2 = int(input("Enter marks of DS: "))
subject3 = int(input("Enter marks of DEF: "))
subject4 = int(input("Enter marks of CN: "))
subject5 = int(input("Enter marks of DBMS: "))

def total_marks(a, b, c, d, e):
    return a + b + c + d + e

marks = [subject1, subject2, subject3, subject4, subject5]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Each subject must be between 0 and 100.")

else:
    total = total_marks(subject1, subject2, subject3, subject4, subject5)
    percentage = total / 5

    print("\n----- Student Report -----")
    print("Name:", name)
    print("College ID:", college_id)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")

    if total <= 50:
        print("FAILED")
    elif total <= 100:
        print("Grade D")
    elif total <= 200:
        print("Grade C")
    elif total <= 300:
        print("Grade B")
    elif total <= 400:
        print("Grade A")
    else:
        print("Grade A+")

    print("\n- - - - - Subject Marks - - - - -")
    print("OS:", subject1)
    print("DS:", subject2)
    print("DEF:", subject3)
    print("CN:", subject4)
    print("DBMS:", subject5)

    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))
