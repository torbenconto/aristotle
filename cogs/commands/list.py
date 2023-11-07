import os
import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option
import pymongo

mongo_client = pymongo.MongoClient(str(os.environ.get('MONGODB_URI')))

class ListQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = mongo_client["aristotle"]

    @slash_command(
        name='list',
        description='Lists all the quotes in the server\'s pool.'
    )
    async def list_quotes(self, ctx):
        # Get the server's ID and create a collection name based on it
        server_id = str(ctx.guild.id)
        collection_name = f"quotes_{server_id}"

        # Access the collection and retrieve all the quotes
        collection = self.db[collection_name]
        quotes = collection.find({}, {"_id": False})

        # Create a formatted list of quotes
        quote_list = "\n".join([f'"{quote.get("quote", "No quote")}" - {quote.get("author", "Unknown")}' for quote in quotes])

        if quote_list:
            await ctx.respond(f'List of quotes for this server:\n{quote_list}')
        else:
            await ctx.respond("No quotes available for this server.")

def setup(bot):
    bot.add_cog(ListQuotes(bot))
