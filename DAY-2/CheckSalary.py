# Taking name and salary as input from the user
name=input("Enter the name of employee: ")
salary=int(input("Enter the salary: "))
# Checking the tax paying criteria
if (name!=" " and salary>300000):
    print(name,"has to pay the tax")
elif(salary>=0 and salary<=300000):
    print(name,"doesn't need to pay tax")
else:
    print("Invalid Input")