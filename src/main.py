import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(client))


client.run(os.getenv('TOKEN'))