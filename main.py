import discord
import random
from bot_token import token
from discord.ext import commands
import os

intents = discord.Intents.all()
Quj = commands.Bot(command_prefix="?", intents=intents, case_insensitive=True)


# Load Cogs
@Quj.command()
async def load(ctx, extension):
    Quj.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded!")


# Unload Cogs
@Quj.command()
async def unload(ctx, extension):
    Quj.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded!")


# Reload Cogs
@Quj.command()
async def reload(ctx, extension):
    Quj.unload_extension(f"cogs.{extension}")
    Quj.load_extension(f"cogs.{extension}")
    await ctx.send("Reloaded!")


# Checks cogs folder for .py files and loads them
for i in os.listdir("./cogs"):
    if i.endswith(".py"):
        Quj.load_extension(f"cogs.{i[:-3]}")


# Test Ig
@Quj.command()
async def commands(ctx):
    await ctx.send("Go fuck yourself.")


Quj.run(token)
