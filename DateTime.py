import datetime
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
try:
    dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
    exit()
now = datetime.datetime.now()
age_delta = now - dob

years = age_delta.days // 365
days = age_delta.days
weeks = age_delta.days // 7
hours = age_delta.total_seconds() // 3600
# mintutes = age_delta.min // 3600 *60

print(f"You are {years} years, {days} days, {weeks} weeks, {int(hours)} hours old")