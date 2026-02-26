# Exercise 1: Vowel or Consonant


def check_letter():
    letter = input("Enter a letter: ").lower()
    if letter in ["a", "e", "i", "o", "u"]:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


check_letter()


# Exercise 2: Old enough to vote?


def check_voting_eligibility():
    age_input = input("Please enter your age: ")
    age = int(age_input)
    voting_age = 18

    if age < 0:
        print("Age cannot be negative.")
    elif age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


check_voting_eligibility()


# Exercise 3: Calculate Dog Years


def calculate_dog_years():
    age = int(input("Input a dog's age: "))

    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")


calculate_dog_years()

# Exercise 4: Weather Advice


def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


weather_advice()


# Exercise 5: What's the Season?


def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").title()
    day = int(input("Enter the day of the month: "))

    if (
        (month == "December" and day >= 21) or
        (month in ["January", "February"]) or
        (month == "March" and day <= 19)
    ):
        print("Winter")

    elif (
        (month == "March" and day >= 20) or
        (month in ["April", "May"]) or
        (month == "June" and day <= 20)
    ):
        print("Spring")

    elif (
        (month == "June" and day >= 21) or
        (month in ["July", "August"]) or
        (month == "September" and day <= 21)
    ):
        print("Summer")

    elif (
        (month == "September" and day >= 22) or
        (month in ["October", "November"]) or
        (month == "December" and day <= 20)
    ):
        print("Fall")


determine_season()