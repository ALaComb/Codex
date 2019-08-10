import discord
from discord.ext import commands
from discord.ext.commands import Context, Bot


class engineer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Engineer has entered the inn.')

    @commands.command()
    async def status(self, ctx : Context, cogName : str):
        await ctx.send("lol")


def setup(client):
    client.add_cog(engineer(client))
