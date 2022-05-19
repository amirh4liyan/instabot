from instagrapi import Client
import sys

cl = Client()

# Login
User, Pass = 'am1r4lian', 'CIV8kvub3z'
cl.login(User, Pass)

# Read File
with open('accounts.txt') as f:
    content = f.readlines()

for i in range(len(content)):
    content[i] = content[i].strip('\n')

diction = {}
c = 0
for item in content:
    if '@' in item:
        users = set()
        while content[c] != '':
            users.add(content[c].split()[1])
            c += 1
        c += 1
        key = item[item.index(' ')+1:]
        users.remove(key)
        diction[key] = users

key = sys.argv[1]
for user in diction[key]:
    try:
        cl.user_follow(cl.user_id_from_username(user))
    except:
        print(f'User {user} Not Found!')
