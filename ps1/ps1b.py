# Program to calculate the number of months you need to save before
# you can afford a down payment on a house. Including calculations for a
# semi-annual raise
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0
monthly_salary = annual_salary / 12
while portion_down_payment >= current_savings:
    current_savings += current_savings * r / 12
    current_savings += portion_saved * monthly_salary
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
print("Number of months:", months)