from keep_alive import keep_alive

import discord
from discord.ext import commands
# import requests
# import json
import os
import random

# client = discord.Client()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$')
# client = commands.Bot(command_prefix = "$", intents = intents)

# from apikeys import *

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$np') or message.content.startswith('$NP') or message.content.startswith('$Np') or message.content.startswith('$NP'):
        await message.channel.send('NYANPASSU!')

    elif message.content.startswith('$10'):
        for count in range(10):
          await message.channel.send('NYANPASSU!')

    elif message.content.startswith('$r') or message.content.startswith('$R'):
        rand = random.randint(1,30)
        for count in range(rand):
          await message.channel.send('NYANPASSU')

    elif message.content.startswith('$lmao'):
        for count in range(3):
          await message.channel.send('LOL!')

# @client.command(pass_context = True)
# async def join(message):
#   if (message.author.voice):
#     channel = message.author.voice.channel
#     await channel.connect()
#   else:
#     await message.channel.send("You are not in a voice channel, please be in one to run this command")
os.environ['TOKEN']
keep_alive()
client.run(os.getenv('TOKEN'))
# client.run('TOKEN')
