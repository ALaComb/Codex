import discord
import random
from discord.ext import commands

class citizen(commands.Cog):
    def __init__(self,client):
        self.client = client

    # Event Sample
    @commands.Cog.listener()
    async def on_ready(self):
        print('Citizen has entered the inn.')

    # Command Sample
    @commands.command()
    async def roll(self, context, dice="1d20"):
        num_rolls,die_size = dice.split('d')
        rolls = []
        if num_rolls == '':
            num_rolls = 1
        for i in range(int(num_rolls)):
            rolls.append(random.randrange(1,int(die_size)))

        await context.send("""``` /\\' .\\    _____
/: \\___\\  / .  /\\
\\' / . / /____/..\\
 \\/___/  \\'  '\\  /
          \\'__'\\/```"""+f'\nRolling **{num_rolls}d{die_size}**... Rolled {rolls} for a total of **{sum(rolls)}**!')


def setup(client):
    client.add_cog(citizen(client))