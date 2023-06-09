## TODO ## 
# - Add a command to change the prefix


import discord
import logging

from discord.ext import commands
from dotenv      import load_dotenv
from os          import getenv

i = 0

for str in ["commands.moderation.essential.ban", 
            "commands.moderation.essential.unban",
            "commands.moderation.essential.kick",
            "commands.misc.spam",
            "commands.util.avatar", 
            "commands.util.clear",
            "commands.util.whois",
            "commands.ai.ask",
            "commands.help",
            "commands.moderation.warnings.warn",
            "commands.moderation.warnings.warns",
            "commands.moderation.warnings.cw",
            "commands.moderation.tickets.ticket",
            "commands.moderation.tickets.close",
            "commands.moderation.tickets.remove",
            "commands.moderation.tickets.add",
            "commands.moderation.purge",
            "commands.moderation.lock",
            "commands.moderation.auto.autorole",
            "commands.moderation.role",
            "commands.moderation.nuke",
            "commands.util.embed",
            "commands.util.ping",
            "commands.music.join",
            "commands.music.play",
            "commands.fun.eightball",
            "commands.fun.economy",
            "commands.util.invite",
            "commands.util.timestamp",
            "commands.util.list",
            "commands.fun.snipe",
            ]:
    
    
    i += 1
    exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")
    
print(f"loaded {i} cogs")    

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

activity = discord.Activity(type=discord.ActivityType.watching, name="nothing.")

Cloud = commands.Bot(command_prefix='$', intents=intent, activity=activity)

Cloud.remove_command('help')

for cog in [
    BanCog,
    UnbanCog, 
    KickCog,
    SpamCog,
    AvatarCog,
    ClearCog,
    WhoisCog,
    AskCog,
    HelpCog,
    WarnCog,
    WarnsCog,
    CwCog,
    TicketCog,
    CloseCog,
    AddCog,
    RemoveCog,
    PurgeCog,
    LockCog,
    AutoroleCog,
    RoleCog,
    NukeCog,
    EmbedCog,
    JoinCog,
    PlayCog,
    EightballCog,
    EconomyCog,
    PingCog,
    InviteCog,
    TimestampCog,
    ListCog,
    SnipeCog,
    ]:
    
    Cloud.add_cog(cog(Cloud))


# I had 20gb of logs in codespaces, resolving this now...

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

load_dotenv()

TOKEN = getenv("TOKEN")
Cloud.run(TOKEN)