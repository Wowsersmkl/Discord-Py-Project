# bot.py
import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands
activity = discord.Game(name="Smirf Made Me")
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


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
       await message.channel.send('Hi +ctx.message.author.mention, Im dad')
    if message.content.startswith('!help'):
       await message.channel.send('I am Smirf123#5911 creation, I am a work in progress, I can only do Ping, and Help atm but will be updated in the future')
    if message.content.startswith('!creator'):
       await message.channel.send('The man who created me is Smirf123#5911, he has made a few other bots but this is his fisrt one based on Python, follow him on twitch https://twitch.tv/smirf123')
client.run(TOKEN)
