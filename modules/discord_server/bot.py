import asyncio
import datetime
import discord
import json
import os
import sys

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

with open('./master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

TOKEN = data["guild"]["TOKEN"]
LT = data["guild"]["LT"]
cp = data["guild"]["command_prefix"]
bot_spam = data["channels"]["bot_spam1"]
warnings = data["channels"]["warnings"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=cp, intents=intents)

@bot.event
async def on_ready():
    await load_cog()
        
def restart_program():

    python = sys.executable
    os.execl(python, python, * sys.argv)

async def load_cog():

    cogs = ["cogs.error_handler", "cogs.staff", "cogs.taskloop"]
    channel3 = bot.get_channel(bot_spam)
    for cog in cogs:    
        try:
            m = await channel3.send(f"{cog} loaded")
            print(f"{cog} loaded")
            bot.load_extension(cog)
            await asyncio.sleep(1)
            await m.delete()
        except:
            x = await channel3.send(f"{cog} reloaded")
            print(f"{cog} reloaded")
            bot.reload_extension(cog)
            await asyncio.sleep(1)
            await x.delete()

    y = await channel3.send("All Cogs Loaded")
    await asyncio.sleep(1)
    await y.delete()
    print("online")

@bot.command()
@commands.has_any_role('Owner', 'Head Dev')
async def update(ctx):

    await restart_program()

@bot.listen('on_message')
async def bprefix(message):
    if message.content.startswith("bprefix"):
        msg = await message.channel.send(f"my prefix is `{cp}`")
        await asyncio.sleep(10)
        await msg.delete()

@bot.event
async def on_message(message):

    member = message.author

    if not message.author.bot:

        with open('./filter.json', 'r', encoding='utf-8-sig') as filtered_list:
            json.load(filtered_list)

        filtered_words = data["filtered_list"]

        for word in filtered_words:
            
            if word in message.content:

                await message.delete()
                a = await message.channel.send(f":red_circle: That word(s) is/are not allowed in this discord!, {member.mention}! Try Again! :red_circle:")
                warning = discord.Embed(color=discord.Colour.red(), timestamp=datetime.datetime.utcnow(), title=f"{member.name}", description=f"**__Offending Content:__**\n{message.content}")
                channel = bot.get_channel(warnings)
                await channel.send(embed=warning)
                await asyncio.sleep(10)
                await a.delete()

    with open('./members.json', 'r', encoding='utf-8-sig') as old:
        data = json.load(old)

    if not message.author.bot:

        current = data["members"][str(message.author.name)]["warnings"]
        current += 0.05

        with open('./members.json', 'w', encoding='utf-8-sig') as new:
            data = json.dump(data, current, indent=4)

    await bot.process_commands(message)

    @bot.event
    async def message_deleted(self, message):

        with open('./modules/discord_server/json_files/deleted_messages.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            
        data["deleted_messages"] = {f'message: {message.content()} by {message.author} was deleted in {message.channel}'}

        with open('./modules/discord_server/json_files/deleted_message.json', 'w', encoding='utf-8-sig') as g:
            data = json.dump(data, new, indent=4)
        
bot.run(TOKEN)