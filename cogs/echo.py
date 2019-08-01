from discord.ext import commands


class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *text):
        print(ctx.author.id)
        await ctx.send(" ".join(text))


def setup(bot):
    bot.add_cog(Echo(bot))
