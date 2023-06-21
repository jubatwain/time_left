age = input("What is your current age? ")

new_age=int(age)
days=90 * 365
weeks=90 * 52
months=90 * 12
days_left= (days-(new_age* 365))
weeks_left= (weeks-(new_age* 52))
months_left= (months-(new_age* 12))
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
