import discord
from discord.ext import commands
import traceback


class CatchError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.traceback = False

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            else:
                embed = discord.Embed(title=f'Error in {ctx.command}',
                                      description=f"'{ctx.command.qualified_name} {ctx.command.signature}' \n {error}",
                                      colour=discord.Colour.red())
                if self.traceback:
                    trace = traceback.format_exc()
                    embed.add_field(name='Full Traceback', value=trace)
                await ctx.send(embed=embed)
        except Exception:                
            embed = discord.Embed(title=f'Error in {ctx.command}', description=error,
                                  colour=discord.Colour.red())
            if self.traceback:
                trace = traceback.format_exc()
                embed.add_field(name='Full Traceback', value=trace)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CatchError(bot))