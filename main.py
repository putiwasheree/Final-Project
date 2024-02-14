import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'こんにちは！ルーキーです🤖🌟。{bot.user}です! 🤖🌟。')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def global_warming(ctx):
    await ctx.send("Global warming is the increase in the average temperature of the Earth's atmosphere, oceans, and land that causes climate change around us. 🌍🔥")
@bot.command()
async def condition(ctx):
    await ctx.send("Earth's global temperature is 2°-3° C hotter today! 😱")
@bot.command()
async def causes(ctx):
    await ctx.send(" ☆ Greenhouse Effect 🏡 \n☆ Industrial effect {air polution, plastic waste, etc} 🏭 \n☆ Increased fuel consumption ⛽ \n☆ forest fires 🌳🔥")
@bot.command()
async def impacts(ctx):
    await ctx.send(" ☆ Hotter temperatures ♨️ \n ☆ More intense storms 🌪️ \n ☆ Increased drought \n ☆ Temperature and sea level rise 🌡️ \n ☆  Loss of species 🐾 \n ☆ More health risks 🤒🚑 \n ☆ Food shortages 🥐 \n ☆ Poverty and displacement 🏘️")
@bot.command()
async def countermeasures(ctx):
    await ctx.send(" ☆ Environmental conservation 🌱 \n ☆ Reduce electricity/energy usage 🔌⚡ \n ☆ Apply Reduce, Reuse, Recycle ♻️ \n ☆ Managing waste wisely 🗑️")
@bot.command()
async def zahra(ctx, count_heh = 5):
    await ctx.send("zahra 🥐" * count_heh)
bot.run("MTEyMTc5MDA5NDE2OTM1MDIyNQ.G8Foyv.BR40Lis1YIWvkcDnRUnnWrNNGlPBkNw_lwjYU4")
