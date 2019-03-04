# Program to calculate the number of months you need to save before
# you can afford a down payment on a house
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:​ "))

portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0

while portion_down_payment >= current_savings:
    current_savings += current_savings * r / 12
    current_savings += portion_saved * (annual_salary / 12)
    months += 1
print("Number of months:", months)
