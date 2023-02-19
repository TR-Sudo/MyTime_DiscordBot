# MyTime_DiscordBot

Mytime conversion bot is the perfect tool for anyone on Discord who needs to quickly and easily convert times to their local timezone. Simply type in a time, and the bot will display it in the viewer's local time. Whether you're coordinating events with friends in different timezones, or just need to know what time it is on the other side of the world, my time conversion bot has you covered.

# MyTime is always alive invite and prompt away!
https://discord.com/oauth2/authorize?client_id=1053567782425464863&permissions=75776&scope=bot
- Deployed on a AWS EC2 Instance

# Support
```
There are two steps to set up and use MyTime:

1.Set your default time zone by typing {>MyLocation [enter time zone]}
2.Convert the time in one time zone to your time zone [>MyTime [time (e.g. 5:00pm)] [Time zone (e.g. EST)]}
```
Without setting a default time zone
```
>TzToTz
Convert 12 Hour time
[12 Hour Time] [Previous Time Zone] [New Time Zone]
EX-> 12:00PM EST PST

Arguments:
  prevTime  [12 Hour Time]  EX->12:30PM
  prev_tz   Previous time zone
  time_zone to time zone
```
```
>TimeTo
Convert Exact Time
[time in 12hr]/[Year]/[Month]/[Day] [Previous Time zone] [Requested Time zone]
EX->12:30pm/2023/02/03 EST PST

Arguments:
  prev_time [time in 12hr]/[Year]/[Month]/[Day]
  prev_tz   Previous time zone
  time_zone to time zone   
```
# To Use
```
No Category:
  MyLocation Set your default timezone by typing {>MyLocation [enter time zone]}
  MyTime     Convert the time in one time zone to your time zone
  Setup      Guide to using this bot
  TimeTo     Convert Exact Time
  TzToTz     Convert 12 Hour time
  help       Shows this message

Type >help command for more info on a command.
You can also type >help category for more info on a category.
```
## Examples
![Screenshot 2023-02-13 203549](https://user-images.githubusercontent.com/78048789/218615669-6fbce45e-53a0-414d-9ab0-b972b47c7414.png)
![Screenshot 2023-02-13 203726](https://user-images.githubusercontent.com/78048789/218615798-16d09fa4-62eb-4af0-8cb0-7207fcab293c.png)



# With Setup
![Screenshot 2023-02-13 203830](https://user-images.githubusercontent.com/78048789/218615942-fcf464b6-e5cf-48a4-86b6-8cf24ab3843a.png)
![Screenshot 2023-02-13 203957](https://user-images.githubusercontent.com/78048789/218616138-de31575c-7be4-4b6f-826a-f041bba489fa.png)


# API
https://timezonedb.com/
<br></br>
https://discord.com/developers/docs/intro

# Database
<img src="https://miro.medium.com/max/700/1*vlaWAXinx8flFp5ZsytpGg.png"/>
