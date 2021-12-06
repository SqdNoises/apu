# Goffy's Bot - nextcord bot
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
class selectGender(nextcord.ui.Select):
    def __init__(self):
        genders = [
            nextcord.SelectOption(label='Male', emoji='♂️'),
            nextcord.SelectOption(label='Female', emoji='♀️'),
            nextcord.SelectOption(label='Custom', emoji='<:cursed_flushed:914769560043946025>')
        ]
        super().__init__(placeholder='Select your gender', min_values=1, max_values=1, options=genders)
    
    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'Gave you the role **`{self.values[0]}**`.', ephemeral=True)

class selectGenderView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(selectGender())

# on_message
@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg == 'gender':
        view = selectGenderView()
        await message.channel.send('**Select your Gender!**', view=view)

# logging into Goffy's Bot
print("Logging into Goffy\'s Bot...\n\n")
client.run(never_gonna_give_you_up)