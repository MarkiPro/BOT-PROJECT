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
    if(str()):
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
