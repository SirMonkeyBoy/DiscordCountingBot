import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

CountStartNumber = os.environ['COUNTSTARTNUMBER']
BotToken = os.environ['BOTTOKEN']


@bot.event
async def on_ready():
    print('Start command online')


@bot.command()
async def start(ctx):
    await ctx.send(CountStartNumber)
    print('Count started')

bot.run(BotToken)
