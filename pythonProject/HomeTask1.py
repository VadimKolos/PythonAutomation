from datetime import datetime

year = int(input("Input birth year: "))
month = int(input("Input birth month: "))

current_date = datetime.now()
age = current_date.year - year
if current_date.month < month : age -= 1

print(age)