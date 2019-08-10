from discord.ext import commands


class engineer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Engineer has entered the inn.')

    @commands.command()
    async def status(self, ctx, cogName):
        ctx.send(ctx.bot.extensions)


def setup(client):
    client.add_cog(engineer(client))
