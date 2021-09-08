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

request = requests.get("https://pypresence.wotanutt.repl.co/get_code",headers={"userID":ID,"userName":username})
#print(request.json())
#print(request)
to_json = request.json()
to_json["code"]
sus = to_json["code"] #lmao i'm so unimagintive with my variable names

print(f"3/3 please paste this code into your ROBLOX about me section: {sus}")


request = requests.get("https://pypresence.wotanutt.repl.co/register",headers={"userID":ID,"userName":username,"code":to_json["code"]})
json_format = request.json()
try:
    print(json_format["error"])
except:
    print("setup complete, you may now run the rich presence")


with open('config.json', 'w') as f:
    information = [{'username': json_format["userName"], 'ID': json_format["userID"], "code": json_format["code"]}]
    jsonString = json.dumps(information, indent=4)
    f.write(jsonString)
    f.close()