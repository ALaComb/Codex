from discord.ext import commands
from discord.ext.commands import Context, Bot


class engineer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Engineer has entered the inn.')

    @commands.command()
    async def status(self, ctx: Context, cogName: str):
        bot: Bot = ctx.bot
        stat=''
        if bot.extensions.get(cogName) is None:
            stat='not '
        ctx.send(f'Cog {cogName} is {stat}loaded')


def setup(client):
    client.add_cog(engineer(client))
