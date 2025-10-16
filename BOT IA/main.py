import discord
from discord.ext import commands
from modelo import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def verificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            file_name = archivo.filename
            archivo_url = archivo.url
            await archivo.save(f'./img/{file_name}')
            await ctx.send(f'Su imagen se almaceno en: ./{archivo_url}')
            class_name, confidence_score = get_class(f'./img/{file_name}')
            confidence_score = confidence_score*100
            await ctx.send(f'***Clase:** {class_name} \n **Predicción:** {confidence_score:.0f}')
    else:
        await ctx.send('No envio ninguna imagen :,D')

bot.run("TUTOKEN")
