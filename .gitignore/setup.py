import os
import random
import string
import json
import time
from roblox import Client
import asyncio
import sys

import roblox

client = Client()
string.ascii_letters

code = ""
loops = 0

while loops != 16:
    letter_or_number = random.randint(1,2)
    if letter_or_number == 1:
        code = code + str(random.randint(1,9))
    else:
        code = code + str(random.choice(string.ascii_letters))
    loops = loops + 1

cmd="python3 main.py"

print("-------------------------------------")
print("Thank you for installing pypresence")
print("-------------------------------------")
print("Before we continue, we need some")
print("vital information. All information")
print("stays local to your machine")
print("-------------------------------------")
username = input("1/3 Please enter your ROBLOX username ")
print("-------------------------------------")
ID = input("2/3 Please enter your ROBLOX ID ")
print("-------------------------------------")
print(f"3/3 For confrimation purposes please paste \n this code into your roblox about: \n {code}")
time.sleep(60)

async def main():
    try:
        user = await client.get_user(ID)
    except Exception as e:
        print(e)
        sys.exit()
        return
    if user.name != str(username):
        print("the user ID does not match the username, please ensure they match and that you are entering the username rather than a display name.")
        sys.exit()
        return
    if code in user.description:
        print("Confirmation success")
    else:
        print("authentication failed")
        sys.exit()
        return
    #print("Name:", user.name)
    #print("Display Name:", user.display_name)
    #print("Description:", user.description)

loop = asyncio.get_event_loop().run_until_complete(main())


with open('config.json', 'w') as f:
    information = [{'username': username, 'ID': ID}]
    jsonString = json.dumps(information, indent=4)
    f.write(jsonString)
    print("config file created")

print("Confirmed, your roblox rich presence is now setup and ready to go")



os.system(cmd)