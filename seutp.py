import requests
import json
import os

# basic basic setup
# gui coming soon


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
code = input("3/3 Please join the verification game and enter the code into the terminal below ")

request = requests.get("https://bloxpresenceserver.herokuapp.com/check_code",headers={"userID":ID,"userName":username,"code":code})
print(request)
print(request.json())
to_json = request.json()
to_json["code"]
sus = to_json["code"] #lmao i'm so unimagintive with my variable names

with open('config.json', 'w') as f:
    information = [{'username': to_json["userName"], 'ID': to_json["userID"], "code": to_json["code"]}]
    jsonString = json.dumps(information, indent=4)
    f.write(jsonString)
    f.close()