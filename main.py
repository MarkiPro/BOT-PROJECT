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

client.remove_command('help')

@client.command()
async def help(ctx, *, commandName):
    if ctx and commandName == "ban":
        embed1 = discord.Embed(
        title="**BAN COMMAND**", 
        description="`{prefix}ban <user> [reason]` - **correct usage, reason is by default set to `None`**",
        color=0x0064ff,
        timestamp=(ctx.timestamp))
        await ctx.send(embed1=embed1)
    if ctx and commandName == "kick":
        embed2 = discord.Embed(
            title="**KICK COMMAND**", 
            description="`{prefix}kick <user> [reason]` - **correct usage, reason is by default set to `None`**",
            color=0x0064ff,
            timestamp=(ctx.timestamp))
        await ctx.send(embed2=embed2)
    if ctx and commandName == "unban":
        embed3 = discord.Embed(
            title="**UNBAN COMMAND**", 
            description="`{prefix}unban <user> [reason]` - **correct usage, reason is by default set to `None`**",
            color=0x0064ff,
            timestamp=(ctx.timestamp))
        await ctx.send(embed3=embed3)
    if ctx and commandName == "clear":
        embed4 = discord.Embed(
            title="**CLEAR COMMAND**", 
            description="`{prefix}clear <amount>` - correct usage, amount is by default set to `0`",
            color=0x0064ff,
            timestamp=(ctx.timestamp))
        await ctx.send(embed4=embed4)
    else:
        embed = discord.Embed(
            title="**COMMANDS:**", 
            description="""

            --EVERYONE--

            `{prefix}help` - shows this message;

            --STAFF--
            
            `{prefix}clear` - clears messages above;
            `{prefix}kick` - kicks a member;
            `{prefix}ban` - bans a member;
            `{prefix}unban` - unbans a member;""",
            color=0x0064ff,
            timestamp=(ctx.timestamp))
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"{member.display_name} has been kicked for: `{reason}`",
        color=0x00fa00,
        timestamp=(ctx.timestamp))
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f"You have been kicked in **{ctx.guild}** for `{reason}`",
        color=0x0064ff,
        timestamp=(ctx.timestamp))
    async with ctx.typing():
        await member.send(embed=embed2)
    await member.kick(reason=reason)
    await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"{member.display_name} has been kicked for: `{reason}`",
        color=0x00fa00,
        timestamp=(ctx.timestamp))
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f"You have been kicked in **{ctx.guild}** for `{reason}`",
        color=0x0064ff,
        timestamp=(ctx.timestamp))
    async with ctx.typing():
        await member.send(embed=embed2)
    await member.ban(reason=reason)
    await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member, *, reason=None):
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"{member.display_name} has been kicked for: `{reason}`",
        color=0x00fa00,
        timestamp=(ctx.timestamp))
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
            await ctx.send(embed=embed1)
@client.event
async def on_command_error(ctx, error):
    embed1 = discord.Embed(
        title="**ERROR**", 
        description=f"***:warning: Please provide all the require arguments, use `r!help <command>` for more information!***",
        color=0xff0000,
        timestamp=(ctx.timestamp))
    embed2 = discord.Embed(
        title="**ERROR**", 
        description=f"***:warning: You do not have permission to use this command!***",
        color=0xff0000,
        timestamp=(ctx.timestamp))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed2)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed1)
client.run(token)