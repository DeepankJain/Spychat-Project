friends = []


def add_friend():
    new_friend = {'name': "",
                  'age':"0",
                  'rating':'A',
                  'is_online': True
                  }
    new_friend['name'] = input("enter your name: ")

    new_friend['age'] = int(input("Enter your age: "))
    new_friend['rating'] = input("Enter your rating: ")
    new_friend['is_online'] = True

    if new_friend['name'].isalpha() == False:
        print("Invalid name")
        sys.exit(0)

    if new_friend['age'] <= 12 or new_age >= 50:
        print("Invalid age")
        sys.exit(0)

    friends_name.append(new_friend)
