import discord
from discord.ext import commands 

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("-----------------------------")

@client.command()
@commands.has_role(1174024231097483284) # Role ID
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'{member.mention} has been Kicked!')

@client.command()
@commands.has_role(1174024231097483284) # Role ID
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'{member.mention} has been Banned!')

@client.command()
@commands.has_role(1174024231097483284) # Role ID
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'{user.mention} has been Unbanned!')

@client.command()
async def hello(ctx):
    await ctx.send("What's up degenerates?")

client.run("MTE3NDAyMjQ0MzU1MjIxMTA1NQ.Grgym6.bJFM44kRaZXWbNqUA-QMo1e5udUBariUh2cxdM")
