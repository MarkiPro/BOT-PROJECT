import discord
from discord.ext import commands
import os

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!')

@client.event
async def on_ready():
    print(f"Logged in as {client.user.tag}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member.has_permissions(ban_members=True, kick_members=True):
        ctx.send(f"I do not have permission to kick {member.display_name}!")
        return
    else:
        pass
        async with ctx.typing():
            await member.send(f"You have been kicked in **{ctx.guild}** for `{reason}`")
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked for: `{reason}`")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member.has_permissions(ban_members=True, kick_members=True):
        ctx.send(f"I do not have permission to ban {member.display_name}!")
        return
    else:
        pass
        async with ctx.typing():
            await member.send(f"You have been banned in **{ctx.guild}** for `{reason}`")
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned for: `{reason}`")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(self,ctx, *, user):
    ban_list = await ctx.guild.bans()
    user_name, user_discriminator = user.split('#')

    for ban_entry in ban_list:
        user = ban_entry.user
        if(user.name, user.discriminator) == (user_name,user_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.name}#{user.discriminator} has been unbanned!")
            return

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all the require arguments, use `r!help <command>`!")

client.run(token)