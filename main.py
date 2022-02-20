import os
import json
import discord
from discord.ext import commands

with open("./Config/config.json", "r") as f:
    config = json.load(f)

token = config["token"]
prefix = config["prefix"]

IPLocator = commands.Bot(command_prefix = prefix, case_insensitive = True, help_command = None)

@IPLocator.event
async def on_ready():
    print(f"{IPLocator.user} em {len(IPLocator.guilds)} servers!")
    print(f"Prefix: {prefix}")
    print(f"Command: {prefix}iplocator or(ou) {prefix}locator")

    await IPLocator.change_presence(
        activity = discord.Activity(
            type = discord.ActivityType.listening,
            name = f"Use {prefix}iplocator"
        )
    )

def load_commands():
    for file in os.listdir("Commands"):
        if (file.endswith(".py")):
            commandFile = file[:-3]
            IPLocator.load_extension(f"Commands.{commandFile}")

if (__name__ == "__main__"):
    load_commands()
    IPLocator.run(token)