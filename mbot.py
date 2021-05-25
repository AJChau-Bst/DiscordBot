# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import requests
import json
from discord.ext import commands
import os
import random

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
client = commands.Bot(command_prefix = '!')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Buttface is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.

with open ("thingstosend.txt", encoding='utf8') as f:
    lines = f.readlines()

@client.event
async def on_message(message):
  if message.author == client.user:
      boop = True
      return 

  if message.content.startswith('$fuckme'):
    death = (random.choice(lines))
    await message.channel.send(death)

  if 'disable' in message.content.lower():
      boop = False
      await message.channel.send("boop disabled")
  if 'enable' in message.content.lower():
      boop = True
      await message.channel.send("boop enabled")

  if message.author.id == (558783890576375819):
      ew = random.randint(1,10)
      if ew == 1:
        await message.channel.send ("weeb.")
  if message.author.id == (477180586327408641):
      ew = random.randint (1,10)
      if ew == 1:
          await message.channel.send ("Lil BEAAAAAN")
  if message.author.id == (264430261238759424):
      ew = random.randint (1,10)
      if ew == 1:
          await message.channel.send ("Space Ships!")
  if message.author.id == (240642266383777796):
      ew = random.randint (1,10)
      if ew == 1:
          await message.channel.send ("GAYYYYYYY")
  if message.author.id == (702595759022800907):
      ew = random.randint (1,10)
      if ew == 1:
          await message.channel.send ("toscana and elliot sittin in a tree...")
  if message.author.id == (543536764690890762):
          ew = random.randint(1,10)
          if ew == 1:
            await message.channel.send('"The porsche isnt even that nice, jesus fucking christ"')
    


#@client.event
#async def on_message(message):
    #if "ly" in message.content:
        #await message.channel.send('simp')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run("ODQ2NDAzNzk3OTE1MDA5MDc0.YKvA9g.q9OTJvKQnd9EO-RHUi8qj2d_HGA")
