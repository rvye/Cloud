from discord.ext import commands
from time        import sleep

class SpamCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="stopspam", aliases=["stopspamspamspam", "nospam"])
    async def stop_spam(self, ctx):
        global spam
        spam = False
        await ctx.send("spam stopped")

    @commands.command(name="spam", aliases=["spammy", "spamspamspam"])
    async def spam(self, ctx):
        global spam
        spam = True
        while spam == True:
            await ctx.send("z")
            sleep(1) # 1 second delay to avoid rate limit