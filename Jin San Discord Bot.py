"""    
    Copyright (C) 2022 ViridianTelamon (Viridian)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import os
import time
import requests
import json

#Jin San Discord Bot.
#By:  ViridianTelamon.

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
