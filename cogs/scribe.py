import datetime
import discord
from discord.ext import commands

class scribe(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Scribe has entered the inn.')

    # Add database logging.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        mydb = db_write_conn["logbook"]
        newcol = mydb["userlog"]
        newcol.addrow({"name": member, "auditdate": datetime.datetime.today(), "status":"join"})
        print(f'{member} has joined a server.')

    # Add database logging.
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')



def setup(client):
    client.add_cog(scribe(client))