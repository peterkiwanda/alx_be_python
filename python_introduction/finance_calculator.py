# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate
annual_interest_rate = 0.05

# Project annual savings with interest
annual_savings_before_interest = monthly_savings * 12
projected_savings = annual_savings_before_interest + (annual_savings_before_interest * annual_interest_rate)

# Output the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings after including interest: ${projected_savings:.2f}")

