import os
import discord
from discord.ext import commands, tasks
from discord.commands import slash_command, Option
import pymongo
import random

mongo_client = pymongo.MongoClient(str(os.environ.get('MONGODB_URI')))

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = mongo_client["aristotle"]

    @slash_command(
        name='random',
        description='Gets a random quote from your server\'s pool.'
    )
    async def random(self, ctx):
        # Get the server's ID and create a collection name based on it
        server_id = str(ctx.guild.id)
        collection_name = f"quotes_{server_id}"

        # Access the collection and retrieve a random quote
        collection = self.db[collection_name]
        quotes = collection.find({}, {"_id": False})

        random_quote = random.choice(list(quotes))

        if random_quote:
            quote_text = random_quote.get("quote", "No quotes available.")
            author = random_quote.get("author", "Unknown")
            await ctx.respond(f'"{quote_text}" - {author}')
        else:
            await ctx.respond("No quotes available for this server.")

def setup(bot):
    bot.add_cog(Random(bot))
