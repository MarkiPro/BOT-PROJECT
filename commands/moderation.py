import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
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

def setup(client):
    client.add_cog(Moderation(client))