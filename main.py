import sys
import default

choice = input("Enter 1 if you want to go with default settings")
if choice == '1':
    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating

    

else:

#Name of the spy
    spy_name = input("Enter the name of the spy")

#Salutation(Mr. or Mrs.)
    spy_salutation = input("Enter your salutation(Mr. or Mrs.)")

#Age
    spy_age = input("Enter your age")

#Rating
    spy_rating = input("Enter your rating")

#Validating the name of the spy
    if spy_name.isalpha() == False:
        print("Name is invalid")
        sys.exit(0)

#Vallidating the age of the spy
    if int(spy_age) <= 12:
        print("Too young")
        sys.exit(0)
    elif int(spy_age) >= 60:
        print("Too old")
        sys.exit(0)

#Rating of the spy_age
    if spy_rating == 'A':
        print("You are 3 star spy")
    elif spy_rating == 'B':
        print("You are a 2 star spy")
    elif spy_rating == 'C':
        print("You are a 1 star spy")
    else:
        print("You have enterd incorrect rating")
        sys.exit(0)

print("Hello " + spy_salutation + spy_name)
print("Your age is " + spy_age)
print("Your rating is " + spy_rating)
