import discord
from discord.ext import commands

from config.secrets import token

bot = discord.Bot()


@bot.slash_command()
async def ping(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"@{name} pong!")


@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")


bot.run(token)
