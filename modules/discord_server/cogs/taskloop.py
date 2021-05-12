import json
import discord
import os
import logging

from discord.ext import commands, tasks
from discord.ext.commands import Cog 
from datetime import datetime

with open('./modules/discord_server/json_files/master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

guild_id = data["guild"]["id"]

class TasksLoops(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @tasks.loop(minutes=10)
    async def save_chat(self, ctx, message):

        logger = logging.getLogger('KasMekLLC-Discord Bot Error')
        logger.setLevel(logging.ERROR)
        path = os.path.exists(f'./modules/discord_server/errors/{datetime.today()}')

        fh = logging.FileHandler(path)
        fh.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s = %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        logger.addhandler(fh)

        with open('./modules/discord_server/json_files/message.json', 'r', encoding='utf-8-sig') as current:
            data = json.load(current)

        guild = self.bot.get_guild(guild_id)

        count = 0

        try:

            while count < 5000:

                for message in guild.text_channels:

                    ctx.author = ctx.message.author.name

                    data[datetime.today().__format__('%m_%d_%y_%H:%M:%S')] = {{str(message.author.name)} : {message.content}}

                    with open('./modules/discord_server/json_files/message.json', 'r', encoding='utf-8-sig') as new:
                        data = json.dump(data, new, indent=4)
            
            else:

                pass

        except ValueError as e:

            logger.exception(e)