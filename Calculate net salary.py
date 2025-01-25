Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> gross_salary = float(input("Enter the gross salary: "))
Enter the gross salary: 100000
>>> allowance = 0.10 * gross_salary
>>> deduction = 0.03 * gross_salary
>>> net_salary = gross_salary + allowance - deduction
>>> print("The net salary is: ",net_salary)
The net salary is:  107000.0
