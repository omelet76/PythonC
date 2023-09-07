import json


def greet_user():
    filename = 'username2.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except:
        username = input('what is you name')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f'we well remember you when you come back,{username}')
    else:
        print(f'welcome back ,{username}')


greet_user()
