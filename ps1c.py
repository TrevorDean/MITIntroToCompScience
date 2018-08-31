# Program to calculate the savings rate each month to be able to afford
# a down payment in 3 years
annual_salary = float(input("Enter your annual salary: "))
portion_saved = 10000 # Percent of salary to save each month expressed as integer but reresenting
                      # ten thousandths of a percent
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0
monthly_salary = annual_salary / 12
high = portion_saved
low = 0
after36_savings = 0
guess_percent = (high + low) / 2
steps = 0

def amount_saved(months, current_savings, portion_saved, monthly_salary):
    while months < 36:
        current_savings += current_savings * r / 12
        current_savings += portion_saved * monthly_salary
        months += 1
        if months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return current_savings

while after36_savings > 250100 or after36_savings < 249900:
    steps += 1
    portion_saved = .0001 * guess_percent
    after36_savings = amount_saved(months, current_savings, portion_saved, monthly_salary)
    if 250100 >= after36_savings >= 249900:
        print("Best savings rate:", round(guess_percent * .0001, 4))
        print("Steps in bisection search:", steps)
    if after36_savings > 250100:
        high = guess_percent
    else:
        low = guess_percent

    if low == 10000:
        print("It is not possible to pay the down payment in three years.")
        print("steps:", steps)
        break
    guess_percent = (high + low) / 2


