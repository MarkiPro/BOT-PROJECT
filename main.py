import discord
from discord.ext import commands
import os
from discord import user
import asyncio
import mysql.connector
import datetime

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!', case_insensitive=True)
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
                            `{prefix}warn <user> <reason>`          - This is the correct usage of the warn command, this command is used for warning a user for something they had done, and the reason is by default set to `None`;
                            `{prefix}removewarn <warningID>`        - This is the correct usage of the removewarn command, this command is used for deleting user's warnings, don't include the `#` in the warning id;
                            `{prefix}warnings <user>`               - This is the correct usage of the warnings command, and this command is used for checking the user warnings;
                            `{prefix}mute <user> <amount> [reason]` - This is the correct usage of the mute command, reason is by default set to `None`, and there is no default value applied to `amount`;
                            `{prefix}unmute <user> [reason]`        - This is the correct usage of the unmute command, reason is by default set to `None`;
                            `{prefix}kick <user> [reason]`          - This is the correct usage of the kick command, reason is by default set to `None`;
                            `{prefix}ban <user> [reason]`           - This is the correct usage of the ban command, reason is by default set to `None`;
                            `{prefix}unban <user> [reason]`         - This is the correct usage of the unban command, by default reason is set to `None`;
                            
                            **--COMMUNITY--**

                            `{prefix}suggest`                       - This is the correct usage of the suggest command, the setup proceeds in dms;
                            `{prefix}post`                          - This is the correct usage of the post command, the setup proceeds in dms, and this command is used for posting `hiring`, `for hire`, `selling creation` and `game advertising` posts;
                            """,
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed6)
    if(str(commandArg)) == ("ban"):
        embed1 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}ban <user> [reason]` - This is the correct usage of the ban command, reason is by default set to `None`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed1)
    if(str(commandArg)) == ("kick"):
        embed2 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}kick <user> [reason]` - This is the correct usage of the kick command, reason is by default set to `None`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed2)
    if(str(commandArg)) == ("clear"):
        embed3 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}clear <amount>` - This is the correct usage of the clear command, amount is by default set to `0`, so it won't delete any other message apart from yours.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed3)
    if(str(commandArg)) == ("unban"):
        embed4 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}unban <user> [reason]` - This is the correct usage of the unban command, by default reason is set to `None`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed4)
    if(str(commandArg)) == ("help"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}help [command]` - This is the correct usage of the help command. This command will inform you about any command that you'd like to, or all the commands, by leaving the command argument empty.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("mute"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}mute <user> <amount> [reason]` - This is correct usage of the mute command, reason is by default set to `None`, and there is no default value applied to `amount`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("unmute"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}unmute <user> [reason]` - This is correct usage of the mute command, reason is by default set to `None`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("suggest"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}suggest` - This is the correct usage of the suggest command, the setup proceeds in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("post"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}post` - This is the correct usage of the post command, the setup proceeds in dms, and this command is used for posting `hiring`, `for hire`, `selling creation` and `game advertising` posts.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("warn"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}warn <user> <reason>` - This is the correct usage of the warn command, this command is used for warning a user for something they had done, and the reason is by default set to `None`.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("warnings"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}warnings <user>` - This is the correct usage of the warnings command, and this command is used for checking the user warnings.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)
    if(str(commandArg)) == ("removewarn"):
        embed5 = discord.Embed(
            title="**COMMAND**", 
            description=f"`{prefix}removewarn <warningID>` - This is the correct usage of the removewarn command, this command is used for deleting user's warnings, don't include the `#` in the warning id.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed5)

@client.command()
@commands.cooldown(1, 60, commands.BucketType.member)
async def credits(ctx):
    user_convertor = commands.UserConverter()
    markipro = await user_convertor.convert(ctx, "438333007036678155")
    malware = await user_convertor.convert(ctx, "466591581286170624")
    creditsEmbed = discord.Embed(
        title=f"**CREDITS**",
        description=f"{markipro} and {malware} made the bot.",
        color=0x0064ff,
        timestamp=datetime.datetime.now(tz=None)
        )
    await ctx.send(embed=creditsEmbed)

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.member)
async def post(ctx):
    if ctx.guild.name == "Test Server":
        RoDevHiringChannelID = id
        RoDevForHireChannelID = id
        RoDevSellingCreationsChannelID = id
        RoDevGameAdvertsChannelID = id
        startedEmbed = discord.Embed(
            title="**POST SETUP**",
            description="Please continue the setup in dms",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        firstEmbed = discord.Embed(
            title="**POST SETUP**",
            description=f"""What would you like to do?
                            
                            `hire`, `get hired`, `sell creation`, `advertise game`""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None),
            set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
        )
        await ctx.send(embed=startedEmbed)
        await ctx.author.send(embed=firstEmbed)
        def check(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        category_message = await client.wait_for('message', check=check, timeout=960)
        category = category_message.content
        if(category == "hire"):
            firstHireEmbed = discord.Embed(
                title="**HIRING SETUP**",
                description="Please go as much in detail about your hiring post.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None),
                set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
            )
            await ctx.author.send(embed=firstHireEmbed)
            message_details = await client.wait_for('message', check=check, timeout=960)
            details = message_details.content
            secondHireEmbed = discord.Embed(
                title="**HIRING SETUP**",
                description="Who are you looking to hire? E.g. scripter, builder etc.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None),
                set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
            )
            await ctx.author.send(embed=secondHireEmbed)
            lookingFor_msg = await client.wait_for('message', check=check, timeout=960)
            lookingFor = lookingFor_msg
            thirdHireEmbed = discord.Embed(
                title="**HIRING SETUP**",
                description="""How would you like to pay?
                                `percentage`, `robux`, `USD`, `other`""",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None),
                set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
            )
            await ctx.author.send(embed=thirdHireEmbed)
            message_body1 = await client.wait_for('message', check=check, timeout=960)
            body1 = message_body1.content
            if(body1 == "percentage"):
                fourthHireEmbed = discord.Embed(
                    title="**HIRING SETUP**",
                    description="How big of a percentage are you willing to give?",
                    color=0x0064ff,
                    timestamp=datetime.datetime.now(tz=None),
                    set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
                )
                await ctx.author.send(embed=fourthHireEmbed)
                percentage_amount = await client.wait_for('message', check=check, timeout=960)
                percentage = percentage_amount.content
                fifthHireEmbed = discord.Embed(
                    title="**HIRING SETUP**",
                    description="Are you willing to add any other payment? `yes`/`no`",
                    color=0x0064ff,
                    timestamp=datetime.datetime.now(tz=None),
                    set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
                )
                await ctx.author.send(embed=fifthHireEmbed)
                other_amount = await client.wait_for('message', check=check, timeout=960)
                other_amount_body = other_amount.content
                if(other_amount_body == "no"):
                    sixthHireEmbed = discord.Embed(
                        title="**HIRING SETUP FINISHED**",
                        description="This is the ending result. Say `done` to continue.",
                        color=0x0064ff,
                        timestamp=datetime.datetime.now(tz=None),
                        set_footer="Timeout on this message is `16 minutes`. Say `cancel` to cancel prompt."
                    )
                    seventhHireEmbed = discord.Embed(
                        title="**HIRING POST**",
                        description=f"""

                        Contact: {ctx.author.mention};

                        About: {details};

                        Looking For: {lookingFor};
                        
                        Payment: {body1}, {percentage};
                        
                        """,
                        color=0x0064ff,
                        timestamp=datetime.datetime.now(tz=None),
                        set_footer=f"by: {ctx.author}"
                    )
                    await ctx.author.send(embed=sixthHireEmbed)
                    await ctx.author.send(embed=seventhHireEmbed)
                    finish_message = await client.wait_for('message', check=check, timeout=960)
                    finish_msg_body = finish_message.content
                    if(finish_msg_body == "done"):
                        RoDevHiringChannel = client.get_channel(id=RoDevHiringChannelID)
                        sent = await RoDevHiringChannel.send(embed=seventhHireEmbed)


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.member)
async def suggest(ctx):
    if ctx.guild.name == "RoDev's":
        suggestionsChannel = client.get_channel(id=711307176899248149)
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please continue the setup in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="What would you like to name your suggestion?",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
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
        title_message = await client.wait_for('message', check=check, timeout=1000)
        title = title_message.content
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please write down your suggestion in detail.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.author.send(embed=startEmbed)
        body_message = await client.wait_for('message', check=check, timeout=1000)
        body = body_message.content
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""*Say `done` to post.*""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        body_message2 = await client.wait_for('message', check=check, timeout=1000)
        body2 = body_message2.content
        if(body2 == "done"):
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="Your suggestion has been posted.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.author.send(embed=finalEmbed)
            suggestedEmbed = discord.Embed(
                title=f"**{title}**",
                description=f"{body}",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            suggestedEmbed.set_footer(text=f"by: {ctx.author}")
            sent = await suggestionsChannel.send(embed=suggestedEmbed)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎')
    if ctx.guild.name == "Content Creators":
        suggestionsChannel = client.get_channel(id=712655570737299567)
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please continue the setup in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="What would you like to name your suggestion?",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
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
        title_message = await client.wait_for('message', check=check, timeout=1000)
        title = title_message.content
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please write down your suggestion in detail.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.author.send(embed=startEmbed)
        body_message = await client.wait_for('message', check=check, timeout=1000)
        body = body_message.content
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""*Say `done` to post.*""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        body_message2 = await client.wait_for('message', check=check, timeout=1000)
        body2 = body_message2.content
        if(body2 == "done"):
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="Your suggestion has been posted.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.author.send(embed=finalEmbed)
            suggestedEmbed = discord.Embed(
                title=f"**{title}**",
                description=f"{body}",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            suggestedEmbed.set_footer(text=f"by: {ctx.author}")
            sent = await suggestionsChannel.send(embed=suggestedEmbed)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎')
    if ctx.guild.name == "ROBOT's Server 2.0":
        suggestionsChannel = client.get_channel(id=712606761617719326)
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please continue the setup in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="What would you like to name your suggestion?",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
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
        title_message = await client.wait_for('message', check=check, timeout=1000)
        title = title_message.content
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please write down your suggestion in detail.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.author.send(embed=startEmbed)
        body_message = await client.wait_for('message', check=check, timeout=1000)
        body = body_message.content
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""*Say `done` to post.*""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        body_message2 = await client.wait_for('message', check=check, timeout=1000)
        body2 = body_message2.content
        if(body2 == "done"):
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="Your suggestion has been posted.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.author.send(embed=finalEmbed)
            suggestedEmbed = discord.Embed(
                title=f"**{title}**",
                description=f"{body}",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            suggestedEmbed.set_footer(text=f"by: {ctx.author}")
            sent = await suggestionsChannel.send(embed=suggestedEmbed)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎')
    if ctx.guild.name == "The Court":
        suggestionsChannel = client.get_channel(id=707272718885585039)
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please continue the setup in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="What would you like to name your suggestion?",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
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
        title_message = await client.wait_for('message', check=check, timeout=1000)
        title = title_message.content
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please write down your suggestion in detail.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.author.send(embed=startEmbed)
        body_message = await client.wait_for('message', check=check, timeout=1000)
        body = body_message.content
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""*Say `done` to post.*""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        body_message2 = await client.wait_for('message', check=check, timeout=1000)
        body2 = body_message2.content
        if(body2 == "done"):
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="Your suggestion has been posted.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.author.send(embed=finalEmbed)
            suggestedEmbed = discord.Embed(
                title=f"**{title}**",
                description=f"{body}",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            suggestedEmbed.set_footer(text=f"by: {ctx.author}")
            sent = await suggestionsChannel.send(embed=suggestedEmbed)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎')
@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def unmute(ctx, member: discord.Member, *, reason=None):
    if ctx.guild.name == "The Court":
        mutedRole = discord.utils.get(ctx.guild.roles, id=709737313705525358)
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
                color=0x00fa00,
                timestamp=datetime.datetime.now(tz=None)
                )
            embed2 = discord.Embed(
                title="**NOTIFICATION**", 
                description=f":bell: *** You *** have been unmuted!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.send(embed=embed1)
            await member.send(embed=embed2)
    if ctx.guild.name == "Content Creators":
        mutedRole = discord.utils.get(ctx.guild.roles, id=712730274412232807)
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
                color=0x00fa00,
                timestamp=datetime.datetime.now(tz=None)
                )
            embed2 = discord.Embed(
                title="**NOTIFICATION**", 
                description=f":bell: *** You *** have been unmuted!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.send(embed=embed1)
            await member.send(embed=embed2)
    if ctx.guild.name == "RoDev's":
        mutedRole = discord.utils.get(ctx.guild.roles, id=601185151766233088)
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
                color=0x00fa00,
                timestamp=datetime.datetime.now(tz=None)
                )
            embed2 = discord.Embed(
                title="**NOTIFICATION**", 
                description=f":bell: *** You *** have been unmuted!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.send(embed=embed1)
            await member.send(embed=embed2)
    if ctx.guild.name == "ROBOT's Server 2.0":
        mutedRole = discord.utils.get(ctx.guild.roles, id=712620826398162958)
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
                color=0x00fa00,
                timestamp=datetime.datetime.now(tz=None)
                )
            embed2 = discord.Embed(
                title="**NOTIFICATION**", 
                description=f":bell: *** You *** have been unmuted!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.send(embed=embed1)
            await member.send(embed=embed2)

@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 5, commands.BucketType.member)
async def mute(ctx, member: discord.Member, time, *, reason=None):
    if ctx.guild.name == "ROBOT's Server 2.0":
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
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed2 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** {member.display_name} *** has been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed3 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** You *** have been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        mutedRole = discord.utils.get(ctx.guild.roles, id=712620826398162958)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed1)
        await member.send(embed=embed3)
        await asyncio.sleep(time)
        await ctx.send(embed=embed2)
        await member.remove_roles(mutedRole)
    if ctx.guild.name == "RoDev's":
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
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed2 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** {member.display_name} *** has been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed3 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** You *** have been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        mutedRole = discord.utils.get(ctx.guild.roles, id=601185151766233088)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed1)
        await member.send(embed=embed3)
        await asyncio.sleep(time)
        await ctx.send(embed=embed2)
        await member.remove_roles(mutedRole)
    if ctx.guild.name == "Content Creators":
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
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed2 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** {member.display_name} *** has been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed3 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** You *** have been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        mutedRole = discord.utils.get(ctx.guild.roles, id=712730274412232807)
        await member.add_roles(mutedRole)
        await ctx.send(embed=embed1)
        await member.send(embed=embed3)
        await asyncio.sleep(time)
        await ctx.send(embed=embed2)
        await member.remove_roles(mutedRole)
    if ctx.guild.name == "The Court":
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
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed2 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** {member.display_name} *** has been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        embed3 = discord.Embed(
            title="**NOTIFICATION**", 
            description=f":bell: *** You *** have been unmuted!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        mutedRole = discord.utils.get(ctx.guild.roles, id=709737313705525358)
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
            color=0xffbd00,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed1)
    embed1 = discord.Embed(
        title="**SUCCESS**", 
        description=f"***:white_check_mark: *** {member.display_name} *** has been kicked for: `{reason}`!***",
        color=0x00fa00,
        timestamp=datetime.datetime.now(tz=None)
        )
    embed2 = discord.Embed(
        title="**NOTIFICATION**", 
        description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`!",
        color=0x0064ff,
        timestamp=datetime.datetime.now(tz=None)
        )
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
            color=0xffbd00,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed1)
    embed1 = discord.Embed(
        title="**SUCCESS**",
        description=f"***:white_check_mark: *** {member.display_name} *** has been banned for: `{reason}`!***",
        color=0x00fa00,
        timestamp=datetime.datetime.now(tz=None)
        )
    embed2 = discord.Embed(
        title="**NOTIFICATION**",
        description=f":bell: *You have been banned in **{ctx.guild}** for:* `{reason}`!",
        color=0x0064ff,
        timestamp=datetime.datetime.now(tz=None)
        )
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
        color=0x00fa00,
        timestamp=datetime.datetime.now(tz=None)
        )
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
        host="us-cdbr-east-06.cleardb.net",
        user="baba29035f4254",
        passwd="8a63c86d",
        database="heroku_daa9f1b493ff319"
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO warns VALUES (%s, %s, %s, %s, %s)", (None, ctx.guild.id, member.id, reason, ctx.author.id))
    connection.commit()
    await ctx.send(f"{member} has been warned!")

@client.command()
async def warnings(ctx, member: discord.Member):
    connection = mysql.connector.connect(
        host="us-cdbr-east-06.cleardb.net",
        user="baba29035f4254",
        passwd="8a63c86d",
        database="heroku_daa9f1b493ff319"
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
        host="us-cdbr-east-06.cleardb.net",
        user="baba29035f4254",
        passwd="8a63c86d",
        database="heroku_daa9f1b493ff319"
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

@client.event
async def on_command_error(ctx, error):
    prefix = await client.get_prefix(ctx.message)
    if isinstance(error, commands.CommandOnCooldown):
        embed3 = discord.Embed(
            title="**ERROR**", 
            description=f"""***:no_entry_sign: The command is on a cooldown, please do not rush it.
                                cooldown for this command is `{error.cooldown.per}`, and you have `{error.retry_after}` left***""",
            color=0xff0000,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed3)
    if isinstance(error, commands.MissingRequiredArgument):
        embed1 = discord.Embed(
            title="**ERROR**", 
            description=f"***:no_entry_sign: You're missing arguments! Please do `{prefix}help <command>` to get more information on a certain command!***",
            color=0xff0000,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed1)
    if isinstance(error, commands.MissingPermissions):
        embed2 = discord.Embed(
            title="**ERROR**", 
            description=f"***:no_entry_sign: You're missing permission to use this command!***",
            color=0xff0000,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.send(embed=embed2)

client.run(token)