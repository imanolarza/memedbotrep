import discord
from discord.ext import commands

from flask_web import keep_alive

from datetime import datetime
import logging
import os


_logger = logging.getLogger(__name__)

bot = commands.Bot(command_prefix='m!', case_insensitive=True)

# Global Variables (temporal)
snipe = False
uptime = False

@bot.event
async def on_ready():
    global uptime
    print('listo!')

@bot.event
async def on_message_delete(message):
    global snipe

    if message.author.bot == False:
        snipe = message

@bot.command()
async def snipe(ctx):
    embed = discord.Embed(
        colour=discord.Colour.purple(),
        description=snipe.content
    )
    embed.set_author(name=snipe.author, icon_url=snipe.author.avatar_url)
    embed.timestamp = snipe.created_at

    await ctx.send(embed=embed) 

if __name__ == "__main__":
    token = os.environ.get('DISCORD_TOKEN')
    keep_alive()
    bot.run(token)
