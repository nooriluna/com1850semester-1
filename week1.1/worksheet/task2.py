"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: AREZO NOORI
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
monthly_input = input("could you please enter the amount you plan to save every month?(whole number only):")
monthly_savings = int(monthly_input)


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
total = monthly_savings * 12
print(f"welcome back! By saving £{monthly_savings} every month, you will have saved £{total} in a year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest_rate = 0.008
total_with_interest = total + (total * interest_rate)
print (f"After adding 0.08% interest, your total will be £{total_with_interest: .2f} per year.")