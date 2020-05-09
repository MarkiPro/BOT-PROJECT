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
async def kick(ctx, member: discord.Member, *, reason=NotImplemented):
    embed.color(embed, "#07ff00")
    embed.title(embed, "SUCCESS")
    embed.description(f"***\:white_check_mark: {user.display_name} has been unbanned!***")
    embed.timestamp(ctx.timestamp)
    async with ctx.typing():
        await member.send(f"You have been kicked in **{ctx.guild}** for `{reason}`")
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked for: `{reason}`")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed.color(embed, "#07ff00")
    embed.title(embed, "SUCCESS")
    embed.description(f"***\:white_check_mark: {member.display_name} has been banned for:*** `{reason}`")
    embed.timestamp(ctx.timestamp)
    async with ctx.typing():
        await member.send()
    await member.ban(reason=reason)
    await ctx.send(embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(self,ctx, *, user):
    embed.color(embed, "#07ff00")
    embed.title(embed, "SUCCESS")
    embed.description(f"***\:white_check_mark: {user.display_name} has been unbanned!***")
    embed.timestamp(ctx.timestamp)
    ban_list = await ctx.guild.bans()
    user_name, user_discriminator = user.split('#')

    for ban_entry in ban_list:
        user = ban_entry.user
        if(user.name, user.discriminator) == (user_name,user_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed)
            return

@client.event
async def on_command_error(ctx, error):
    embed.color(embed, "#07ff00")
    embed.title(embed, "ERROR")
    embed.description(f"***\:warning: You do not have permission to use this command!***")
    embed.timestamp(ctx.timestamp)
    embed2.color(embed, "#07ff00")
    embed2.title(embed, "ERROR")
    embed2.description(f"***\:warning: Please provide all the require arguments, use `r!help <command>` for more information!***")
    embed2.timestamp(ctx.timestamp)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed2)

client.run(token)