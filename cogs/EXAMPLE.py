import discord
from discord.ext import commands

class EXAMPLE(commands.Cog):
    def __init__(self,client):
        self.client = client

    # Event Sample
    @commands.Cog.listener()
    async def on_ready(self):
        print('EXAMPLE has entered the inn.')

    # Command Sample
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def zzz(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(EXAMPLE(client))