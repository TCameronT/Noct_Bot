import discord
from discord.ext import commands

# A Cog used exclusively for setting up games of Skribbl.io using custom words

class Skribblio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def skribblio(self, ctx):
        self.hello()
        await ctx.send("In Progress...")
    
    @classmethod
    def hello(self):
        print("It works.")

def setup(bot):
    bot.add_cog(Skribblio(bot))