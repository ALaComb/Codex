import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner has entered the inn.')

    @commands.command()
    async def ping(self, ctx):
        """
        Shows latency between messages sent to the server and the bot's response.
        """
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    # @commands.command()
    # async def load(self, ctx, extension):
    #     self.client.load_extension(f'cogs.{extension}')

    # @commands.command()
    # async def unload(self, ctx, extension):
    #     self.client.unload_extension(f'cogs.{extension}')

    # @commands.command()
    # async def reload(self, ctx, extension):
    #     self.client.unload_extension(f'cogs.{extension}')
    #     self.client.load_extension(f'cogs.{extension}')

    @commands.command(aliases = ['cleanup', 'wipedown'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """
        Deletes the last 5 messages in the current channel, or however many you specify.
        """
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(owner(client))