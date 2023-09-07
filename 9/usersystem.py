import json

filename = 'username.json'
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
