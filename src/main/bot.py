##################################################
##########
# Bot INIT file

# my audimar piguette worth the gdp of yemen if this watch breaks the foreign exchange market will take a 28 percent hit people will DIE
##########
##################################################

# IMPORTS
##########
from disnake.ext import commands
from dotenv import load_dotenv
import os


# INIT
##########
bot = commands.InteractionBot()
load_dotenv()

# COMMANDS
##########
@bot.slash_command()
async def hello(inter):
    await inter.response.send_message('shut it bitch')

# RUN
##########
bot.run(os.getenv("BOT_TOKEN"))