import discord
from discord.ext import commands
from discord.ext.commands import ExtensionError
import random
from discord.ext import commands


class Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready 😎")

    # Commands
    @commands.command()
    async def kek(self, ctx):
        await ctx.send('poggers')

    # 8 Ball Command
    @commands.command(aliases=["8ball", "eightball", "ball"])
    async def _8ball(self, ctx):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes, definitely",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f"{random.choice(responses)}")


def setup(client):
    client.add_cog(Cog(client))
