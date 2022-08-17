import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=['!fm '], intents=intents)
token = 'token'

@bot.event
async def on_ready():
    print(f'👌 Login as {bot.user.name}')
    print('Made by Nicknamekr with ❤️')

@bot.command(name="send")
async def ssend(ctx, user: discord.User, *, text):
    wh = await ctx.message.channel.create_webhook(name=".")
    await ctx.message.delete()
    usr = await bot.fetch_user(user.id)
    webhook = DiscordWebhook(url=wh.url, username=f'{usr.name}', content=f'{text}', avatar_url=f'{usr.display_avatar}')
    webhook.execute()
    await wh.delete()

bot.run(token)
