import asyncio
import discord
import random

from discord.ext import commands
from discord.ext.commands import Cog 
from datetime import datetime

from error_handler import CatchError

class StaffStuff(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.CatchError = CatchError()


    @commands.command()
    @commands.has_role("Staff")
    async def warn(self, ctx, member:discord.Member, reason):

        def check(m):
            return m.author.id == ctx.author.id

        await ctx.message.delete()

        async with ctx.typing():

            num = random.randint(0, 11)

            await asyncio.sleep(num)

        if all(i.isprintable() for i in reason.content):

            warn = discord.Embed(color= discord.Colour.red(), timestamp=datetime.datetime.utcnow(), title=f":red_circle:**__WARNING__**:red_circle:", description=f"Staff Member: {ctx.author.display_name}\nStaff member Role: {ctx.author.top_role}\nMember: {member.display_name}\nReason: {reason.content}").set_thumbnail(url=ctx.author.avatar_url)

            await member.send(embed=warn)
            channel = self.bot.get_channel()
            await channel.send(embed=warn)

            await a.delete()
            await reason.delete()

        else:

            await ctx.send("")

    @commands.command()
    @commands.has_any_role('Owner', 'Head Dev', 'Dev', 'Head Administrator', 'Admins', 'Moderators', 'Community Helpers')
    async def tempmute(self, ctx, member:discord.Member, reason, timer:int):

        await ctx.message.delete()

        async with ctx.typing():

            num = random.randint(0, 11)

            await asyncio.sleep(num)

        def check(m):
            return ctx.message.author == m.author

        channel1 = self.bot.get_channel(staff_commands)

        if ctx.message.channel == channel1:

            embed1 = discord.Embed(color=discord.Colour.red(), timestamp=self.time, title="**__A Tempmute Has Been Issued!__**", description=f"Offending Members Name: {member.top_role.name} {member.name}\nStaff Member Responsible: {ctx.author.top_role.name} {ctx.author.display_name}\nReason: {reason}\nTime Length: {timer}s", inline=False).set_thumbnail(url=self.url)
            await member.send(embed=embed1)
            channel = self.bot.get_channel(tempmutes)
            msg1 = await channel.send(embed=embed1)
            await msg1.pin()
            await channel.purge(limit=1)

            existing_role = member.top_role
            await member.remove_roles(existing_role)

            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.add_roles(role)

            await asyncio.sleep(timer)

            await member.remove_roles(role)
            await member.add_roles(existing_role)

            embed2 = discord.Embed(color=discord.Colour.green(), timestamp=self.time, title="**__YOU HAVE BEEN UNMUTED!__**", description=f"Yeet, {member.mention}! You have served your sentence! Your access has been regained within the discord :)", inline=False).set_thumbnail(url=self.url)
            await member.send(embed=embed2)
            await channel.send(embed=embed2)

        else:
            a = await ctx.send("**__You must be in the #staff_commands channel to use this command")
            await asyncio.sleep(10)
            await a.delete()

def setup(bot):
    bot.add_cog(StaffStuff(bot))