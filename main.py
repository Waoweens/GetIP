import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from mcstatus import JavaServer

load_dotenv(".env")
token = os.environ["TOKEN"]
prefix = os.environ["PREFIX"]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user} (ID {bot.user.id})")


@bot.command(description="Sends bot round-trip latency.")
async def ping(ctx):
	await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command(description="Sends server status.")
async def status(ctx):
	await ctx.send("tmp")

bot.run(token)
