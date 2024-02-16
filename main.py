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
    await ctx.send("Pemanasan global adalah peningkatan suhu rata-rata atmosfer, lautan, dan daratan Bumi yang menyebabkan perubahan iklim di sekitar kita. 🌍🔥")
@bot.command()
async def kondisi(ctx):
    await ctx.send("Suhu global Bumi saat ini lebih panas 2°-3° C! 😱")
@bot.command()
async def penyebab(ctx):
    await ctx.send("Efek Rumah Kaca 🏡 \n ☆ Efek industri {polusi udara, sampah plastik, dll} 🏭 \n ☆ Peningkatan konsumsi bahan bakar ⛽ \n ☆ kebakaran hutan 🌳🔥")
@bot.command()
async def dampak(ctx):
    await ctx.send("Suhu yang lebih panas ♨️ \n ☆ Badai yang lebih hebat 🌪️ \n ☆ Meningkatnya kekeringan \n ☆ Kenaikan suhu dan permukaan air laut 🌡️ \n ☆ Hilangnya spesies 🐾 \n ☆ Lebih banyak risiko kesehatan 🤒🚑 \n ☆ Kekurangan makanan 🥐 \n ☆ Kemiskinan dan pengungsian 🏘️")
@bot.command()
async def penanggulangan(ctx):
    await ctx.send("Pelestarian lingkungan 🌱 \n ☆ Mengurangi penggunaan listrik/energi 🔌⚡ \n ☆ Menerapkan Kurangi, Gunakan Kembali, Daur Ulang ♻️ \n ☆ Mengelola sampah dengan bijak 🗑️")

bot.run("Bot token in here!")
