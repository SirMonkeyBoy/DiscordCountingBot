# DiscordCountingBot
## A discord bot that counts for ever

## Buld commands 
Run where the readme file is

docker build -t countstart ./CountingBotStart/<br>
docker build -t countingbot ./CountingBot/

## Compose

    version: '3.5'

    services:

     CountingBotStart:
        image: countstart
        environment:
            BOTTOKEN: 'Bot Token 1'
            COUNTSTARTNUMBER: '1'
        stdin_open: true
        tty: true
      
    CountingBot1:
        image: countingbot
        environment:
            BOTTOKEN: 'Bot Token 1'
            CHANNELID: 'Channel id'
        stdin_open: true
        tty: true
    
    CountingBot2:
        image: countingbot
        environment:
            BOTTOKEN: 'Bot Token 2'
            CHANNELID: 'Channel id'
        stdin_open: true
        tty: true

Bot Token 1 should be the same token<br>
Bot Token 2 should be a diffrent token to Bot Token 1<br>
Channel id is the channel you want the bot to work in

## Starting the bot

In the channel you copyed the channel id from type !start but make sure you or anyone else don't send a message with a number in the same channel or the bot will double the messages per second each second and then will crash i will try and fix this in a later version
