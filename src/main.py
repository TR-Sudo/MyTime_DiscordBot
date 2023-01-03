import discord
from discord.ext import commands
import os
from datetime import datetime
from api_req import res
from unixtime import conToUnixTime
from unixtime import con12TimeToUnix
from dynamobd_user_store import add_user
from dynamobd_user_store import get_user
from valid_time_zone import check_time_zone
INC_TIME_ZONE="Enter a valid time zone abbreviation,follow url for assistance https://www.timeanddate.com/time/zones/"

bot = commands.Bot(command_prefix='>', intents=discord.Intents().all())

@bot.event
async def on_ready():
    print('MyTime Bot active and running as {0.user}'.format(bot))


@bot.command(name='Setup',help="Guide to using this bot\nThere are two steps to set up and use MyTime:\n\n1.Set your default timezone by typing {>MyLocation [enter timezone]}\n2.Convert the time in one time zone to your time zone [>MyTime [time (e.g. 5:00pm)] [Timezone (e.g. EST)]}\n\nWithout setting a default timezone\n3.{#TimeTo [Type >help TimeTo for description]}\n4.{#TzToTz [Type >help TzToTz for description]}")
async def sendHelp(ctx):
    if ctx.message.author==bot.user:
        return 
    await ctx.send()

@bot.command(name='TimeTo',help="Convert Exact Time\nInput [time in 12hr]/[Year]/[Month]/[Day] [Previous Timezone] [Requested Timezone]\nEX->12:30pm/2023/02/03 EST PST")
async def converTime(ctx,prev_time: str = commands.parameter(description="[time in 12hr]/[Year]/[Month]/[Day]"),prev_tz: str=commands.parameter(description="Previous time zone"),time_zone: str =commands.parameter(description="to time zone")):
    unixTime=(conToUnixTime(prev_time))
    prev_tz=prev_tz.upper()
    time_zone=time_zone.upper()    

    if(check_time_zone(prev_tz) and check_time_zone(time_zone)):
        await ctx.send(datetime.fromtimestamp(res(unixTime,prev_tz,time_zone)).strftime('%Y-%m-%d %I:%M %p'))
    else:
        await ctx.send(INC_TIME_ZONE)

@bot.command(name="TzToTz",help="Convert 12 Hour time to different time zones\n[12 Hour Time] [Previous Time Zone] [New Time Zone]\nEX-> 12:00PM EST PST")
async def conver12Time(ctx,prevTime: str = commands.parameter(description="[12 Hour Time] -> EX.12:30PM"),prev_tz: str=commands.parameter(description="Previous time zone"),time_zone: str =commands.parameter(description="to time zone")):
    unixTime=(con12TimeToUnix(prevTime))
    prev_tz=prev_tz.upper()
    time_zone=time_zone.upper()    

    if(check_time_zone(prev_tz) and check_time_zone(time_zone)):
        await ctx.send(datetime.fromtimestamp(res(unixTime,prev_tz,time_zone)).strftime('%I:%M %p'))
    else:
        await ctx.send(INC_TIME_ZONE)

@bot.command(name="MyLocation",help="Set your default timezone by typing {>MyLocation [enter timezone]}")
async def setTz(ctx,time_zone):
    time_zone=time_zone.upper()

    if(check_time_zone(time_zone)):
        await add_user(ctx,ctx.message.author,time_zone)
    else:
        await ctx.send(INC_TIME_ZONE)

@bot.command(name="MyTime",help="Convert the time in one time zone to your time zone [>MyTime [time (e.g. 5:00pm)] [Timezone (e.g. EST)]}")
async def get_tz(ctx,prev_time,time_zone):
    unixTime=(con12TimeToUnix(prev_time))
    time_zone=time_zone.upper()
    
    if(check_time_zone(time_zone)):
        response=await get_user(ctx,ctx.message.author)
        if response=="User needs to be added, Enter [>help MyLocation] for assistance":
            await ctx.send("User needs to be added, Enter [>help MyLocation] for assistance")
        else:
            await ctx.send(datetime.fromtimestamp(res(unixTime,response,time_zone)).strftime('%I:%M %p'))
    else:
        await ctx.send(INC_TIME_ZONE)

#Todo: add MyTime by getting users time zone value
bot.run(os.getenv('DISCORD_TOKEN'))