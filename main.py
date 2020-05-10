import discord
from discord.ext import commands
import os
from discord import user

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='rm!')
prefix = commands.Bot.command_prefix

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

@client.remove_command(help)

@client.command()
async def help(ctx, *, commandArg):
    if(str(commandArg)) == ("ban"):
        embed1 = discord.Embed(
            title="**BAN COMMAND**", 
            description=f"`{prefix}ban <user> [reason]` - correct usage of ban command, reason is by default set to `None`.",
            color=0x00fa00)
        await ctx.send(embed1=embed1)
    if(str(commandArg)) == ("kick"):
        embed1 = discord.Embed(
            title="**KICK COMMAND**", 
            description=f"`{prefix}kick <user> [reason]` - correct usage of kick command, reason is by default set to `None`.",
            color=0x00fa00)
        await ctx.send(embed1=embed1)
    if(str(commandArg)) == ("clear"):
        embed1 = discord.Embed(
            title="**CLEAR COMMAND**", 
            description=f"`{prefix}clear <amount>` - correct usage of clear command, amount is by default set to `0`.",
            color=0x00fa00)
        await ctx.send(embed1=embed1)
    if(str(commandArg)) == ("unban"):
        embed1 = discord.Embed(
            title="**UNBAN COMMAND**", 
            description=f"`{prefix}unban <user> [reason]` - correct usage of unban command, reason is by default set to `None`.",
            color=0x00fa00)
        await ctx.send(embed1=embed1)
    if(str(commandArg)) == (None):
        embed1 = discord.Embed(
            title="**COMMANDS:**", 
            description=f"""
            
            --MODERATION

            `{prefix}clear`          **- clears messages;**
            `{prefix}kick`           **- kicks users;**
            `{prefix}ban`            **- bans users;**
            `{prefix}unban`          **- unbans users;**

            --INFORMATIVE--

            `{prefix}help`           **- shows this message;**
            `{prefix}help <command>` **- shows more about a certain command;**
            """,
            color=0x00fa00)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {member.display_name} *** has been kicked for: `{reason}`***",
        color=0x00fa00)
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`",
        color=0x0064ff)
    async with ctx.typing():
        await member.send(embed=embed2)
        await member.kick(reason=reason)
        await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {member.display_name} *** has been banned for: `{reason}`***",
        color=0x00fa00)
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`",
        color=0x0064ff)
    async with ctx.typing():
        await member.ban(reason=reason)
        await ctx.send(embed=embed1)
        await member.send(embed=embed2)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {member.display_name} *** has been unbanned for: `{reason}`***",
        color=0x00fa00)
    ban_list = await ctx.guild.bans()
    for ban_entry in ban_list:
        user = ban_entry.user
        id = member
        try:
            user_name, user_discriminator = member.split('#')
        except ValueError:
            user_name = ''
            user_discriminator = ''
        if (user.name, user.discriminator) == (user_name, user_discriminator) or int(id) == user.id:
            await ctx.guild.unban(user, reason=reason)
            await ctx.send(embed1=embed1)
@client.event
async def on_command_error(ctx, error):
    embed1 = discord.Embed(
        title="**ERROR**", 
        description=f"***:warning: Please provide all the require arguments, use `r!help <command>` for more information!***",
        color=0xff0000)
    embed2 = discord.Embed(
        title="**ERROR**", 
        description=f"***:warning: You do not have permission to use this command!***",
        color=0xff0000)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed2)
client.run(token)