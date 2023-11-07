import os
import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option
import pymongo

mongo_client = pymongo.MongoClient(str(os.environ.get('MONGODB_URI')))

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = mongo_client["aristotle"]

    @slash_command(
        name='add',
        description='Adds a quote to the pool for your server.'
    )
    async def add(self, ctx, quote, author):
        # Get the server's ID and create a collection name based on it
        server_id = str(ctx.guild.id)
        collection_name = f"quotes_{server_id}"

        # Access the collection and insert the document
        collection = self.db[collection_name]
        quote_document = {
            "quote": quote,
            "author": author
        }
        result = collection.insert_one(quote_document)

        if result.acknowledged:
            await ctx.respond("Quote added successfully.")
        else:
            await ctx.respond("Failed to add the quote.")

def setup(bot):
    bot.add_cog(Add(bot))
