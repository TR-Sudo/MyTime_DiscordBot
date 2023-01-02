import discord
from discord.ext import commands
import os
from datetime import datetime
from api_req import res
from unixtime import conToUnixTime
from unixtime import con12TimeToUnix

bot = commands.Bot(command_prefix='>', intents=discord.Intents().all())

@bot.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(bot))


@bot.command(name='Setup',help="Guide to using this bot\nThere are two steps to set up and use MyTime:\n\n1.Set your default timezone by typing {>MyLocation [enter timezone]}\n2.Convert the time in one timezone to another by typing {>MyTime [time (e.g. 5:00pm)] [Timezone (e.g. EST)]}\n\nWithout setting a default timezone\n3.{#TimeTo [Type >help TimeTo for description]}\n4.{#TzToTz [Type >help TzToTz for description]}")
async def sendHelp(ctx):
    await ctx.send()

@bot.command(name='TimeTo',help="Convert Exact Time\nInput [time in 12hr]/[Year]/[Month]/[Day] [Previous Timezone] [Requested Timezone]\nEX->12:30pm/2023/02/03 EST PST")
async def converTime(ctx,prevTime: str = commands.parameter(description="[time in 12hr]/[Year]/[Month]/[Day]"),prevTZ: str=commands.parameter(description="Previous time zone"),TZ: str =commands.parameter(description="to time zone")):
    unixTime=(conToUnixTime(prevTime))
    await ctx.send(datetime.fromtimestamp(res(unixTime,prevTZ,TZ)).strftime('%Y-%m-%d %I:%M %p'))

@bot.command(name="TzToTz",help="Convert 12 Hour time to different time zones\n[12 Hour Time] [Previous Time Zone] [New Time Zone]\nEX-> 12:00PM EST PST")
async def conver12Time(ctx,prevTime: str = commands.parameter(description="[12 Hour Time] -> EX.12:30PM"),prevTZ: str=commands.parameter(description="Previous time zone"),TZ: str =commands.parameter(description="to time zone")):
    unixTime=(con12TimeToUnix(prevTime))
    await ctx.send(datetime.fromtimestamp(res(unixTime,prevTZ,TZ)).strftime('%I:%M %p'))

##Todo: Implement database to write author name and time zone 
@bot.command(name="MyLocation",help="Set your default timezone")
async def setTz(ctx,timezone):
    await ctx.send(f'{ctx.message.author}{timezone}')

bot.run(os.getenv('DISCORD_TOKEN'))