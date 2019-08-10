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
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        """
        Kick a member from the server.
        """
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        """
        Ban a member from the server. This is permanent, until revoked.
        """
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, *, member):
        """
        Unban a member that has been previously banned.
        """
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(bouncer(client))