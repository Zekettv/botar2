import discord
from discord.ext import commands
import os
import asyncio
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix="'")
client = discord.Client()

@client.event
async def on_ready():
 print(f"Tamo activo {client.user}")


bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))



bot.run("MTAwMzA4Njk4MjYzOTAwOTgyMg.G6v4lR.dQlXCixNZUiPQe8nGmwn1jI9ReDuWeEuzxPslQ")
#bot.run(os.getenv("TOKEN"))
