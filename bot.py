# bot.py

import discord
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
loading = discord.emoji 

TOKEN = ('Token Here')
activity = discord.Game(name="Smirf Made Me")


client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
       await message.channel.send('pong')
    if message.content.startswith('Im'):
       await message.channel.send("Hi Im dad")
    if message.content.startswith('!help'):
       await message.channel.send('I am Smirf123#5911 creation, I am a work in progress, I can only do Ping, and Help atm but will be updated in the future')
    if message.content.startswith('!creator'):
       await message.channel.send('The man who created me is Smirf123#5911, he has made a few other bots but this is his fisrt one based on Python, follow him on twitch https://twitch.tv/smirf123')
    if message.content.startswith('!meme'):
       await message.channel.send('It is wednesday my dudes')
    if message.content.startswith('!random'):
       await message.channel.send('Gettin ya a meme :loading:')
       response = requests.get("https://some-random-api.ml/meme")
       results = (response[0]['image'])
       await message.channel.send(results)
client.run(TOKEN)
