#day 9 -- conditional statments 
#conditional statments

# Task 1 - Smart Grade Analyzer

student_name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

print(student_name)

# Conditional statements

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("GRADE : A")

elif marks >= 80:
    print("GRADE : B")

elif marks >= 70:
    print("GRADE : C")

elif marks >= 60:
    print("GRADE : D")

elif marks >= 40:
    print("GRADE : E")

else:
    print("GRADE : F")


#task 2 
#ATM SIMULATOR


balance = 1000

print("--- ATM ---")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")

atm_input = input("Enter the number to proceed: ")

if atm_input == "1":
    print("YOUR BALANCE:", balance)

elif atm_input == "2":
    amount_to_deposit = int(input("Enter the amount to deposit: "))

    if amount_to_deposit > 0:
        balance += amount_to_deposit
        print("DEPOSIT SUCCESSFUL")
        print("YOUR NEW BALANCE:", balance)
    else:
        print("Invalid deposit amount")

elif atm_input == "3":
    amount_withdraw = int(input("Enter the amount that you want to withdraw: "))

    if amount_withdraw <= 0:
        print("Invalid withdrawal amount")
    elif amount_withdraw > balance:
        print("Insufficient balance")
    else:
        balance -= amount_withdraw
        print("WITHDRAWAL SUCCESSFUL")
        print("YOUR NEW BALANCE:", balance)

else:
    print("Invalid choice")