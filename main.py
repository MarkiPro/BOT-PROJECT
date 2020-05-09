import discord
from discord.ext import commands
import os

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!')

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

@client.command()
async def help(ctx):
    await ctx.send(f"NOOB {ctx.message.author.mention}")

client.run(token)