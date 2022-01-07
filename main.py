#!/usr/bin/python3

import argparse
from instagrapi import Client

# Arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("-d", "--dontlogin", action="store_true",
                    help="prevent from login to account")
group.add_argument("-f", "--follow", help="")
group.add_argument("-u", "--unfollow", help="")
args = parser.parse_args()

# Login
cl = Client()
if not args.dontlogin:
    User, Pass = "aryaramnes20", "@mir8157"
    cl.login(User, Pass)

if args.follow:
    path = args.follow
elif args.unfollow:
    path = args.unfollow

with open(path) as f:
    content = f.readlines()

guys = set()
for item in content:
    if "usr" in item:
        item = item.strip()
        guys.add(item.split()[1])

print(guys)
