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

# environ.token, os.getenv - setting and getting token
environ.token()
print('Setting bot token from environmental variables...')
never_gonna_give_you_up = os.getenv('TOKEN')
print('Done.')

# Discord Client
print('Assigning `client` to `discord.Client()` with all intents...')
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
     
     # checks if message is from guild
    if message.guild == None:
       if msg.startswith('os!'):
           await react('<a:no:901803557014077480>')
           await reply('<a:no:901803557014077480> **You cannot use my commands in DMs!**')
           return
       else:
           rand = random.randint(0, 100)
           rand2 = random.randint(0, 100)
           if rand == rand2:
               await sendmsg('You cannot use my messages in DMs!\n\nFun Fact:\n*There\'s a 1in 100 chance that you are seeing this message!')
           return
     
    # admin commands
    if msg == 'os!helpadmin' or msg == 'os!ha' or msg == 'os!admin':
        if author.id in admins:
            try:
                channel = await author.create_dm()
                await channel.send('''Here are my commands and aliases for commands.
```py
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
                await react('<a:no:901803557014077480>')
                await reply('Couldn\'t DM you! Please make sure to have your DMs enabled!\n**`Exception: `**`' + str(e) + '`')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')


    if msg == 'os!deadchat':
        if author.id in admins:
            await delete()
            await sendmsg('Dead chat...', file=discord.File('files/media/dead-chat.mp4'))
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')

    if msg == 'os!reload' or msg == 'os!r':
        if author.id in admins:
            channel = message.channel.id
            os.environ['reloadinfo'] = 'reloading'
            os.environ['channel'] = str(channel)
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('**Reloading...**')
            print('Reloading Bot...')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nobody. Reloading!"), status=discord.Status.dnd)
            os.system('python3 main.py')
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

    if msg == 'os!checkthepins' or msg == 'os!ctp':
        if author.id in admins:
            await delete()
            await sendmsg('<a:ctp:901802005230661662>')
        else:
            await reply('**no.**')

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
"os!fosslist" - Replies with some useful FOSS alternative lists
"os!source" - Replies with the link to source code for APU Utils
"os!aliases" - Replies with aliases to commands
"os!distros" - Replies with a list of linux distros.

### More public commands cooming soon (hopefully) ###
```''')

    if msg == 'os!aliases':
        await reply('''```py
# Aliases - APU Utils
# Prefix: os!
"os!source" - os!sourcecode, os!source-code, os!sc, os!code
```''')

    if msg == 'os!fosslist':
        await reply('''> **Useful lists with FOSS alternatives and software:**
<https://privacytools.io> -- **FOSS** and private alternatives to proprietary crap.
<https://opensource.builders> -- Tool to find **FOSS** alternatives to proprietary software you might use.
*Also allows you to specify the programming language and license.*''')
    if msg == "os!distros":
        await reply('''> **For begginers**
**Zorin OS** -- Windows look-alike, very user friendly | <https://zorin.com/os>
**Deepin** -- macOS look-alike, also user friendly | <https://deepin.org/en>
> **For advanced users**
**Arch Linux** -- DIY Keep-it-simple distro with a huge repository | <archlinux.org>
**KISS Linux** -- Very simple DIY metadistro, hard to install | <https://kisslinux.org>
**Void Linux** -- A distro with the option to be completely GNUless | <https://voidlinux.org>''')

    if msg.startswith('os!sc') or msg.startswith('os!sourcecode') or msg.startswith('os!source-code') or msg.startswith('os!source') or msg.startswith('os!code'):
        await reply('shut up and here\'s my code: <https://github.com/SqdNoises/apu>')

    if 'closed source suck' in lowmsg or 'closed-source suck' in lowmsg or 'closed source is bad' in lowmsg or 'closed-source is bad' in lowmsg or 'closed-source bad' in lowmsg or 'closed source bad' in lowmsg or lowmsg == 'closed-source = bad' or lowmsg == 'closed source = bad' or lowmsg == 'proprietary = bad' or lowmsg == 'proprietary software = bad' or lowmsg == 'closed-source == bad' or lowmsg == 'closed source == bad' or lowmsg == 'proprietary == bad' or lowmsg == 'proprietary software == bad':
        await reply('Agreed.')
        return

    if 'proprietary suck' in lowmsg and 'anti-proprietary' not in lowmsg and 'anti proprietary' not in lowmsg and 'not proprietary' not in lowmsg:
        await reply ('Agreed.') 
        return

    if 'proprietary is bad' in lowmsg and 'anti-proprietary' not in lowmsg and 'anti proprietary' not in lowmsg and 'not proprietary' not in lowmsg:
        await reply ('Agreed.') 
        return

    if 'proprietary bad' in lowmsg and 'anti-proprietary' not in lowmsg and 'anti proprietary' not in lowmsg and 'not proprietary' not in lowmsg:
        await reply ('Agreed.') 
        return

    if 'open-source > closed-source' in lowmsg or 'open source > closed source' in lowmsg or 'open-source > closed source' in lowmsg or 'open source > closed-source' in lowmsg or 'closed-source < open-source' in lowmsg or 'closed source < open source' in lowmsg or 'closed-source < open source' in lowmsg or 'closed source < open-source' in lowmsg:
        await reply('Agreed!')
        return
    
    if 'open-source < closed-source' in lowmsg or 'open source < closed source' in lowmsg or 'open-source < closed source' in lowmsg or 'open source < closed-source' in lowmsg or 'closed-source > open-source' in lowmsg or 'closed source > open source' in lowmsg or 'closed-source > open source' in lowmsg or 'closed source > open-source' in lowmsg:
        await reply('You want to die?')
        return

    if 'closed-source' in lowmsg or 'closed source' in lowmsg:
        await reply('**Proprietary software** is **__bad__** for your **health** and **privacy**')
        
    if 'proprietary' in lowmsg and 'anti-proprietary' not in lowmsg and 'antiproprietary' not in lowmsg and 'anti proprietary' not in lowmsg and 'not proprietary' not in lowmsg and 'closed-source' not in lowmsg and 'closed source' not in lowmsg:
        await reply('**Proprietary software** is **__bad__** for your **health** and **privacy**')

    if lowmsg == ':gigachad:':
        await reply('Here, lemme help you.')
        await sendmsg('<:gigachad:901804317512720394>')

    if 'gigachad' in lowmsg and ':gigachad:' not in lowmsg or 'giga chad' in lowmsg or 'i use arch btw' in lowmsg or 'i use debian btw' in lowmsg or 'i use mint btw' in lowmsg or 'i use garuda btw' in lowmsg:
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
     
    # "cum" stands for client user mention, please dont end me ;-;
    cum = client.user.mention
    cumstr = str(client.user.mention)
    cum2 = cum.replace('<@', '<@!')

    if client.user.mention in msg or cum2 in msg:
            if msg == cum or msg == cum2:
                await reply('''```py
Hi! I am APU Utils.
# indev
```''')
            elif cum in msg or cum2 in msg:
                if 'are you watching me' or 'are u watching me' or 'are you fucking watching me' or 'are u fucking watching me':
                    await reply('I\'m watching you.')

    if msg == '<@&903299738542161962>':
        await reply('You\'re pinging my integration role, you dummy dumbo head.')

    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa pee you you tils'):
        await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa p u u tils'):
        await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa pu utils'):
        await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaapu utils'):
        await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')

# on member join
@client.event
async def on_member_join(member):
    print(f'{member} joined')
    channel = await member.create_dm()
    try:
        await channel.send('Hello ' + member.mention + '!\nWelcome to **Anti Proprietary Union**!\n__Here\'s what you should do to get started__:\n> Read the rules to avoid getting punished. (<#901519584102854687>)\n> Talk in <#901860174539677706> chat!\nHope you have fun in our server.\n**Server invite:** https://discord.gg/7bDvDnpUZC\n\n**#open-source-gang** ❤️')
        print('dm greet sent to ' + f'{member}')
    except Exception as e:
        print('failed to dm greet ' + f'{member}')
        print(str(e))
    channel = client.get_channel(901761695033212939)
    greets = ['just arrived! Say hi!', 'just joined the Anti Proprietary Union!', 'is now open-source gang.', 'just landed.', 'joined! Say hi!', 'just joined the open-source gang!', 'is now open-source gang!']
    n = len(greets) - 1
    num = random.randint(0, n)
    greet = greets[num]
    await channel.send(f'{member.mention} ' + greet)
    print('alerted the server for member join (' + f'{member})')

# on member leave
@client.event
async def on_member_remove(member):
    print(f'{member} left')
    channel = client.get_channel(901761742609219595)
    sendmsg = channel.send
    byelist = ['just left the Anti Proprietary Union!', 'is now closed-source gang.', 'just left the server! (Closed-source gang??)', 'just left!', 'is a proprietary software user!', 'left. Do they not like open-source software??']
    n = len(byelist) - 1
    num = random.randint(0, n)
    bye = byelist[num]
    await sendmsg(f'{member} ' + bye)
    print('alerted the server for member leave (' + f'{member})')

# logging into APU Utils
print("Logging into APU Utils...")
client.run(never_gonna_give_you_up)
