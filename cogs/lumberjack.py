import discord
from discord.ext import commands

class lumberjack(commands.Cog):
    def __init__(self,client):
        self.client = client

    # Event Sample
    @commands.Cog.listener()
    async def on_ready(self):
        print('lumberjack has entered the inn.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Error handling for Python errors, not discord.py errors. Those should be handled with specific error handling.
        await ctx.send(f'{error}')

def setup(client):
    client.add_cog(lumberjack(client))