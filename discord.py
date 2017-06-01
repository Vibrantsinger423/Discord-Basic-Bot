import discord

bot = commands.Bot(command_prefix='s!', description="Just some random bot...")

owner = ["273145338506903552"]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))

bot.run('312990951775928322')
