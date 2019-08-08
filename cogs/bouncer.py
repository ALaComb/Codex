import discord
from discord.ext import commands

class bouncer(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bouncer has entered the inn.')



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def kick(self, context, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await context.send(f'{member.mention} has been kicked.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ban(self, context, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await context.send(f'{member.mention} has been banned.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await context.guild.unban(user)
                await context.send(f'Unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(bouncer(client))