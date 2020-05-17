import discord
from discord.ext import commands
import os
from discord import user
import asyncio
import mysql.connector
import datetime

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
            
                            `{prefix}help [command]`                - This is the correct usage of the help command. This command will inform you about any command that you'd like to, or all the commands, by leaving the command argument empty;
                            
                            **--MODERATION--**
                            
                            `{prefix}clear <amount>`                - This is the correct usage of the clear command, amount is by default set to `0`, so it won't delete any other message apart from yours;
                            `{prefix}mute <user> <amount> [reason]` - This is the correct usage of the mute command, reason is by default set to `None`, and there is no default value applied to `amount`;
                            `{prefix}unmute <user> [reason]`        - This is the correct usage of the unmute command, reason is by default set to `None`;
                            `{prefix}kick <user> [reason]`          - This is the correct usage of the kick command, reason is by default set to `None`;
                            `{prefix}ban <user> [reason]`           - This is the correct usage of the ban command, reason is by default set to `None`;
                            `{prefix}unban <user> [reason]`         - This is the correct usage of the unban command, by default reason is set to `None`;
                            
                            **--COMMUNITY--**

                            `{prefix}suggest <suggestion>`          - This is the correct usage of the suggest command, suggestion doesn't have a default value;
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
@commands.cooldown(1, 60, commands.BucketType.member)
async def credits():
    suggestedEmbed = discord.Embed(
        title=f"**CREDITS**",
        description=f"""
        This bot was originally made by `MarkiPro#0825`.
        HUUUUUUGE Thank you to `Malware#1234` for being of big help with setting a big chunk of this bot up.""",
        color=0x0064ff
        )
    suggestedEmbed.timestamp(datetime.datetime.now().strftime())

@client.command()
@commands.cooldown(1, 3600, commands.BucketType.member)
async def suggest(ctx):
    startedEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="Please continue in dms.",
        color=0x0064ff
        )
    furstEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="What would you like to name your suggestion?",
        color=0x0064ff
        )
    await ctx.send(embed=startedEmbed)
    await ctx.author.send(embed=furstEmbed)
    def check(m):
        if isinstance(m.channel, discord.DMChannel):
            if m.author == ctx.author:
                return True
            else:
                return False
        else:
            return False
    title_message = await client.wait_for('message', check=check, timeout=500)
    title = title_message.content
    startEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="Please write down your suggestion in detail.",
        color=0x0064ff
        )
    await ctx.author.send(embed=startEmbed)
    body_message = await client.wait_for('message', check=check, timeout=500)
    body = body_message.content
    finalEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="Your suggestion has been posted.",
        color=0x0064ff
        )
    await ctx.author.send(embed=finalEmbed)
    suggestionsChannel = client.get_channel(id=711307176899248149)
    ThumbsUpEmoji = client.get_emoji(id=711691482683277313)
    ThumbsDownEmoji = client.get_emoji(id=711691608780963937)
    suggestedEmbed = discord.Embed(
        title=f"**{title}**",
        description=f"{body}",
        color=0x0064ff,
        timestamp=datetime.datetime.utcfromtimestamp(1589750228)
        )
    suggestedEmbed.set_footer(f"by: {ctx.author}")
    await ctx.add_reaction(ThumbsUpEmoji)
    await ctx.add_reaction(ThumbsDownEmoji)
    await suggestionsChannel.send(embed=suggestedEmbed)
@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def unmute(ctx, member: discord.Member, *, reason=None):
    mutedRole = discord.utils.get(ctx.guild.roles, id=709737313705525358)
    everyoneRole = discord.utils.get(ctx.guild.roles, id=707262068218265653)
    has_role = False
    for role in member.roles:
        if role.name == 'Muted':
            has_role = True
            break
    if has_role:
        await member.remove_roles(mutedRole)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been unmuted for: `{reason}`***",
            color=0x00fa00)
        embed2 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** You *** have been unmuted!",
            color=0x0064ff)
        await ctx.send(embed=embed1)
        await member.send(embed=embed2)

@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 5, commands.BucketType.member)
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
    mutedRole = await discord.utils.get(ctx.guild.roles, id=709737313705525358)
    await member.add_roles(mutedRole)
    await ctx.send(embed=embed1)
    await member.send(embed=embed3)
    await asyncio.sleep(time)
    await ctx.send(embed=embed2)
    await member.remove_roles(mutedRole)

@client.command()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 5, commands.BucketType.member)
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
@commands.cooldown(1, 5, commands.BucketType.member)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount+1)


@client.command()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 5, commands.BucketType.member)
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
@commands.cooldown(1, 5, commands.BucketType.member)
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

@client.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def warn(ctx, member: discord.Member, *, reason):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='discord-py-tutorial'
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO warns VALUES (%s, %s, %s, %s, %s)", (None, ctx.guild.id, member.id, reason, ctx.author.id))
    connection.commit()
    await ctx.send(f"{member} has been warned!")

@client.command()
async def warnings(ctx, member: discord.Member):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='discord-py-tutorial'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM warns WHERE user_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
    warns = cursor.fetchall()
    embed = discord.Embed(title=f"Warns of {member}".upper(), description="Returns all the warns of a user")
    member_converter = commands.MemberConverter()
    for warn in warns:
        moderator = await member_converter.convert(ctx, warn[4])
        embed.add_field(name=f"Warn #{warn[0]} by {moderator}", value=f"{warn[3]}", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def removewarn(ctx, *, id):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='discord-py-tutorial'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM warns WHERE id = %s", (int(id), ))
    warn = cursor.fetchone()

    if warn == None:
        return await ctx.send("This warn does'nt exist!")

    if int(warn[1]) != ctx.guild.id:
        return await ctx.send("This warn doesnt belong to this guild.")


    cursor.execute("DELETE FROM warns WHERE id = %s", (int(id), ))
    connection.commit()
    await ctx.send(f"Removed warn #{id}")
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
    embed3 = discord.Embed(
        title="**ERROR**", 
        description=f"***:no_entry_sign: The command is on a cooldown, please do not rush it.***",
        color=0xff0000)
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed3)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed1)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed2)
"""
client.run(token)