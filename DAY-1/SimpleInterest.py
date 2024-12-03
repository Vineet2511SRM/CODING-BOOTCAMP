# Program to accept principle, time, rate of interest to calculate simple interest

principle=float(input("Enter the principle amount: "))

time=float(input("Enter the time: "))

rate_of_interest=float(input("Enter the rate of interest: "))

simple_interest=(principle*time*rate_of_interest)/100

print("Simple interest is:",simple_interest)