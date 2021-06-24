from keep_alive import keep_alive

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import youtube_dl
# import requests
# import json
import os
import random
import asyncio
import time


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

# client = discord.Client()
intents = discord.Intents.default()
intents.members = True

# client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix='$')
client = commands.Bot(command_prefix = "$", intents = intents)

# from apikeys import *

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_member_join(member):
#     channel = discord.utils.get(member.guild.channels, name='general')
#     greeting =[
#       f'Welcome {member.mention}!  to hell. Why did you even join? UwU',
#       f'Welcome {member.mention}!  You might regret it here',
#       f'Welcome {member.mention}!  Make sure you contribute to our memes',
#     ]
#     await channel.send(random.choice(f'Welcome {member.mention}!  Make sure you contribute to our memes'))
@client.event
async def on_member_join(member):
  # channel = discord.utils.get(member.guild.channels, name='sembang-santai🤡')
  greeting =[
        f'Welcome {member.mention}!  to hell. Why did you even join? UwU',
        f'Welcome {member.mention}!  You might regret it here',
        f'Welcome {member.mention}!  Make sure you contribute to our memes',
      ]
  await member.send(random.choice(greeting))
  await member.send("On a serious note, glad to have you here! We talk for fun here, play games, post memes (Please view the gambar tersumpah at your own risks). We don't post lewds or nsfw here, except for the occasional one or two memes that includes them. You can also ask programming questions here and join us in programming.")
  await member.send("Each category has their own rules. Please follow them. If you don't, the admin and mods might discuss it with you, we won't ban though. Anyways, enjoy yourselves!")
  await member.send("Also just a plug in, this bot is created by firdauskotp. If you are interested in stuff like this, you can join us in the programming portfolio or new language. Use $help in the server to find out this bot's functions")
  # await channel.send(random.choice(greeting))
  
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$np') or message.content.startswith('$NP') or message.content.startswith('$Np') or message.content.startswith('$NP'):
#         await message.channel.send('NYANPASSU!')

#     elif message.content.startswith('$10'):
#         for count in range(10):
#           await message.channel.send('NYANPASSU!')

#     elif message.content.startswith('$r') or message.content.startswith('$R'):
#         rand = random.randint(1,30)
#         await message.channel.send('NYANPASSU WILL REPEAT FOR ' + str(rand)+ " TIMES")
#         for count in range(rand):
#           await message.channel.send('NYANPASSU')

#     elif message.content.startswith('$p') or message.content.startswith('$P'):
#       if message.author.voice:
#         await message.channel.send('You are not connected to a voice channel')
        
#         return
#       else:
#         channel = message.author.voice.channel
#         await channel.connect()
  
@client.command(name="np", aliases=["nP","Np","NP"], help="Sends NYANPASSU once in current text channel")
async def np(ctx):
  await ctx.send('NYANPASSU!')

@client.command(name="10", help="Sends NYANPASSU 10 times in current text channel. NOTE: MAY LAG A BIT EACH 3-5 MESSAGES")
async def ten(ctx):
  for count in range(10):
    await ctx.send('NYANPASSU!')

@client.command(name="r", aliases=["R"], help="Sends NYANPASSU random number of times between 1 to 30 in current text channel. NOTE: MAY LAG A BIT EACH 3-5 MESSAGES")
async def r(ctx):
  rand = random.randint(1,30)
  await ctx.send('NYANPASSU WILL REPEAT FOR ' + str(rand)+ " TIMES")
  for count in range(rand):
    await ctx.send('NYANPASSU')

@client.command(name="p", aliases=["P"], help="Plays nyanpass in voice channel")
async def p(ctx):
  print("It doesn't works")
  if not ctx.message.author.voice:
      await ctx.send("You are not connected to a voice channel")
      return

  else:
      channel = ctx.message.author.voice.channel

  await channel.connect()

  server = ctx.message.guild
  voice_channel = server.voice_client

  # async with ctx.typing():
  #   player = await YTDLSource.from_url('https://www.youtube.com/watch?v=anhaSZ4aJe8', loop=client.loop)
  #   voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

  # await ctx.send('What fate have you brought upon yourself?')

  await ctx.send('What fate have you brought upon yourself?! Although the music ends, the bot will remain here, until you disconnect it,staring into you, hauntingly. ')
  player = await YTDLSource.from_url('https://www.youtube.com/watch?v=anhaSZ4aJe8', loop=client.loop)
  voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
  
  # time.sleep(300)

  # voice_client = ctx.message.guild.voice_client
  # await voice_client.disconnect()

@client.command(name='s', aliases=["S"],help='Disconnects bot from voice channel')
async def s(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='c', aliases=["C"],help='Show credits')
async def c(ctx):
    await ctx.send('Created by firdauskotp(first disc bot) with help from online resources such as freecodecamp and RK Coding. Oh also you guys from Stack Overflow ayy')
  
os.environ['TOKEN']
keep_alive()
client.run(os.getenv('TOKEN'))
# client.run('TOKEN')
