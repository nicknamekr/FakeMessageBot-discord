"""
Made by NicknameKR
You can use mine freely
(Under the MIT License)

Thanks for Using!
If you need some help, please send dm to 사죄#9999.
"""
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
async def send(ctx, user: discord.User, *, text):
    webhook = await ctx.message.channel.create_webhook(name=user.id)
    await ctx.message.delete()
    DiscordWebhook(url=wh.url, username=f'{user.name}', content=f'{text}', avatar_url=f'{user.display_avatar}').execute()
    await webhook.delete()

bot.run(token)
