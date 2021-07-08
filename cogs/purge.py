import discord
from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Purge/Clear command
    @commands.command(aliases=["purge"])
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} messages have been removed!", delete_after=5)


def setup(client):
    client.add_cog(Purge(client))
