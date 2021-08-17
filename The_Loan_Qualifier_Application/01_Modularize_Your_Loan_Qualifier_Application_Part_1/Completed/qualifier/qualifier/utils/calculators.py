
# This script contains a variety of financial calculator functions needed to determine loan qualifications.

# Calculates user's monthly debt-to-income ratio
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio

# Calculates user's loan-to-value
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
