name = input("enter the user name:")
monthly_income = float(input("enter the monthly income: "))
credit_score = int(input("enter your current credit score: "))
loan_amount = int(input("enter the requested loan amount you want to take: "))

is_approved = monthly_income >= 30000 and credit_score >= 700

is_high_risk = monthly_income <= 20000 or credit_score <= 600
processing_fee = 0.02 * loan_amount
monthly_emi = loan_amount / 12
print("-" * 40)
print("BANK LOAN SYSTEM - RESULT")
print("-" * 40)
print(f"applicant name:\t\t {name}\n")
print(f"income:\t\t {monthly_income}\n")
print(f"credit score:\t\t {credit_score}\n")
print("-" * 3 + "DECISION" + "-" * 3)
print(f"approved:\t\t {is_approved}\n")
print(f"high risk:\t\t {is_high_risk}\n")
print("-" * 3 + "FINANCIALS" + "-" * 3)
print(f"loan amount:\t\t {loan_amount}\n")
print(f"processing fee:\t\t {processing_fee}\n")
print(f"monthly emi:\t\t {monthly_emi}\n")
print("-" * 40)

