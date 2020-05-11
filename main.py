import discord
from discord.ext import commands
import os
from discord import user

class EmbedHelpCommand(commands.MinimalHelpCommand):
    def command_not_found(self, string):
        pass
    def get_ending_note(self):
        return 'Use `{0}{1} [command]` for more information on a certain command.'.format(self.clean_prefix, self.invoked_with)
    def get_command_signature(self, command):
        return '``{1.clean_prefix}{0.qualified_name} {0.signature}``'.format(command, self)
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="**Bot Commands:**", colour=0x0064ff)
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
        embed = discord.Embed(title='**{0.qualified_name} Commands:**'.format(cog), colour=0x0064ff)
        if cog.description:
            embed.description = cog.description
        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.description(self.get_command_signature(command))
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=0x0064ff)
        if group.help:
            embed.description = group.help
        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.description(self.get_command_signature(command))
        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)
    async def send_command_help(self, command):
        embed = discord.Embed(title="**Command**", colour=0x0064ff)
        if command.help:
            embed.description = command.help
        if isinstance(command, commands.Command):
            embed.description(self.get_command_signature(command))
        await self.get_destination().send(embed=embed)

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='rm!', help_command=EmbedHelpCommand(), case_insensitive=True)

@client.event
async def on_ready():
    print(f"Ready")

for file in os.listdir('commands/'):
    if file.endswith('.py'):
        client.load_extension(f'commands.{file[:-3]}')
client.run(token)