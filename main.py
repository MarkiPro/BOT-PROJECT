import discord
from discord.ext import commands
import os
from discord import user

class EmbedHelpCommand(commands.MinimalHelpCommand):
    """This is an example of a HelpCommand that utilizes embeds.
    It's pretty basic but it lacks some nuances that people might expect.
    1. It breaks if you have more than 25 cogs or more than 25 subcommands. (Most people don't reach this)
    2. It doesn't DM users. To do this, you have to override `get_destination`. It's simple.
    Other than those two things this is a basic skeleton to get you started. It should
    be simple to modify if you desire some other behaviour.
 
    To use this, pass it to the bot constructor e.g.:
 
    bot = commands.Bot(help_command=EmbedHelpCommand())
    """
    # Set the embed colour here
    COLOUR = discord.Colour.blurple()
 
    def get_ending_note(self):
        return 'Use {0}{1} [command] for more info on a command.'.format(self.clean_prefix, self.invoked_with)
 
    def get_command_signature(self, command):
        return '``{1.clean_prefix}{0.qualified_name} {0.signature}``'.format(command, self)
 
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Bot Commands', colour=self.COLOUR)
        description = self.context.bot.description
        if description:
            embed.description = description
 
        for cog, commands in mapping.items():
            name = 'No Category' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value = ', \u2002'.join(c.name for c in commands)
                if cog and cog.description:
                    value = '{0}\n{1}'.format(cog.description, value)
 
                embed.add_field(name=name, value=value, inline=False)
 
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
 
    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR)
        if cog.description:
            embed.description = cog.description
 
        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.description or '...', inline=False)
 
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
 
    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=self.COLOUR)
        if group.help:
            embed.description = group.help
 
        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command), value=command.short_doc or '...',
                                inline=False)
 
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
 
    async def send_command_help(self, command):
        embed = discord.Embed(title="Command", colour=self.COLOUR)
        if command.help:
            embed.description = command.help
 
        if isinstance(command, commands.Command):
            embed.add_field(name=self.get_command_signature(command), value=command.description or '....', inline=False)
 
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='rm!', help_command=EmbedHelpCommand())

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

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
for file in os.listdir('commands/'):
    if file.endswith('.py'):
        client.load_extension(f'commands.{file[:-3]}')
client.run(token)