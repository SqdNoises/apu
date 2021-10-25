# APU Utils - discord bot
# Importing Packages
print('Importing packages...')
print('Importing discord...')
import discord
print('Importing asyncio...')
import asyncio
print('Importing os...')
import os
print('Importing random...')
import random
print('Packages imported.')
# Importing Modules
print('Importing modules...')
print('Importing environ (from environ.py)...')
import environ
print('Modules imported.')

# os.getenv - setting and getting token
environ.token()
print('Setting bot token from environmental variables...')
never_gonna_give_you_up = os.getenv('TOKEN')
print('Done.')

# Discord Client
print('Assigning `client` to `discord.Client()`...')
client = discord.Client(intents=discord.Intents.all())
print('Done.')

# on_ready
@client.event
async def on_ready():
    reloadinfo = os.getenv('reloadinfo')
    channel = os.getenv('channel')
    if channel != None:
        channel = client.get_channel(int(channel))
    user = str(client.user)
    os.system('clear')
    print('Logged in! (' + user + ')')
    print("")
    print("Setting Status...")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."), status=discord.Status.idle)
    os.system("clear")
    print('Logged in! (' + user + ')')
    print("")
    print("Status Set.")
    print("")
    if reloadinfo == 'reloading':
        await channel.send('**Reloaded!**')
        os.environ['reloadinfo'] = 'reloaded'
        print('Reloaded!')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you. Reloaded!"), status=discord.Status.idle)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."), status=discord.Status.idle)
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you. Connected!"), status=discord.Status.idle)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."), status=discord.Status.idle)

# on_message
@client.event
async def on_message(message):
    # shortcuts
    msg = message.content
    sendmsg = message.channel.send
    author = message.author
    mention = message.author.mention
    reply = message.reply
    typing = message.channel.trigger_typing
    delete = message.delete
    wait = asyncio.sleep
    lowmsg = msg.lower()
    edit = message.edit
    react = message.add_reaction
    i = -1
    
    # admins
    admins = [840644782673100870, 842457844724400142, 884099213615587338, 477683725673693184]
    mods = [840644782673100870, 842457844724400142, 884099213615587338, 477683725673693184]
    
    # main
    # if author is bot itself
    if author == client.user:
        if i == 1:
            pass
        else:
            return
    
    # admin commands
    if msg == 'os!helpadmin' or msg == 'os!ha' or msg == 'os!admin':
        if author.id in admins:
            try:
                channel = await author.create_dm()
                await channel.send('''```py
# Admin Commands - Admin Help - APU Utils
# Prefix: os!
"os!helpadmin" - Sends you a DM with the Admin Commands Page

# Fun
"os!deadchat" - Sends a dead chat meme after deleting your message

# Bot Related
"os!reload" - Reloads the bot's code
"os!killprocess" - Kills the bot's process
"os!test" - tests done by sqd
```
```py
# Command Aliases - Admin Help - APU Utils
# Prefix: os!
"os!helpadmin" - os!ha, os!admin
"os!reload" - os!r
"os!killprocess" - os!kp
```''')
                await react('<a:GreenCheck:901802575052025917>')
                await reply('Check your DMs!')
            except Exception as e:
                await reply('Couldn\'t DM you! Please make sure to have your DMs enabled!\n**`Exception: `**`' + str(e) + '`')
        
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')

    if msg == 'os!deadchat':
        await delete()
        await sendmsg('Dead chat...', file=discord.File('files/media/dead-chat.mp4'))

    if msg == 'os!reload' or msg == 'os!r':
        if author.id in admins:
            channel = message.channel.id
            os.environ['reloadinfo'] = 'reloading'
            os.environ['channel'] = str(channel)
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('**Reloading...**')
            print('Reloading Bot...')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nobody. Reloading!"), status=discord.Status.dnd)
            os.system('python3 ~/workspace/apu/main.py')
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!killprocess' or msg =='os!kp':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('**Killing my process...**')
            print('Process Killed.')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nobody. Process killed."), status=discord.Status.dnd)
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
            
    if msg == 'os!test':
        if author.id in admins:
            print('os!test called.')
            try:
                await react('<a:Animated_Checkmark:901803000861966346>')
                await reply('Check my console!')
            except Exception as e:
                await react('<a:no:901803557014077480>')
                await reply('<a:no:901803557014077480> **`Exception: `**`' + str(e) + '`')
    
    # mod commands
    if msg.startswith('os!modcheck'):
        if author.id in mods:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await sendmsg('<a:Animated_Checkmark:901803000861966346> **You are whitelisted as a mod!**')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as a mod!**')

    # non-admin-mod
    if msg == 'os!help':
        await reply('''```py
# Commands - Help - APU Utils
# Prefix: os!
"os!help" - Replies with a list of commands

### More public commands cooming soon (hopefully) ###
```''')

    if 'closed-source' in lowmsg or 'closed source' in lowmsg:
        await reply('**Proprietary software** is **__bad__** for your **health** and **privacy**')

    if lowmsg == ':gigachad:':
        await reply('Here, lemme help you.')
        await sendmsg('<:gigachad:901804317512720394>')

    if 'gigachad' in lowmsg or 'giga chad' in lowmsg or 'i use arch btw' in lowmsg or 'i use debian btw' in lowmsg or 'i use mint btw' in lowmsg or 'i use garuda btw' in lowmsg:
        await react('<:gigachad:901804317512720394>')
    
    if lowmsg == 'manjaro':
        await sendmsg('<:manjaro:901827004704374854>')
    
    if lowmsg == 'kali':
        await sendmsg('<:kali:901833149644963870>')

    if lowmsg == 'arch':
        await sendmsg('<:arch:901825671746166845>')
    
    if lowmsg == 'debian':
        await sendmsg('<:debian:901826706107686982>')
    
    if lowmsg == 'mint':
        await sendmsg('<:mint:901826533537247334>')

    if lowmsg == 'your mom':
        await reply('what?')
    
    if lowmsg == 'uwu':
        await reply('owo')
    
    if lowmsg == 'owo':
        await reply('uwu')
    
    if lowmsg == 'hack' or lowmsg == 'hacked':
        await reply(file=discord.File('files/media/hacc.gif'))

# on member join
@client.event
async def on_member_join(member):
    print('member joined')
    channel = client.get_channel(901761695033212939)
    sendmsg = channel.send
    greets = ['just arrived! Say hi!', 'just joined the Anti Proprietary Union!', 'is now Open-Source Gang.', 'just landed.', 'joined! Say hi!', 'just joined the Open-Source Gang!']
    n = len(greets) - 1
    num = random.randint(0, n)
    greet = greets[num]
    await sendmsg(f'{member} ' + greet)

# on member leave
@client.event
async def on_member_remove(member):
    print('member left')
    channel = client.get_channel(901761742609219595)
    sendmsg = channel.send
    byelist = ['just left the Anti Proprietary Union!', ' is now closed-source gang.', 'just left the server! (Closed-source gang??)', 'just left!']
    n = len(byelist) - 1
    num = random.randint(0, n)
    bye = byelist[num]
    await sendmsg(f'{member} ' + bye)

# logging into APU Utils
print("Logging into APU Utils...")
client.run(never_gonna_give_you_up)