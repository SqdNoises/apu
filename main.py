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
client = discord.Client()
print('Done.')

# on_ready
@client.event
async def on_ready():
    user = str(client.user)
    os.system('clear')
    print('Logged in! (' + user + ')')
    print("")
    print("Setting Status...")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"), status=discord.Status.idle)
    os.system("clear")
    print('Logged in! (' + user + ')')
    print("")
    print("Status Set.")
    print("")

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
    
    # main
    # if author is bot itself
    if author == client.user:
        return
    
    # admin commands
    if msg == 'os!reload':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('> **Reloading...**')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nobody. Reloading!"), status=discord.Status.dnd)
            os.system('python3 apu/main.py')
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!killprocess' or msg =='os!kp':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('> **Killing my process...**')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nobody. Process killed."), status=discord.Status.dnd)
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!jl':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    #if author.id in admins:
        #emojibool = 
    
    if msg == 'os!test':
        if author.id in admins:
            print('os!test called.')
            emojis = message.guild.emojis
            print(emojis)
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('Check my console!')
    
    # non-admin
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
    byelist = ['just left the Anti Proprietary Union!', ' is now closed-source gang.', 'just left the server! (Closed-source gang??)']
    n = len(byelist) - 1
    num = random.randint(0, n)
    bye = byelist[num]
    await sendmsg(f'{member} ' + bye)

# logging into APU Utils
print("Logging into APU Utils...")
client.run(never_gonna_give_you_up)