import requests

username = input("> ")
request = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()

name = request["name"]
uuid = request["id"]

print(name)
print(uuid)