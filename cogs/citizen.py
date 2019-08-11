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

    @commands.command()
    async def test(self,ctx):
        await ctx.send('Oh yeah!')

    # Command Sample
    ## Add kh and kl and other dice commands.
    @commands.command(aliases = ['r'])
    async def roll(self, ctx, dice="1d20+0"):
        """
        This is the roll command!
        """
        num_rolls,die_size = dice.split('d')
        r_mod = 0
        if '+' in die_size:
            die_size,r_mod = die_size.split('+')
            r_mod = int(r_mod)
        elif '-' in die_size:
            die_size,r_mod = die_size.split('-')
            r_mod = int(r_mod) * -1
        rolls = []
        if num_rolls == '':
            num_rolls = 1
        for i in range(int(num_rolls)):
            rolls.append(random.randrange(1,int(die_size)))

        await ctx.send("""``` /\\' .\\    _____
/: \\___\\  / .  /\\
\\' / . / /____/..\\
 \\/___/  \\'  '\\  /
          \\'__'\\/```"""+f'\nRolling **{dice}**... Rolled {rolls} for a total of **{sum(rolls)+r_mod}**!')


def setup(client):
    client.add_cog(citizen(client))