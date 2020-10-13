# bot.py

import discord
import requests
import json
import sqlite3
from discord.ext.commands import Bot
from discord.ext import commands
conn = sqlite3.connect('servers.db')
c = conn.cursor()
loading = '<:loading:747680523459231834>'

TOKEN = ('NzQxODg1MzM4NDMwOTk2NDkx.Xy-EkA.lj_crjFiN1-ghTopFFpNlYLT8gE')
loading = '<:loading:747680523459231834>'

TOKEN = ('NzUwMDI1NTAyNjk3MzI0NjEw.X00hrg.bAvlHDU-QgMt2MhLHl0G9DDn8K4')
activity = discord.Game(name="Smirf Deployed Me")


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
       await message.channel.send('Gettin ya a meme')
       r = requests.get("https://meme-api.herokuapp.com/gimme")
       json_response = r.json()
       image = json_response['postLink']
       await message.channel.send(image)
    if message.content.startswith('!tomato'):
        await message.channel.send("Potato")
    if message.content.startswith('!turtles'):
        await message.channel.send("I like turtles")
    if message.content.startswith('!lbrp);
        await message.channel.send("https://discord.gg/fXtWJcP")
<<<<<<< HEAD
    if message.content.startswith('!settingsetup'):
       await message.channel.send('Setting your server up in our database, you can delete your server from our database at any time')
       async def getguild(ctx):
          id = ctx.message.guild.id
       c.execute("INSERT INTO Settings (SERVERID) VALUES (?)",
                 (id))
       await message.channel.send('Your Server Has Been Setup')
@client.event
async def on_member_join(member):
   await member.send("Welcome to the Server my dude")
   await member.send("Let our staff know if you need anything to make this experience any better")
   await member.send("Bot Made by Smirf123#5911")

@client.event
async def on_guild_join(guild):
   print("Joined new guild")
@client.event
async def on_member_join(member):
   await member.send("Welcome to the Server my dude")
client.run(TOKEN)
