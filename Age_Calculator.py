user_age = int(input("What is your Age/Year of birth.\n"))

year_age = 0
age = 0

if len(str(user_age)) == 4:
    year_age = user_age
elif len(str(user_age)) == 2:
    year_age = 2022 - user_age

if year_age < 1900:
    print("You seem to be the oldest person alive")
    exit()
elif year_age > 2022:
    print("You are not yet born")
    exit()

print(f"You will be 100 years old in {year_age + 100}")

interestedYear = int(input("Enter your interested Year."))

print(f"You will be {interestedYear - year_age} years old in {interestedYear}")
