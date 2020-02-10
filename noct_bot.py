import discord
from discord.ext import commands

#Notes:
#Bot Prefix is '!'
#Cogs [or extensions] are named after the file's name, not the class name

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
    extensions = ['noct_commands', 'admin', 'skribbl']
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
        self.bot.run(getToken())        

    #End Noctis

Noct = Noctis.bot
@Noct.event
async def on_ready():
    #Bot is logged in
    print('Logged in as {0.user}'.format(Noctis.bot))
    await Noct.change_presence(activity=discord.Game(name='FFVXIII'))

@Noct.event
async def on_message_delete(message):
    print("A message was deleted!")
    #print(message.content)
    if(message.author.id == Noct.user.id):
        await message.channel.send("That's my job.")

@Noct.event
async def on_message(message):
    user = Noct.get_user(message.author.id)
    if message.author == Noct.user:
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