# the code for the server but replit is being shit so i'm storing it here for now

from quart import Quart, request
import requests
from roblox import Client
import os

client = Client(token=os.getenv("pypresence_cookie"))


app = Quart('')

@app.route('/')
async def home():
  return '<p>Hello World</p>'

@app.route("/api",methods=["GET","POST"])
async def json():
    if request.method == "GET":
      print(request.headers["userID"])

      json={
          "userIds": request.headers["userID"]
      }
      
      presences_response = requests.post('https://presence.roblox.com/v1/presence/users',json,cookies={".ROBLOSECURITY":os.getenv("pypresence_cookie")})
      # print(presences_response) shows 200 if everything went ok
      print(presences_response.json()) # prints the good stuff
      response = presences_response.json() # changes it to json so we can get the data out of it

      res = response["userPresences"]
      print(res)
      raw = res[0]
      print(raw)


      if raw["userPresenceType"] == 1:
        json={
        "userPresenceType": raw["userPresenceType"]
      }
      elif raw["userPresenceType"] == 2:
        game_id = raw["placeId"]
        game = await client.get_place(int(game_id))
        name = game.name
        json={
        "userPresenceType": raw["userPresenceType"],
        "game": name
      }


      elif raw["userPresenceType"] ==3:
        game_id = raw["placeId"]
        game = await client.get_place(int(game_id))
        name = game.name
        json={
        "userPresenceType": raw["userPresenceType"],
        "game": name
      }

      return request.jsonify(json),200
    #elif request.method == "POST":
     # content = request.json
      #print(content)
      #return request.jsonify({"post":"userIds"},200)

def run():
  app.run(
    host='0.0.0.0',
    port=8000,
    debug=True
  )

run()