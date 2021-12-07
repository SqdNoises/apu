# APU Utils - nextcord bot
# Importing Packages
print('Importing packages...')
print('  - Importing nextcord (fork of discord.py)...')
import nextcord
print('  - Importing asyncio...')
import asyncio
print('  - Importing os...')
import os
print('  - Importing random...')
import random
print('  - Importing getpass...')
import getpass
print('  - Importing socket...')
import socket
print('Packages imported.')
# Importing Functions
print('\nImporting functions..')
print('  - Importing environ (from environ.py)...')
import environ
print('Functions imported.\n')

# environ.token, os.getenv - setting and getting token
environ.token()
print('Setting bot token from environmental variables...')
never_gonna_give_you_up = os.getenv('TOKEN')
print('Done.\n')

# Nextcord Client
print('Assigning `client` to `nextcord.Client()` with all intents...')
client = nextcord.Client(intents=nextcord.Intents.all())
print('Done.\n')

# Getting user and host
print('Getting username and hostname and setting it in \'userHost\' variable...')
u = getpass.getuser()
H = socket.gethostname()
userHost = u + '@' + H
print('Done.\n')

# on ready
@client.event
async def on_ready():
    wait = asyncio.sleep
    print(f'Connected to Discord!')
    print(f'Logged in as {str(client.user)}!')
    print(f'Running on {userHost}!')
    print('')

# NEXTCORD.UI
# pingpong
class pingpong(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label='Pong! 🏓', style=nextcord.ButtonStyle.red)
    async def pingpong(self, button: nextcord.ui.Button, interaction: nextcord.Interaction): await interaction.response.send_message("**Here's the link to the pong game:** https://github.com/flightcrank/pong 🏓\n\n*open source btw, || it's obvious lol ||*", ephemeral=True)

# pingpong_disabled
class pingpong_disabled(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label='Pong! 🏓', style=nextcord.ButtonStyle.red, disabled=True)
    async def pingpong(self, button: nextcord.ui.Button, interaction: nextcord.Interaction): pass

# on_message
@client.event
async def on_message(message):
    # pingpong
    if message.content == 'pingpong':
        view = pingpong()
        t = await message.reply('**Ping... Pong!** 🏓', view=view)
        await asyncio.sleep(5)
        view = pingpong_disabled()
        await t.edit('**Ping... Pong!** 🏓', view=view)

# logging into APU Utils
print("Logging into APU Utils...\n\n")
client.run(never_gonna_give_you_up)