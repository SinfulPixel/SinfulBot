
#SinfulBot by SinfulPixel
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
Client = discord.Client()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("SinfulBot Ready!")
    print("I am "+bot.user.name)
    print("My ID is: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='Torturing Darthvaper'))
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value = user.name, inline=True)
    embed.add_field(name="ID",value = user.id,inline=True)
    embed.add_field(name="Status",value=user.status,inline=True)
    embed.add_field(name="In-Game",value=user.game,inline=True)
    embed.add_field(name="Highest Role",value=user.top_role,inline=True)
    embed.add_field(name="Join Date",value=user.joined_at,inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name),description="Here's what I could find.",color=0x00ff00)
    embed.set_author(name="SinfulBot")
    embed.add_field(name="Server Name",value=ctx.message.server.name,inline=True)
    embed.add_field(name="ID",value=ctx.message.server.id,inline=True)
    embed.add_field(name="Roles",value=len(ctx.message.server.roles),inline=True)
    embed.add_field(name="Members",value=len(ctx.message.server.members),inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def rolestats(ctx):
    embed = discord.Embed(title="{}'s Role Info".format(ctx.message.server.name),description="Here's what I could find.",color=0x00ff00)
    embed.set_author(name="SinfulBot")
    roles = ctx.message.server.roles
    nummem = 0
    for role in roles:
        for member in ctx.message.server.members:
            if role in member.roles:
                nummem+=1
        embed.add_field(name=role,value=nummem,inline=True)
        nummem=0
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def dmall(ctx,*, message: str):
    rlimit = 0
    roles = ctx.message.server.roles
    for role in roles:
        for member in ctx.message.server.members:
            if role!="Bots" or role!="Bot":
                continue
            else:
                if rlimit==5:
                    asyncio.sleep(15)
                    rlimit=0
                else:
                    await bot.send_message(member, message)
                    rlimit+=1

        

bot.run('AuthCode')
