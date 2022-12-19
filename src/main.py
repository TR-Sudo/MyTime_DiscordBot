import discord
from discord.ext import commands
import os
from api_req import res
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

@bot.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(bot))


@bot.command(name='Setup',help="Guide to using this bot")
async def sendHelp(ctx):
    await ctx.send("There are two steps to set up and use MyTime:\n\n1.Set your default timezone by typing {#MyLocation [enter timezone]}\n2.Convert the time in one timezone to another by typing {#MyTime [time (e.g. 5:00pm)] [Timezone (e.g. EST)]}\n\nWithout setting a default timezone\n3.{#TimeTo [time] EST to [Timezone (e.g. PST)]}")

bot.run(os.getenv('DISCORD_TOKEN'))