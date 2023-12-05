from asyncio import sleep
import os
import discord

client = discord.Client(intents=discord.Intents().all())

BotToken = os.environ['BOTTOKEN']
ChannelID = os.environ['CHANNELID']

@client.event
async def on_ready():
    print('Counting bot is online')


@client.event
async def on_message(message):

    if message.author.id == client.user.id:
        return

    if message.channel.id == int(ChannelID):
        string = message.content
        await sleep(1)
        try:
            counter = int(string)
            counter += 1
            await message.channel.send(counter)
            print(counter)
        except ValueError:
            # Handle the exception
            message.channel.send('Please enter an integer')
            print('Please enter an integer')


client.run(BotToken)
