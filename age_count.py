def age_count(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = age_count(birth_year)

print(f"Hello {name}! You are {age}.")
