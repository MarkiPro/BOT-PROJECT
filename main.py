import discord
from discord.ext import commands
import os
from discord import user
import asyncio

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='rm!', case_insensitive=True)

@client.event
async def on_ready():
    print(f"Ready")

@client.remove_command('help')

@client.command()
async def help(ctx, *, commandArg=None):
    prefix = await client.get_prefix(ctx.message)
    if(not commandArg):
        embed6 = discord.Embed(
            title="**COMMANDS:**", 
            description=f"""**--INFORMATIVE--**
            
                            `{prefix}help [command]` - This is the correct usage of the help command. This command will inform you about any command that you'd like to, or all the commands, by leaving the command argument empty;
                            
                            **--MODERATION--**
                            
                            `{prefix}clear <amount>`                - This is the correct usage of the clear command, amount is by default set to `0`, so it won't delete any other message apart from yours;
                            `{prefix}mute <user> <amount> [reason]` - This is the correct usage of the mute command, reason is by default set to `None`, and there is no default value applied to `amount`;
                            `{prefix}unmute <user> [reason]`        - This is the correct usage of the unmute command, reason is by default set to `None`;
                            `{prefix}kick <user> [reason]`          - This is the correct usage of the kick command, reason is by default set to `None`;
                            `{prefix}ban <user> [reason]`           - This is the correct usage of the ban command, reason is by default set to `None`;
                            `{prefix}unban <user> [reason]`         - This is the correct usage of the unban command, by default reason is set to `None`;
                            """,
            color=0x0064ff)
        await ctx.send(embed=embed6)
    if(str(commandArg)) == ("ban"):
        embed1 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}ban <user> [reason]` - This is the correct usage of the ban command, reason is by default set to `None`.",
            color=0x0064ff)
        await ctx.send(embed=embed1)
    if(str(commandArg)) == ("kick"):
        embed2 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}kick <user> [reason]` - This is the correct usage of the kick command, reason is by default set to `None`.",
            color=0x0064ff)
        await ctx.send(embed=embed2)
    if(str(commandArg)) == ("clear"):
        embed3 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}clear <amount>` - This is the correct usage of the clear command, amount is by default set to `0`, so it won't delete any other message apart from yours.",
            color=0x0064ff)
        await ctx.send(embed=embed3)
    if(str(commandArg)) == ("unban"):
        embed4 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}unban <user> [reason]` - This is the correct usage of the unban command, by default reason is set to `None`.",
            color=0x0064ff)
        await ctx.send(embed=embed4)
    if(str(commandArg)) == ("help"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}help [command]` - This is the correct usage of the help command. This command will inform you about any command that you'd like to, or all the commands, by leaving the command argument empty.",
            color=0x0064ff)
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("mute"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}mute <user> <amount> [reason]` - This is correct usage of the mute command, reason is by default set to `None`, and there is no default value applied to `amount`.",
            color=0x0064ff)
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("unmute"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}unmute <user> [reason]` - This is correct usage of the mute command, reason is by default set to `None`.",
            color=0x0064ff)
        await ctx.send(embed=embed5)

@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    mutedRole = discord.utils.get(ctx.guild.roles, id=709737313705525358)
    everyoneRole = discord.utils.get(ctx.guild.roles, id=707262068218265653)
    has_role = False
    for role in member.roles:
        if role.name == 'Muted':
            has_role = True
            break
    if has_role:
        member.remove_roles(mutedRole)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been unmuted for: `{reason}`***",
            color=0x00fa00)
        await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time, *, reason=None):
    def parse_time(time):
        split_time = time.split(' ')
        options = {'m': 60, 'h': 3600, 'd': 86400}
        time = 0

        for _ in split_time:
            for key, value in options.items():
                if _.endswith(key):
                    multiplier = int(_[:-1])
                    print(multiplier)
                    time_to_add = value * multiplier
                    print(time_to_add)
                    time = time + time_to_add

        return time
    embed1 = discord.Embed(
        title="**SUCCESS**",
        description=f"***:white_check_mark: *** {member.display_name} *** has been muted for: `{time}`, for: `{reason}`!***",
        color=0x00fa00)
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *** {member.display_name} *** has been unmuted!",
        color=0x0064ff)
    embed3 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *** You *** have been unmuted!",
        color=0x0064ff)
    mutedRole = discord.utils.get(ctx.guild.roles, id=709737313705525358)
    await member.add_roles(mutedRole)
    await ctx.send(embed=embed1)
    await member.send(embed=embed3)
    await asyncio.sleep(time)
    await ctx.send(embed=embed2)
    await member.remove_roles(mutedRole)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if(member == ctx.me):
        embed1 = discord.Embed(
            title="**OOPS**",
            description=f"***Sorry bro, not gonna happen :) ***",
            color=0xffbd00)
        await ctx.send(embed=embed1)
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {member.display_name} *** has been kicked for: `{reason}`!***",
        color=0x00fa00)
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`!",
        color=0x0064ff)
    async with ctx.typing():
        await member.send(embed=embed2)
        await member.kick(reason=reason)
        await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if(member == ctx.me):
        embed1 = discord.Embed(
            title="**OOPS**",
            description=f"***Sorry bro, not gonna happen :) ***",
            color=0xffbd00)
        await ctx.send(embed=embed1)
    embed1 = discord.Embed(
        title="**SUCCESS**",
        description=f"***:white_check_mark: *** {member.display_name} *** has been banned for: `{reason}`!***",
        color=0x00fa00)
    embed2 = discord.Embed(
        title="**NOTIFICATION**",
        description=f":bell: *You have been banned in **{ctx.guild}** for:* `{reason}`!",
        color=0x0064ff)
    async with ctx.typing():
        await member.ban(reason=reason)
        await ctx.send(embed=embed1)
        await member.send(embed=embed2)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member, *, reason=None):
    ban_list = await ctx.guild.bans()
    for ban_entry in ban_list:
        user = ban_entry.user
        id = member
        embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {user.display_name} *** has been unbanned for: `{reason}`!***",
        color=0x00fa00)
        try:
            user_name, user_discriminator = member.split('#')
        except ValueError:
            user_name = ''
            user_discriminator = ''
        if (user.name, user.discriminator) == (user_name, user_discriminator) or int(id) == user.id:
            await ctx.guild.unban(user, reason=reason)
            await ctx.send(embed=embed1)
"""
@client.event
async def on_command_error(ctx, error):
    prefix = await client.get_prefix(ctx.message)
    embed1 = discord.Embed(
        title="**ERROR**", 
        description=f"***:no_entry_sign: You're missing arguments! Please do `{prefix}help <command>` to get more information on a certain command!***",
        color=0xff0000)
    embed2 = discord.Embed(
        title="**ERROR**", 
        description=f"***:no_entry_sign: You're missing permission to use this command!***",
        color=0xff0000)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed2)
"""
client.run(token)