# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import requests
import json
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
client = commands.Bot(command_prefix = '!')
#to do 5/25: 24/7 online, RNG, more insults, alarm bot
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

with open ("thingstosend.txt", encoding='utf8') as f:
    lines = f.readlines()

@client.event
async def on_message(message):
<<<<<<< Updated upstream
    #boop == True
=======
    # boop == True
>>>>>>> Stashed changes
    if message.author == client.user:
      return
    if message.content.startswith('$fuckme'):
        death = (random.choice(lines))
        await message.channel.send(death)
<<<<<<< Updated upstream
    if message.content.startswith('$fuckwhat'):
      await message.channel.send("*$fuckme -- shitty pickup lines\n" + "$fuckwhat -- about the bot\n" + "$enable + $disable -- turn on/off the insults*")
    # if '$disable' in message.content.lower():
    #   boop = False
    #   await message.channel.send("boop disabled")
    # if '$enable' in message.content.lower():
    #   boop = True
    #   await message.channel.send("boop enabled")
    # if boop == True:
    #   if message.author.id == (477180586327408641):
    #       ew = random.randint (1,10)
    #       if ew == 1:
    #           await message.channel.send ("Lil BEAAAAAN")
    #   if message.author.id == (264430261238759424):
    #       ew = random.randint (1,10)
    #       insultnumber = random.randint(1,10)
    #       if ew == 1:
    #           if insultnumber == 1:
    #               await message.channel.send ("Space Ships!")
    #           if insultnumber == 2:
    #                 await message.channel.send ("salmon.")
    #   if message.author.id == (240642266383777796):
    #       ew = random.randint (1,10)
    #       if ew == 1:
    #           await message.channel.send ("GAYYYYYYY")
    #   if message.author.id == (702595759022800907):
    #       ew = random.randint (1,10)
    #       if ew == 1:
    #           await message.channel.send ("toscana and elliot sittin in a tree...")
    #   if message.author.id == (543536764690890762):
    #       ew = random.randint(1,10)
    #       if ew == 1:
    #           await message.channel.send('"The porsche isnt even that nice, jesus fucking christ"')
    #   if message.author.id == (558783890576375819):
    #       ew = random.randint(1,10)
    #       if ew == 1:
    #           await message.channel.send ("weeb.")
    #   if message.author.id == (355880585186770945):
    #       ew = random.randint (1,20)
    #       if ew == 1:
    #           await message.channel.send ("God.")
    #   if message.author.id == (714717355887820830):
    #       ew = random.randint (1,10)
    #       if ew == 1:
    #           insultnumber = random.randint (1,3)
    #           if insultnumber == 1:
    #               await message.channel.send ("Dingus")
    #           if insultnumber == 2:
    #               await message.channel.send ("John John John John John John")
    #           else:
    #               await message.channel.send ("You are small god.")

    #   #if
=======
#     if message.content.startswith('$fuckwhat'):
#       await message.channel.send("*$fuckme -- shitty pickup lines\n" + "$fuckwhat -- about the bot\n" + "$enable + $disable -- turn on/off the insults*")
#     if '$disable' in message.content.lower():
#       boop = False
#       await message.channel.send("boop disabled")
#     if '$enable' in message.content.lower():
#       boop = True
#       await message.channel.send("boop enabled")
#     if boop == True:
#       if message.author.id == (477180586327408641):
#           ew = random.randint (1,10)
#           if ew == 1:
#               await message.channel.send ("Lil BEAAAAAN")
#       if message.author.id == (264430261238759424):
#           ew = random.randint (1,10)
#           insultnumber = random.randint(1,10)
#           if ew == 1:
#               if insultnumber == 1:
#                   await message.channel.send ("Space Ships!")
#               if insultnumber == 2:
#                     await message.channel.send ("salmon.")
#       if message.author.id == (240642266383777796):
#           ew = random.randint (1,10)
#           if ew == 1:
#               await message.channel.send ("GAYYYYYYY")
#       if message.author.id == (702595759022800907):
#           ew = random.randint (1,10)
#           if ew == 1:
#               await message.channel.send ("toscana and elliot sittin in a tree...")
#       if message.author.id == (543536764690890762):
#           ew = random.randint(1,10)
#           if ew == 1:
#               await message.channel.send('"The porsche isnt even that nice, jesus fucking christ"')
#       if message.author.id == (558783890576375819):
#           ew = random.randint(1,10)
#           if ew == 1:
#               await message.channel.send ("weeb.")
#       if message.author.id == (355880585186770945):
#           ew = random.randint (1,20)
#           if ew == 1:
#               await message.channel.send ("God.")
#       if message.author.id == (714717355887820830):
#           ew = random.randint (1,10)
#           if ew == 1:
#               insultnumber = random.randint (1,3)
#               if insultnumber == 1:
#                   await message.channel.send ("Dingus")
#               if insultnumber == 2:
#                   await message.channel.send ("John John John John John John")
#               else:
#                   await message.channel.send ("You are small god.")

#       #if
>>>>>>> Stashed changes
        
    

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run("ODQ2NDAzNzk3OTE1MDA5MDc0.YKvA9g.q9OTJvKQnd9EO-RHUi8qj2d_HGA")

            
      #if message.content.startswith('$rng'):
          #if message.content == int:
              #x = message.content
              #exput = random.randint (1, int(x))