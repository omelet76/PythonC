import json


def get_stored_username():
    filename = 'username2.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f'welcome back,{username}')
    else:
        # username = input('what is you name')
        # filename = 'username2.json'
        # with open(filename, 'w') as f:
        #     json.dump(username, f)
        username = new_user()
        print(f'we will remember you when you come banck,{username}')


def new_user():
    username = input('what is you name')
    filename = 'username2.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


greet_user()
