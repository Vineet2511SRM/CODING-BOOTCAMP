employee_name=input("Enter the name of employee: ")
employee_ID=input("Enter the ID of employee: ")
employee_salary=float(input("Enter the monthly salary of employee: "))
employee_allowances=float(input("Enter the special allowances of employee: "))
bonus_percentage=float(input("Enter the annual bonus percentage of employee: "))

gross_monthly_salary=employee_salary+employee_allowances
bonus=(bonus_percentage/100)*(gross_monthly_salary*12)
annual_gross_salary=(gross_monthly_salary*12)+bonus

print(f"Employee name: {employee_name}")
print(f"Employee ID: {employee_ID}")
print(f"Employee gross monthly salary: {gross_monthly_salary}")
print(f"Employee gross annual salary: {annual_gross_salary}")