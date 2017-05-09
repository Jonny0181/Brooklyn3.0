import os
import re
import json
import time
import asyncio
import discord
import datetime
from utils import checks
from discord.ext import commands
from random import choice as randchoice

description = "Brooklyn - A multi function discord bot. Now using the discord.py rewrite."
prefix = ["b!", "B!", "<@226132382846156800>", "<@!226132382846156800>"]
shardid = 1
shardcount = 2
bot = commands.Bot(command_prefix=prefix, description=description, shard_id=shardid, shard_count=shardcount)
bot.pm_help = None
wrap = "```py\n{}\n```"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for extension in modules:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

@bot.command(description="Evaluates code.", hidden=True, pass_context=True)
@checks.is_owner()
async def debug(ctx, *, code: str):
    try:
        result = eval(code)
        if code.lower().startswith("print"):
            result
        elif asyncio.iscoroutine(result):
            await result
        else:
            await ctx.send(wrap.format(result))
    except Exception as e:
        await ctx.send(wrap.format(type(e).__name__ + ': ' + str(e)))

bot.run("token")
