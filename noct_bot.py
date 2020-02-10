import discord
from discord.ext import commands

def getToken():
    with open('token', 'r') as tokenFile:
        tokenStr = tokenFile.read()
        tokenFile.close()
        return tokenStr

#Noctis's brain
class Noctis:
    bot = discord.Client()
    bot = commands.Bot(command_prefix='!')
    bot.owner_id = 148987550072176641
    extensions = ['noct_commands', 'admin']
    loadedExts = set()

    def __init__(self):
        for ext in self.extensions:
            self.load_cog(ext)
        print("Init Done.")
        

    @classmethod
    def load_cog(self, cog):
        #Initializes cog's class instance
        self.bot.load_extension(cog)
        self.loadedExts.add(cog)
        print("Extension " + cog + " loaded")

    @classmethod
    def unload_cog(self, cog):
        #Initializes cog's class instance
        self.bot.unload_extension(cog)
        self.loadedExts.remove(cog)
        print("Extension " + cog + " unloaded")
    
    @classmethod
    def reload_cog(self, cog):
        self.bot.reload_extension(cog)
        self.loadedExts.add(cog)
        print("Extension " + cog + " reloaded")

    @classmethod
    def run(self):
        try:
            self.bot.run(getToken())
        except:
            print("Invalid token. Please check './token' and ensure your bot's token is correct.")
        

    def print():
        print("Hello")
    #End Noctis

Noct = Noctis.bot
@Noct.event
async def on_ready():
    #Bot is logged in
    print('Logged in as {0.user}'.format(Noctis.bot))
    await Noct.change_presence(activity=discord.Game(name='FFVXIII'))

@Noct.event
async def on_message(message):
    user = Noct.get_user(message.author.id)
    if message.author == Noct.user:
        return

    if message.content.startswith(Noct.command_prefix + 'stop'):
        print("Shutting down...")
        quit()
        return

    await Noct.process_commands(message)

@Noct.command(name="aniyo")
async def annyeong(context, arg):
    await context.send(arg)

@Noct.command(name="kill")
async def kill(context):
    if context.message.author.id != 148987550072176641:
        print(context.message.author.id + 'attempted to perform !Kill')
        await context.send("You are not authorized to perform this action.")
    else:
        await context.send("Shutting down...")
        exit()

@commands.is_owner()
@Noct.command()
async def load(ctx, arg):
    Noctis.load_cog(arg)
    await ctx.send("Loading " + arg + "...")

@commands.is_owner()
@Noct.command()
async def unload(ctx, arg):
    Noctis.unload_cog(arg)
    await ctx.send("Unloading " + arg + "...")

@commands.is_owner()
@Noct.command()
async def reload(ctx, arg):
    Noctis.reload_cog(arg)
    await ctx.send("Reloading " + arg + "...")

@Noct.command(name="list")
async def listCogs(ctx, arg=""):
    await ctx.send(', '.join(Noctis.extensions))

@Noct.command(name="loaded")
async def listLoadedCogs(ctx):
    await ctx.send(', '.join(Noctis.loadedExts))

@Noct.command(name="helpme")
async def help(ctx):
    await ctx.send('Nah.')

def setup(bot):
    bot.add_cog(Noctis(bot))