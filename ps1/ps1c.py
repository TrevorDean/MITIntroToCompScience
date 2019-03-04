# Program to calculate the savings rate each month to be able to afford
# a down payment in 3 years
annual_salary = float(input("Enter your annual salary: "))
savings_rate_as_decimal = 10000  # Percent of salary to save each month expressed as integer but reresenting
                       # ten thousandths of a percent
total_cost = 1000000
semi_annual_raise = .07
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04  # Annual return on savings that have been invested
months = 0
monthly_salary = annual_salary / 12
high = savings_rate_as_decimal
low = 0
after36_savings = 0
savings_rate_guess_integer = (high + low) / 2
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
    savings_rate_as_decimal = .0001 * savings_rate_guess_integer
    after36_savings = amount_saved(months, current_savings, savings_rate_as_decimal, monthly_salary)
    if 250100 >= after36_savings >= 249900:
        print("Best savings rate:", round(savings_rate_guess_integer * .0001, 4))
        print("Steps in bisection search:", steps)
    if after36_savings > 250100:
        high = savings_rate_guess_integer
    else:
        low = savings_rate_guess_integer

    if low == 10000:
        print("It is not possible to pay the down payment in three years.")
        print("steps:", steps)
        break
    savings_rate_guess_integer = (high + low) / 2