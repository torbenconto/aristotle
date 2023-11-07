import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(
        name='random',
        description='Gets a random quote from your servers pool.'
    )
    async def random(self, ctx):
        # fetch random quote
        await ctx.respond("test")
    
    

def setup(bot):
    bot.add_cog(Random(bot))