import aiohttp
import asyncio

username = input("> ")

async def findUUID(username):
        async with aiohttp.ClientSession() as session:
            requesturl = f"https://api.mojang.com/users/profiles/minecraft/{username}"
            async with session.get(requesturl) as resp:
                outputresponse = await resp.json()
                name = outputresponse["name"]
                uuid = outputresponse["id"]

                print(name)
                print(uuid)

                return uuid

asyncio.run(findUUID(username))