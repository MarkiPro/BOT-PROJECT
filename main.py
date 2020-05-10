import discord
from discord.ext import commands
import os
from discord import user

embed = discord.Embed
embed2 = discord.Embed
token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!')

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    async with ctx.typing():
        await member.send(f"You have been kicked in **{ctx.guild}** for `{reason}`")
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been kicked for: `{reason}`")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    async with ctx.typing():
        await member.send(f"You have been banned in **{ctx.guild}** for `{reason}`")
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned for: `{reason}`")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_id = member
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.id) == (member_id):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.name}#{user.discriminator} has been unbanned!")
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.name}#{user.discriminator} has been unbanned!")
"""@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"***\:warning: You do not have permission to use this command!***")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"***\:warning: Please provide all the require arguments, use `r!help <command>` for more information!***")"""
client.run(token)