# import pyprsence
from typing import Optional
from pypresence import Presence, presence
import time
import os
import random
import string
import json
from roblox import Client
import asyncio
import sys
import requests
import roblox
from roblox.presence import PresenceProvider


pypresence_cookie = "8FF835EDE08B428FB37F97586EE821B8EDCA3898F75F43C4E79053510E967598C7566BD63E5CACB79A979D8B7F48CF4ABB307763ABC94827A11463E6F62635F388B6B9235C4CE3BEBF953E73275AE95E1CEF85F1E0DFA2256D78DFB8EB4E46C6D2BC882D1CEA35FC626D3EB94668718F079D645F0FBA283318C62982651258322EC0B2FA047A75F8D161BD0E9B191B4AD4FCE58677D1979CF64297D551688A77482E83E5AAF175BA16875424EF0E9747AD382630298CFF3449D20F50386A93BBDC6359540931BB08FF3D23FDC006BCEFC552C684A04C2F9F4310C0A83AD3F7F7153306114A9253D1C07E9A3ABE5126179146D2D4666FB7B92181EAF67DE674366595A1DFE42D415317C87B2283F4849F1221CFE2493C6EA9D3525BD0581BA494C0FA568A3480B3955FB4C318EC64D970BF009801F8A2A26563E0C85B34A9ED85D089D8A7F78A68FC7A52A89A70A3B48E36696358"
client = Client(token=pypresence_cookie)

with open('config.json') as f:
    data = json.load(f)
    ID = data[0]["ID"]
    username = data[0]["username"]

#running = True

#while running != False:
    

async def main():
    user = await client.get_user(ID)

    # presence = await client.presence.get_user_presences(user_ids=[ID])
    # print(presence)
    #print(presence[0]["placeId"])
    #print(presence)


    json={
        "userIds": user.id
    }
    
    presences_response = requests.post('https://presence.roblox.com/v1/presence/users',json,cookies={".ROBLOSECURITY":pypresence_cookie})
    # print(presences_response) shows 200 if everything went ok
    print(presences_response.json()) # prints the good stuff
    response = presences_response.json() # changes it to json so we can get the data out of it

    res = response["userPresences"]
    print(res)
    raw = res[0]
    print(raw)
    print(raw["userPresenceType"])

    global state
    global name

    state = "none"
    name = "none"

    if raw["userPresenceType"] == 1:
        state = "browsing"
        print("browsing")
    elif raw["userPresenceType"] == 2:
        print("playing")
        state = "playing"
        game_id = raw["placeId"]
        game = await client.get_place(int(game_id))
        name = game.name
    elif raw["userPresenceType"] ==3:
        print("developing")
        game_id = raw["placeId"]
        game = await client.get_place(int(game_id))
        name = game.name
        state = "developing"

loop = asyncio.get_event_loop().run_until_complete(main())

client_id = "882181964378030100"

if state == "playing":
    print("loading playing rp")
    RPC = Presence(client_id=client_id)
    RPC.connect()
    start_time = time.time()
    RPC.update(details=name,start=start_time,large_image="roblox",large_text="ROBLOX",small_image="game", small_text="playing",buttons=[{"label":"Join via profile", "url":f"https://www.roblox.com/users/{ID}/profile"}])
    print("loaded playing rp")
elif state == "browsing":
    RPC = Presence(client_id=client_id)
    RPC.connect()
    start_time = time.time()
    print("loading browsing rp")
    RPC.update(details="browsing",start=start_time,large_image="roblox",large_text="ROBLOX")
    print("loaded browsing rp")
elif state == "developing":
    client_id = "882537825227120660"
    RPC = Presence(client_id=client_id)
    RPC.connect()
    start_time = time.time()
    print("loading developing rp")
    RPC.update(details="developing",state=name,start=start_time,large_image="studio",large_text="ROBLOX STUDIO",small_image="dev", small_text="developing")
    print("loaded developing rp")

while 1:
    time.sleep(15)