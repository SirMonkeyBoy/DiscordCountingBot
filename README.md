# DiscordCountingBot
## A discord bot that counts for ever

### How to start docker Container

all commands are run in the spot where the readme is

1. Download this git repository
2. Run
   
        docker build -t countingbot:start ./CountingBotStart/ && docker build -t countingbot:bot ./CountingBot/
4. Put all the environment verables in the compose.yml
5. Run
   
        docker compose -p counting_bot -f compose.yaml
6. Starting the counting bot Run !start if you want to start from 1 Run !start number to start form a diffrent number
   both commands have to be run where you copied the channel id from

### Compose

    version: '3.5'

    services:

     CountingBotStart:
        image: countingbot:start
        depends_on:
            - CountingBot1
            - CountingBot2
        environment:
            BOTTOKEN: 'Bot Token 1'
            COUNTSTARTNUMBER: '1'
        stdin_open: true
        tty: true
      
    CountingBot1:
        image: countingbot:bot
        environment:
            BOTTOKEN: 'Bot Token 1'
            CHANNELID: 'Channel id'
            BOTID1: 'Bot 1 user id'
            BOTID2: 'Bot 2 user id'
        stdin_open: true
        tty: true
    
    CountingBot2:
        image: countingbot:bot
        environment:
            BOTTOKEN: 'Bot Token 2'
            CHANNELID: 'Channel id'
            BOTID1: 'Bot 1 user id'
            BOTID2: 'Bot 2 user id'
        stdin_open: true
        tty: true

Bot Token 1 should be the same token<br>
Bot Token 2 should be a diffrent token to Bot Token 1<br>
Channel id is the channel you want the bot to work in<br>
Bot 1 and 2 user id is their user/bot id is not the same as bot token<br>
example id 170733454822341405
