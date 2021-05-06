import requests
import json

key = "/api new!"
player_name = input("Player name:")
print("Getting UUID...")
uuid_url = f'https://api.mojang.com/users/profiles/minecraft/{player_name}?'
response_uuid = requests.get(uuid_url)
uuid = response_uuid.json()['id']
print(f"Got UUID - {uuid}")
print("Getting hypixel....")
online_link = f"https://api.hypixel.net/status?key={key}&uuid={uuid}"
main_link = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"
recent_link = f"https://api.hypixel.net/recentgames?key{key}&uuid={uuid}"
recent_response = requests.get(recent_link)
recent_data = recent_response.json()
main_response = requests.get(main_link)
main_data = main_response.json()
online_response = requests.get(online_link)
online_data = online_response.json()

Session = online_data.get('session', False)
if Session != False:
    playing_rn_gametype = Session.get('gameType', "Not Found")
    playing_rn_map = Session.get('map', "Not Found")
    playing_rn_mode = Session.get('mode', "Not Found")
else:
  playing_rn_gametype = "Not found"
  playing_rn_mode = "Not found"
  playing_rn_map = "Not found"




print("Got it")
def online():
  try:
    if "Malform" in online_data['cause']:
      print("Wrong username!")
  except:
    isonline = online_data['session']['online']
    if isonline == False:
      print("Player is offline!")
    else:
      print(f"Player is online! and playing {playing_rn_gametype} , {playing_rn_mode} on {playing_rn_map} ")

def rank():
  try:
    if "Malform" in data['cause']:
      print("Wrong username!")
  except:
    rank = main_data["player"]["rank"]
    print(rank)



what = input("What you want to check! [Online] , [Rank]:")

stuff = ["Online" , "Rank"]

if what == "Online":
  online()

if what == "Rank":
  rank()


if what not in stuff:
  print("Wrong")
  




