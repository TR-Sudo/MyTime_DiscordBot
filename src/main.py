import discord
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


client = discord.Client(command_prefix='#', intents=discord.Intents().all())

@client.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(client))


client.run(os.getenv('DISCORD_TOKEN'))