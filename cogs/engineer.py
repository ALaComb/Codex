import os

from discord.ext import commands
from discord.ext.commands import Context


class engineer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Engineer has entered the inn.')

    @commands.command()
    async def status(self, ctx: Context, cogName: str):
        ex = ctx.bot.extensions.get(f'cogs.{cogName}')
        await ctx.send(f'{ex}')

    @commands.command()
    async def branch(self, ctx):
        branch = os.popen('git symbolic-ref --short HEAD').read()
        await ctx.send(f'Codex is currently running on branch `{branch}`')


def setup(client):
    client.add_cog(engineer(client))
