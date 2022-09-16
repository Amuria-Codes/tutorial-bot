import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()

activity = discord.Activity(type=discord.ActivityType.watching, name="Coding Keks")
status = discord.Status.dnd

bot = discord.Bot(
    intents=intents,
    debug_guilds=[123456789],  # hier server id einfügen
    activity=activity,
    status=status
)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("TOKEN"))
