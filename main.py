from typing import Optional
import time
import os
import random
import string
import json
import asyncio
import sys
import requests
from pypresence import Presence

with open('config.json') as f:
    data = json.load(f)
    ID = data[0]["ID"]
    username = data[0]["username"]
    code = data[0]["code"]

client_id = "882181964378030100"

running = True

previous = [0] # set's a string for the previous presence, so we can compare if they're stil in the same presence they were before

RPC = Presence(client_id=client_id)
RPC.connect()

global PID
PID = 2

while running == True:

    request = requests.get("https://bloxpresenceserver.herokuapp.com/api",headers={"userID":ID,"code":code})
    print(request.json())
    req = request.json()

    if req["userPresenceType"] == 2 and 2 not in previous:
        previous.pop(0)
        previous.append(2)
        print("loading playing rp")
        RPC.clear(pid=os.getpid())
        client_id = "882537825227120660"
        RPC = Presence(client_id="882181964378030100")
        RPC.connect()
        start_time = time.time()
        RPC.update(pid=PID,details=req["game"],start=start_time,large_image="roblox",large_text="ROBLOX",small_image="game", small_text="playing",buttons=[{"label":"Join via profile", "url":f"https://www.roblox.com/users/{str(ID)}/profile"}])
        print("loaded playing rp")
    elif req["userPresenceType"] == 1 and 1 not in previous:
        previous.pop(0)
        previous.append(1)
        RPC.clear(pid=os.getpid())
        client_id = "882537825227120660"
        RPC = Presence(client_id="882181964378030100")
        RPC.connect()
        start_time = time.time()
        print("loading browsing rp")
        RPC.update(pid=PID,details="browsing",start=start_time,large_image="roblox",large_text="ROBLOX")
        print("loaded browsing rp")
    elif req["userPresenceType"] == 3 and 3 not in previous:
        RPC.clear(pid=os.getpid())
        previous.pop(0)
        previous.append(3)
        client_id = "882537825227120660"
        RPC = Presence(client_id=client_id)
        RPC.connect()
        start_time = time.time()
        print("loading developing rp")
        RPC.update(pid=3,details="developing",state=req["game"],start=start_time,large_image="studio",large_text="ROBLOX STUDIO",small_image="dev", small_text="developing")
        print("loaded developing rp")

    elif req["userPresenceType"] == 0 and 0 not in previous:
        previous.pop(0)
        previous.append(3)
        RPC.clear(pid=os.getpid())

    time.sleep(15)