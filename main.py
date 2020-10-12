import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json
import asyncio

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
    bot.load_extension('cogs.tickets')




bot.run("TOKEN")
