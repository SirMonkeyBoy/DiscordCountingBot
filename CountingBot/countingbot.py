from asyncio import sleep
import os
import discord

client = discord.Client(intents=discord.Intents().all())

BotToken = os.environ['BOTTOKEN']
ChannelId = os.environ['CHANNELID']
BotId1 = os.environ['BOTID1']
BotId2 = os.environ['BOTID2']


@client.event
async def on_ready():
    print('Counting bot is online')


@client.event
async def on_message(message):

    if message.author.id == client.user.id:
        return

    if message.author.id == int(BotId1):
        if message.channel.id == int(ChannelId):
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
    else:
        if message.author.id == int(BotId2):
            if message.channel.id == int(ChannelId):
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

