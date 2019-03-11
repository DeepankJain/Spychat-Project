import sys
import default

STATUS_MESSAGES = []

def add_status(current_status_message):
    if(current_status_message == None):
        print("You do not have any current status")
    else:
        print("Your current status is", current_status_message)

    update_choice = input("Do you want to select from old status?(y/n): ")
    if update_choice.upper() == 'N':
        new_status_message = input("Enter the new status: ")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)


    elif update_choice.upper() == 'Y':
        for i in range(len(STATUS_MESSAGES)):
            print(str(i+1) + " " + STATUS_MESSAGES[i])
        message_Selection = int(input("Choose from the older message"))
        if len(STATUS_MESSAGES) > message_Selection:

            updated_status_message = STATUS_MESSAGES[message_Selection - 1]
    return updated_status_message

def start_chat(spy_name, spy_age, spy_rating):

    current_status_message = None
    show_menu = True
    while(show_menu):
        menu_choice = input("1. Add a status update\n2. Exit Application")
        if menu_choice == '1':
            print("you have chosen to add a status")
            current_status_message = add_status(current_status_message)
        elif menu_choice == '2':
            show_menu = False


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
    if int(spy_age) >= 12 and int(spy_age) <= 50:
        print("you are eligible")

    else:

        print("You are not eligible")
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

print("Hello %s %s. Your age is %s. Your rating is %s." %(spy_salutation, spy_name, spy_age, spy_rating))
# print("Your age is " + spy_age)
# print("Your rating is " + spy_rating)
start_chat(spy_name, spy_age, spy_rating)
