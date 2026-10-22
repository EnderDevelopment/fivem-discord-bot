import discord
import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
FIVEM_SERVER_IP = os.getenv('FIVEM_SERVER_IP')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.command(name='online', help='Wyświetla liczbę osób online na serwerze FiveM')
async def online(ctx):
    try:
        response = requests.get(f'http://{FIVEM_SERVER_IP}/players.json')
        response.raise_for_status()
        players = response.json()
        online_count = len(players)
        await ctx.send(f'Liczba osób online na serwerze FiveM: {online_count}')
    except requests.exceptions.RequestException as e:
        await ctx.send(f'Błąd podczas pobierania liczby osób online: {e}')

bot.run(TOKEN)