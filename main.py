import discord
from discord.errors import PrivilegedIntentsRequired
from discord.ext import commands, tasks
import os
from discord import Intents, Bot
from keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot=discord.Bot(intents=intents)

for ext in ['cogs.commands.add', 'cogs.commands.random', 'cogs.commands.list']:
    bot.load_extension(ext)

keep_alive()
bot.run(str(os.environ.get('TOKEN')))