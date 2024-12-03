employee_name=input("Enter the name of employee: ")
employee_ID=input("Enter the ID of employee: ")
employee_salary=float(input("Enter the monthly salary of employee: "))
employee_allowances=float(input("Enter the special allowances of employee: "))
bonus_percentage=float(input("Enter the annual bonus percentage of employee: "))

gross_monthly_salary=employee_salary+employee_allowances
bonus=(bonus_percentage/100)*(gross_monthly_salary*12)
annual_gross_salary=(gross_monthly_salary*12)+bonus
standard_deduction=annual_gross_salary-50000

if (annual_gross_salary>500000 and annual_gross_salary<=1500000):
    standard_deduction=standard_deduction - (0.1)*annual_gross_salary
elif annual_gross_salary>1500000:
    standard_deduction=standard_deduction - (0.3)*annual_gross_salary

print(f"Employee name: {employee_name}")
print(f"Employee ID: {employee_ID}")
print(f"Employee gross monthly salary: {gross_monthly_salary}")
print(f"Employee gross annual salary: {annual_gross_salary}")
print(f"Employee gross annual salary after deduction of taxes: {standard_deduction}")