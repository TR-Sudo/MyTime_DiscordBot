import discord
import os
import requests
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

API_URL="http://api.timezonedb.com/v2.1/convert-time-zone"

payload={KEos.getenv('API_KEY'),}
res=requests.get()

client = discord.Client(command_prefix='#', intents=discord.Intents().all())

@client.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('#help'):
        await message.channel.send("There are two steps to set up and use this tool:\n\n1.Set your default timezone by typing {#MyLocation [enter timezone]}\n2.Convert the time in one timezone to another by typing {#MyTime [time (e.g. 5:00pm)] [Timezone (e.g. EST)]}\n\nWithout setting a default timezone\n3.{#TimeTo [time] EST to [Timezone (e.g. PST)]}")


client.run(os.getenv('DISCORD_TOKEN'))