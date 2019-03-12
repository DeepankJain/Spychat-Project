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
