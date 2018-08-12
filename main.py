import discord
import asyncio
import youtube_dl
import random
import time
from discord.ext import commands
role = ['Mafia', 'Jester', 'Town', 'Investigator', 'Doctor', 'Town']
random.shuffle(role)
token = 'NDc3MTQ3MDMyODM5MjU4MTIz.Dk35lQ.aoX7HaD0bGKLifNQp7n82ZKbXoM'
client = commands.Bot(command_prefix = '~')

player1 = ''
player2 = ''
player3 = ''
player4 = ''
player5 = ''
player6 = ''
dead = ''
saved = ''



players = {}

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Murder Mystery'))
    print('Bot is ready')


@client.event
async def on_message(message):
    channel = message.author
    if message.content.startswith('~role'):
        try:
            await client.send_message(channel, role.pop())
        except IndexError:
            await client.send_message(channel, 'All roles have been handed out.')
    await client.process_commands(message)

@client.command()
async def reset():
    await client.say('Roles have been reset!')
    role = ['Mafia', 'Jester', 'Town', 'Investigator', 'Doctor', 'Town']
    random.shuffle(role)
    print(role)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    
@client.command(pass_context=True)
async def kill(ctx, *args, amount=2):
    dead = ''
    await client.say('....')
    global dead
    for word in args:
        dead += word
        dead += ' '
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('He has been killed.')
    print(dead)

@client.command()
async def set(arg1, arg2):
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    print(arg2)
    print(arg1)
    if arg1 == "player1":
        player1 = arg2
    elif arg1 == "player2":
        player2 = arg2
    elif arg1 == "player3":
        player3 = arg2
    elif arg1 == "player4":
        player4 = arg2
    elif arg1 == "player5":
        player5 = arg2
    elif arg1 == "player6":
        player6 = arg2
    else:
        await client.say('That is not a valid person.')

@client.command(pass_context=True)
async def inves(ctx, *args, amount=2):
    await client.say('....')
    member = ctx.message.author
    channel = member
    inves = ''
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    for word in args:
        inves += word
    if inves == "player1":
        await client.send_message(channel, player1)
    elif inves == "player2":
        await client.send_message(channel, player2)
    elif inves == "player3":
        await client.send_message(channel, player3)
    elif inves == "player4":
        await client.send_message(channel, player4)
    elif inves == "player5":
        await client.send_message(channel, player5)
    elif inves == "player6":
        await client.send_message(channel, player6)
    messages = []
    channel1 = ctx.message.channel
    async for message in client.logs_from(channel1, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('The results have been sent to you.')
    print(inves)

@client.command(pass_context=True)
async def save(ctx, *args, amount=2):
    await client.say('....')
    saved = ''
    global saved
    for word in args:
        saved += word
        saved += ' '
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('He has been saved.')
    print(saved)

@client.command()
async def results():
    global dead
    global saved
    await client.say(dead + ' was killed')
    await client.say(saved + ' was saved')
    dead = ''
    saved = ''




client.run(token)

