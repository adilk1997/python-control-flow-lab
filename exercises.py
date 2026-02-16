# Exercise 1: Vowel or Consonant

def check_letter():
    vowel = ['a', 'e', 'i', 'o', 'u']
    letter = input('enter a letter: ')
    if letter in vowel:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")

check_letter('a')


# Exercise 2: Old enough to vote?

def check_voting_eligibility(age):
    voting_age = 18
    if age < voting_age:
        return f"your {age} is less than 18, you cannot vote"
    else:
        return f"your {age} is ok, you can vote"
print(check_voting_eligibility( 17))


# Exercise 3: Calculate Dog Years

def calculate_dog_years(age):
    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7

    print(f"The dog's age in dog years is {dog_years}.")


calculate_dog_years(5)

# Exercise 4: Weather Advice

def weather_advice(cold, raining):
    if cold == 'yes' and raining == 'yes':
        print ('wear a waterproof coat')
    elif cold == 'yes' and raining == 'no':
        print ('wear a jacket')
    elif cold == 'no' and raining == 'yes':
        print('take a umbrella')
    else:
        print ('there is a good weather')

weather_advice('yes', 'no')


# Exercise 5: What's the Season?

def determine_season(month):
    if month in ['february', 'march', 'april' , 'may']:
        print ('is spring')
    elif month in ['june', 'july', 'august']:
        print ('is summer')
    else:
        print ('is winter')

determine_season('april')

