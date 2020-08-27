# bot.py

import discord
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
loading = discord.emoji 

TOKEN = ('Bot Token Here')
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
       await message.channel.send('I am Smirf123#5911 creation, I am a work in progress, I can only do ping, help, meme, and rmeme Caution the rmeme is a random reddit meme and idk what it will send so it is suggested to send in nsfw channel just incase.')
    if message.content.startswith('!creator'):
       await message.channel.send('The man who created me is Smirf123#5911, he has made a few other bots but this is his fisrt one based on Python, follow him on twitch https://twitch.tv/smirf123')
    if message.content.startswith('!meme'):
       await message.channel.send('It is wednesday my dudes')
    if message.content.startswith('!rmeme'):
       await message.channel.send('Gettin ya a meme :loading:')
       r = requests.get("https://meme-api.herokuapp.com/gimme")
       json_response = r.json()
       image = json_response['postLink']
       await message.channel.send(image)
client.run(TOKEN)
