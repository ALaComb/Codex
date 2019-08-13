# This is here for reference in the version controlled code.
# bot.py is the code that is running on the EC2 server.

import discord
import pymongo
import os
import logging
from discord.ext import commands

logging.basicConfig(filename=r'.\output.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

codex = commands.Bot(command_prefix='!')


@codex.event
async def on_ready():
    await codex.change_presence(status=discord.Status.online,
                                activity=discord.Game('5th Edition D&D'))
    print('Codex is ready!')
    print('---------------')
    print('Logged in as ')
    print(codex.user.name)
    print(codex.user.id)


@codex.command()
async def load(ctx, extension):
    """
    Loads a cog into the environment. Useful if a new cog is created.
    """
    codex.load_extension(f'cogs.{extension}')


@codex.command()
async def unload(ctx, extension):
    """
    Unloads a cog from the environment. Tbh, this is covered in reload.
    """
    codex.unload_extension(f'cogs.{extension}')


@codex.command()
async def reload(ctx, extension):
    """
    Reloads a single cog.
    """
    codex.unload_extension(f'cogs.{extension}')
    codex.load_extension(f'cogs.{extension}')


@codex.command()
async def reloadall(ctx):
    """
    There's no real reason to use this since !pull reloads all the cogs.
    """
    reloadcogs()
    await ctx.send(f'All content reloaded!')


@codex.command()
async def pull(ctx, branch):
    """
    Pulls code from 'development' branch and reloads all the cogs accordingly.
    """
    await ctx.send('Checking out branch...')
    os.system(f'git checkout {branch}')
    await ctx.send('Updating code...')
    os.system('git pull')
    await ctx.send('Reloading cogs...')
    reloadcogs()
    await ctx.send(f'All content reloaded!')


# Efficiency. Its used twice and written once.
def reloadcogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            if codex.extensions.get(f'cogs.{filename[:-3]}') is not None:
                codex.unload_extension(f'cogs.{filename[:-3]}')
            codex.load_extension(f'cogs.{filename[:-3]}')


# Load all the cogs on bot start.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        codex.load_extension(f'cogs.{filename[:-3]}')


db_write_conn = pymongo.MongoClient(os.environ["DATABASE_CONNECTION_WRITE"])
db_read_conn = pymongo.MongoClient(os.environ["DATABASE_CONNECTION_READ"])

# Assigned as an environment variable on the server. Can be found
#   in discordapp.com/developer for the bot.
codex.run(os.environ["CODEX_AUTH_KEY"])
