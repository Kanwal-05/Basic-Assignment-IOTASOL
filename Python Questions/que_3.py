# WAP to Calculate the salary of employee. user enter the basic salary, HRA, TA
basicsalary=int(input("Enter the Basic Salary : "))
TA=int(input("Enter the Tarvel Allowance : "))
HRA=int(input("Enter the House Rent Allowance : "))
Salary = basicsalary + HRA + (2*TA) + (0.5*basicsalary )
print()
print("Total Salary is : ",Salary)