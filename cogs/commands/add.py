import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(
        name='add',
        description='Adds a quote to the pool for your server.'
    )
    async def add(self, ctx, quote, author):
        # add to pool
        await ctx.respond(quote + " " + author)
    
    

def setup(bot):
    bot.add_cog(Add(bot))