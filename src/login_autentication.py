import json


def login_autentication(user_input, password_input):
    with open('users.json') as users:
        list = json.load(users)
    
        if user_input == list[0]['username'] and password_input == list[0]['password']:
            return user_input
        else:
            if user_input == list[1]['username'] and password_input == list[1]['password']:
                return user_input
            else:
                return "/"
            