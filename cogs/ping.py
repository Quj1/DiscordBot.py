import discord
from discord.ext import commands


class Latency(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Latency Command
    @commands.command()
    async def ping(self, ctx,):
        await ctx.send(f"Ping: {int(self.client.latency * 1000)} ms")


def setup(client):
    client.add_cog(Latency(client))
