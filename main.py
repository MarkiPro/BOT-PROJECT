import discord
from discord.ext import commands
import os

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!')

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been banned for {reason}")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are missing permissions to perform this command")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all the required arguments. Please run r!help.")


client.run(token)