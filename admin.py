import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.check(isOwner)
    @commands.is_owner()
    @commands.command()
    async def abba(self, ctx, arg):
        await ctx.send("OPP..." + arg)
    
    @commands.is_owner()
    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Shutting down...")
        quit()
        return         
    
    @commands.is_owner()
    @commands.command(name = "setGame")
    #Use "Game Name Here" for game titles with spaces to be recognized
    async def setGame(self, ctx, arg):
        await ctx.send('Changing game to ' + arg)
        await ctx.bot.change_presence(activity=discord.Game(name=arg))

def setup(bot):
    bot.add_cog(Admin(bot))