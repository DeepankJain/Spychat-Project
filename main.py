import sys
import default
import spy_status
import spy_friend








def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None
    show_menu = True
    while(show_menu):
        menu_choice = input("1. Add a status update\n2. Add Friend\n3. Exit Application")
        if menu_choice == '1':
            print("you have chosen to add a status")
            current_status_message = spy_status.add_status(current_status_message)

        elif menu_choice == '2':
            print("you have chosen to add a friend")
            spy_friend.add_friend()

        elif menu_choice == '3':
            show_menu = False







spy = {}
choice = input("Enter 1 if you want to go with default settings")
if choice == '1':
    spy['name'] = default.spy['name']

    spy['age'] = default.spy['age']
    spy['rating'] = default.spy['rating']
    spy['is_online'] = default.spy['is_online']



else:

#Name of the spy
    spy['name'] = input("Enter the name of the spy")

#Salutation(Mr. or Mrs.)


#Age
    spy['age'] = input("Enter your age")

    #Rating
    spy['rating'] = input("Enter your rating")
    spy['is_online'] = True

#Validating the name of the spy
    if spy['name'].isalpha() == False:
        print("Name is invalid")
        sys.exit(0)

 #Vallidating the age of the spy
    if int(spy['name']) >= 12 and int(spy['name']) <= 50:
        print("you are eligible")

    else:

        print("You are not eligible")
#Rating of the spy_age
    if spy['rating'] == 'A':
        print("You are 3 star spy")
    elif spy['rating'] == 'B':
        print("You are a 2 star spy")
    elif spy['rating'] == 'C':
        print("You are a 1 star spy")
    else:
        print("You have enterd incorrect rating")
        sys.exit(0)

print("Hello " + spy['name'] + "Your age is " + spy['age'] + "Your rating is " + spy['rating'])
# print("Your age is " + spy_age)
# print("Your rating is " + spy_rating)
start_chat(spy['name'], spy['age'], spy['rating'])
