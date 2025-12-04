"""Wap to find out how many days,month,
  weeks we have left-
  if we live until 90 years old"""
age = int(input("Enter age:"))   # Take age as input from the user
years_left = 90 - age            # Calculate years left until age 90
days_left = years_left * 365     # Approximate days left (ignoring leap years)
months_left = years_left * 12    # Approximate months left
weeks_left = years_left * 52     # Approximate weeks left

# Print the result using f-string formatting
print(f"{years_left} Years {months_left} months {days_left} days {weeks_left} weeks")