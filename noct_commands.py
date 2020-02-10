import discord
from discord.ext import commands

#PLACEHOLDER FOR COGS
class General(commands.Cog):
    #bot = discord.Client()
    #bot = commands.Bot(command_prefix='!')
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loathe(self, *, module : str):
        self.bot.load_extension(module)

    @commands.command()
    async def annyeong(self, ctx, arg):
        await ctx.send("Working thus far...")

def setup(bot):
    bot.add_cog(General(bot))