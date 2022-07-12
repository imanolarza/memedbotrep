import discord
from discord.ext import commands

from flask_web import keep_alive

from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import os


_logger = logging.getLogger(__name__)

bot = commands.Bot(command_prefix='m!!', case_insensitive=True)

# Global Variables (temporal)
snipe = False
uptime = False

@bot.event
async def on_ready():
    global uptime

    uptime = datetime.today()

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

@bot.command()
async def uptime(ctx):
    today = datetime.now()
    delta = relativedelta(today, uptime)

    dates = [
        [delta.years, 'año' if delta.years == 1 else 'años'],
        [delta.months, 'mes' if delta.months == 1 else 'meses'],
        [delta.hours, 'día' if delta.hours == 1 else 'horas'],
        [delta.minutes, 'minuto' if delta.minutes == 1 else 'minutos'],
        [delta.seconds, 'segundo' if delta.seconds == 1 else 'segundos'],
    ]
    res = []
    for d in dates:
        if d[0] != 0:
            res.append('%s %s' % (d[0],d[1]))

    await ctx.send(', '.join(res))


if __name__ == "__main__":
    token = os.environ.get('DISCORD_TOKEN')
    keep_alive()
    bot.run(token)
