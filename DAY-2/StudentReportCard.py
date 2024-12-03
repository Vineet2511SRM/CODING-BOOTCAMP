name=input("Enter the name of student: ")

subject1_score=float(input("Enter the score of first subject (out of 100): "))
subject2_score=float(input("Enter the score of second subject (out of 100): "))
subject3_score=float(input("Enter the score of third subject (out of 100): "))

average_score=(subject1_score+subject2_score+subject3_score)/3

if(average_score>=60 and name!=" "):
    print(f"1st Class")
elif(average_score>=50 and name!=" "):
    print(f"2nd Class")
elif(average_score>=35 and name!=" "):
    print(f"Pass Class")
elif(average_score<35 and name!=" "):
    print(f"Fail")
else:
    print("Invalid Input")