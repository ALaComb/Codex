import random
from discord.ext import commands


class soothsayer(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Event Sample
    @commands.Cog.listener()
    async def on_ready(self):
        print('Soothsayer has entered the inn.')

    # Command Sample
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        """
        Answers your dark queries. Can see into the future, be careful.
        """
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'Question: {question}\n' +
                       f'Answer: {random.choice(responses)}')


def setup(client):
    client.add_cog(soothsayer(client))
