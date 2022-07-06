import discord
import os
import time
import requests
import json

#Jin San Discord Bot.
#By:  ViridianTelamon

client = discord.Client()

token = "Put Discord Bot Token Here."

#Get Quote Event.
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -"+json_data[0]["a"]
  return(quote)

#On Ready Event.
@client.event
async def on_ready():
  print("Bot Ready.")
  time.sleep(1)
  print("Logged In As:  {0.user}".format(client))

#If The Bot Recieves A Message Event.
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(":quote"):
    quote = get_quote()
    await message.channel.send(quote)

client.run(token)
