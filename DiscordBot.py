import random

import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

amount = 0


@client.event
async def on_ready():
    print('bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['it is certain',
                 'ooh hell naw']
    await ctx.send(f'Question: {question}\nAnswer:{random.choice(responses)}')


client.run("NzY2MzUzNzY2NzUyMTkwNDc1.X4iIkA.gdcZx27XvjqT3d-zesslPPgkdNs")
