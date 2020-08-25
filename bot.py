# bot.py
import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands
activity = discord.Game(name="Smirf Made Me")

TOKEN = 'No Token 4 U'

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
client.run(TOKEN)
