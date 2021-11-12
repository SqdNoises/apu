# APU Utils - nextcord bot
# Importing Packages
print('Importing packages...')
print('Importing nextcord (fork of discord.py)...')
import nextcord
print('Importing asyncio...')
import asyncio
print('Importing os...')
import os
print('Importing random...')
import random
print('Importing getpass...')
import getpass
print('Importing socket...')
import socket
print('Importing time...')
import time
print('Importing json...')
import json
print('Packages imported.')
# Importing Functions
print('Importing functions..')
print('Importing environ (from environ.py)...')
import environ
print('Functions imported.')

# environ.token, os.getenv - setting and getting token
environ.token()
print('Setting bot token from environmental variables...')
never_gonna_give_you_up = os.getenv('TOKEN')
print('Done.')

# Nextcord Client
print('Assigning `client` to `nextcord.Client()` with all intents...')
client = nextcord.Client(intents=nextcord.Intents.all())
print('Done.')

# Getting user and host
print('Getting username and hostname and setting it in \'userHost\' variable...')
u = getpass.getuser()
H = socket.gethostname()
userHost = u + '@' + H
print('Done.')

# Clearing the messy terminal
os.system('clear')

# on_ready
@client.event
async def on_ready():
    rldsts = os.getenv('rldsts')
    logchannel = client.get_channel(902785006173315072)
    if rldsts == 'connection lost':
        os.environ['`Re-connected (Re-connect after losing connection)`']
        reloadstat = os.getenv('rldsts')
        await logchannel.send(f'> **Connected to Discord!**\n**Running on**: {userHost}\n**Status**: {reloadstat}\n**Latency**: {round(client.latency * 1000)}ms')
    else:
        os.environ['rldsts'] = '`Connected`'
    reloadinfo = os.getenv('reloadinfo')
    channel = os.getenv('channel')
    if channel != None:
        channel = client.get_channel(int(channel))
    user = str(client.user)
    print('Logged in! (' + user + ')')
    print('Running on `' + userHost + '`!')
    print("")
    print("Setting Status...")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you."), status=nextcord.Status.idle)
    print("Status Set.")
    print("")
    if reloadinfo == 'reloading':
        await channel.send('**Reloaded!**')
        os.environ['rldsts'] = '`Reloaded`'
        os.environ['reloadinfo'] = 'reloaded'
        print('Reloaded!')
        reloadstat = os.getenv('rldsts')
        await logchannel.send(f'> **Connected to Discord!**\n**Running on**: {userHost}\n**Status**: {reloadstat}\n**Latency**: {round(client.latency * 1000)}ms')
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you. Reloaded!"), status=nextcord.Status.idle)
        await asyncio.sleep(5)
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you."), status=nextcord.Status.idle)
    else:
        if rldsts == 'connection lost':
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you. Re-connected!"), status=nextcord.Status.idle)
            await asyncio.sleep(5)
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you."), status=nextcord.Status.idle)
        else:
            reloadstat = os.getenv('rldsts')
            await logchannel.send(f'> **Connected to Discord!**\n**Running on**: {userHost}\n**Status**: {reloadstat}\n**Latency**: {round(client.latency * 1000)}ms')
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you. Connected!"), status=nextcord.Status.idle)
            await asyncio.sleep(5)
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="you."), status=nextcord.Status.idle)

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
    cum = client.user.mention
    cumstr = str(client.user.mention)
    cum2 = cum.replace('<@', '<@!')
    
    # sqd
    sqd = 477683725673693184
    # admins
    admins = [840644782673100870, 842457844724400142, 884099213615587338, 477683725673693184]
    #mods
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
           rand = random.randint(0, 9)
           rand2 = random.randint(0, 9)
           if rand == rand2:
               await sendmsg('**You cannot use my commands in DMs!**\n\nFun Fact:\n*There\'s a 1 in 100 chance that you are seeing this message!*')
           return
     
    # sqd commands
    if msg.startswith('os!die'):
        if author.id == sqd:
            if msg == 'os!die':
                await reply('ok, you\'re dead. now what?')
            elif msg.startswith('os!die '):
                user = msg.split('os!die ', 1)[1]
                await sendmsg(user + ', death.')
        else:
            await reply('special sqd-only command uwu')
        return
    
    if msg == 'os!clear':
        if author.id == sqd:
            await reply('**Clearing your *messy* console screen...**')
            os.system('clear')
            await sendmsg('**Cleared!**')
        else:
            await reply('special sqd-only command uwu')
    
    # admin commands
    if msg == 'os!admincheck':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await sendmsg('<a:Animated_Checkmark:901803000861966346> **You are whitelisted as an admin!**')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
            
    if msg == 'os!helpadmin' or msg == 'os!ha' or msg == 'os!admin':
        if author.id in admins:
            try:
                channel = await author.create_dm()
                await channel.send('''Here are my commands and aliases for commands.
```py
# Admin Commands - Admin Help - APU Utils
# Prefix: os!
"os!helpadmin" - Sends you a DM with the Admin Commands Page
"os!helpmod" - Sends you a DM with the Mod Commands Page
"os!help" - Replies with a list of Public Commands
"os!admincheck" - Checks if you are whitelisted as an admin or not.

# Moderation
"os!userinfo <id>" (where <id> is the member id) - Replies with the info of the member id mentioned

# Fun
"os!deadchat" - Sends a dead chat meme after deleting your message

# Bot Related
"os!reload" - Reloads the bot's code
"os!killprocess" - Kills the bot's process
"os!test" - tests done by sqd
"os!ping" - Checks the ping/latency of the bot
"os!instance" - Shows `username@hostname` of the device the bot is running on
```
```py
# Command Aliases - Admin Help - APU Utils
# Prefix: os!
"os!helpadmin" - os!ha, os!admin
"os!reload" - os!r
"os!killprocess" - os!kp
"os!ping" - os!latency
```''')
                await react('<a:GreenCheck:901802575052025917>')
                await reply('Check your DMs!')
            except Exception as e:
                await react('<a:no:901803557014077480>')
                await reply('Couldn\'t DM you! Please make sure to have your DMs enabled!\n**`Exception: `**`' + str(e) + '`')
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
            channel = client.get_channel(902785006173315072)
            await channel.send(f'**os!reload** called by an admin ({str(author)}). Reloading the bot!')
            print('Reloading Bot...')
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="nobody. Reloading!"), status=nextcord.Status.dnd)
            os.system('python3 main.py')
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!killprocess' or msg =='os!kp':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('**Killing my process...**')
            channel = client.get_channel(902785006173315072)
            await channel.send(f'**os!killprocess** called by an admin ({str(author)}). Killing the process!')
            print('Process Killed.')
            await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="nobody. Process killed."), status=nextcord.Status.dnd)
            os._exit(1)
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!clientclose' or msg =='os!cc':
        if author.id in admins:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await reply('**`client.close()`ing...**')
            channel = client.get_channel(902785006173315072)
            await channel.send(f'**os!clientclose** called by an admin ({str(author)}). `client.close()`ing!')
            print('Client Closed.')
            await client.close()
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg.startswith('os!proprietary') or msg.startswith('os!p'):
        if author.id in admins:
            if msg.startswith('os!proprietary ') or msg.startswith('os!p '):
                if msg.startswith('os!proprietary '):
                    msg = msg.split('os!proprietary ', 1)[1]
                    os.environ['msg'] = msg
                if msg.startswith('os!p '):
                    msg = msg.split('os!p ', 1)[1]
                    os.environ['msg'] = msg
                id = os.getenv('msg')
                try:
                    member = author.guild.get_member(int(id))
                    await member.edit(nick='proprieraryuser')
                    await reply(f'**Successfully proprieraried {member.mention}\'s nickname.**')
                except Exception as e:
                    await reply(f'usage: `os!proprietary <id>` where `<id>` is the user id of the member\n**`Exception:`**` {e}`')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg.startswith('os!ratio'):
        if author.id in admins:
            if msg == 'os!ratio':
                await delete()
                await sendmsg('ratio')
            if msg.startswith('os!ratio '):
                msg = msg.split('os!ratio ', 1)[1]
                idlist = msg.split(' ', 1)
                messageid = message.id
                if len(idlist) == 1:
                    try:
                        msgid = int(idlist[0])
                        message = await message.channel.fetch_message(msgid)
                        await message.reply('ratio')
                        message = await message.channel.fetch_message(messageid)
                        await message.delete()
                    except Exception as e:
                        await sendmsg(f'**`Exception:`**` {e}`\n**Usage**: `os!ratio <message id> [channel id]` where `<message id>` is the message id and `[channel id]` (optional) is the channel id of the message.')
                if len(idlist) == 2:
                    try:
                        msgid = int(idlist[0])
                        channelid = int(idlist[1])
                        channel = client.get_channel(channelid)
                        message = await channel.fetch_message(msgid)
                        await message.reply('ratio')
                    except:
                        await sendmsg(f'**`Exception:`**` {e}`\n**Usage**: `os!ratio <message id> [channel id]` where `<message id>` is the message id and `[channel id]` (optional) is the channel id of the message.')
        else:
            await reply('look, no one cares.')
            
    if msg == 'os!test':
        if author.id in admins:
            print('os!test called.')
            try:
                # test here
                
                ########
                await react('<a:Animated_Checkmark:901803000861966346>')
                await reply('Check my console!')
            except Exception as e:
                await react('<a:no:901803557014077480>')
                await reply('<a:no:901803557014077480> **`Exception: `**`' + str(e) + '`')
                
    # mod commands
    if msg == 'os!modcheck':
        if author.id in mods:
            await react('<a:Animated_Checkmark:901803000861966346>')
            await sendmsg('<a:Animated_Checkmark:901803000861966346> **You are whitelisted as a mod!**')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as a mod!**')
    
    if msg == 'os!helpmod' or msg == 'os!hm' or msg == 'os!mod':
        if author.id in mods:
            try:
                channel = await author.create_dm()
                await channel.send('''Here are my commands and aliases for commands.
```py
# Mod Commands - Mod Help - APU Utils
# Prefix: os!
"os!helpmod" - Sends you a DM with the Mod Commands Page
"os!help" - Replies with a list of Public Commands
"os!modcheck" - Checks if you are whitelisted as a mod or not

# Moderation
"os!userinfo <id>" (where <id> is the member id) - Replies with the info of the member id mentioned
"os!rules" - Sends a message with all the rules of the server.
"os!rule <rule number>" (where <rule number> is the rule number.) - Sends a message with the rule you specified

# Fun
"os!deadchat" - Sends a dead chat meme after deleting your message

# Bot Related
"os!ping" - Checks the ping/latency of the bot
"os!instance" - Shows `username@hostname` of the device the bot is running on
```
```py
# Command Aliases - Mod Help - APU Utils
# Prefix: os!
"os!helpmod" - os!hm, os!mod
"os!ping" - os!latency
```''')
                await react('<a:GreenCheck:901802575052025917>')
                await reply('Check your DMs!')
            except Exception as e:
                await react('<a:no:901803557014077480>')
                await reply('Couldn\'t DM you! Please make sure to have your DMs enabled!\n**`Exception: `**`' + str(e) + '`')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg == 'os!rules':
        if author.id in admins:
            await delete()
            await sendmsg('''> **Rules** (<#901519584102854687>)
**1)** NO PROPRIETARY SOFTWARE.
**2)** No bigotry
**3)** No slurs
**4)** No NSFW in non-NSFW channels
**5)** No illegal stuff
**6)** No arguing about stupid stuff
**7)** NO BEING UNFUNNY!!!
**8)** No spamming/chat flood
**9)** No advertising except in <#901860994446405692>, and even then, only advertise open-source stuff

*Not following these rules will result in a mute, warn or ban depending on the severity of the rule you break and which rule you broke.*''')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as an admin!**')
    
    if msg.startswith('os!rule '):
        if author.id in mods:
            try:
                rulelist = ['NO PROPRIETARY SOFTWARE.', 'No bigotry', 'No slurs', 'No NSFW in non-NSFW channels', 'No illegal stuff', 'No arguing about stupid stuff', 'NO BEING UNFUNNY!!!', 'No spamming/chat flood', 'No advertising except in <#901860994446405692>, and even then, only advertise open-source stuff']
                rule = msg.split('os!rule ', 1)[1]
                rulenum = int(rule) - 1
                rulestr = rulelist[rulenum]
                await sendmsg(f'> **Rule {rule}**\n   - {rulestr}')
                await delete()
            except:
                await reply('That rule number doesn\'t exist...')
    
    if msg.startswith('os!modnick'):
        if author.id in mods:
            if msg.startswith('os!modnick '):
                memid = msg.split('os!modnick ', 1)[1]
                try:
                    await delete()
                    member = author.guild.get_member(int(memid))
                    def modnickrnum():
                        rnum = random.randint(0, 9999999)
                        modnick = 'moderated nickname ' + str(rnum)
                        for member in message.guild.members:
                            if modnick == member.nick:
                                modnickrnum()
                        os.environ['modnick'] = modnick
                    modnickrnum()
                    modnick = os.getenv('modnick')
                    await member.edit(nick=modnick)
                    await sendmsg(f'> **Moderated the nickname to `{modnick}`.**')
                    # log it
                    channel = client.get_channel(902785006173315072)
                    await channel.send(f'''> **Nickname Moderated**
**Nickname moderated by**: `{author}` ({author.id})
**Nickname moderated for**: `{member}` ({member.id})
**Nickname moderated to**: {modnick}''')
                except Exception as e:
                    await sendmsg(f'**``Exception:``**` {e}`')
            else:
                await reply('Specify a user id you dumb dumb dumbo head.')
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as a mod!**')
            
    if msg.startswith('os!nick'):
        if author.id in mods:
            if msg.startswith('os!nick '):
                 memidnick = msg.split('os!nick ', 1)[1]
                 memlist = memidnick.split(' ', 1)
                 try:
                     memid = int(memlist[0])
                     member = author.guild.get_member(memid)
                     if len(memlist) == 1:
                         await member.edit(nick=None)
                         await reply('**Set the member\'s server nickname back to default.**')
                         # log it
                         channel = client.get_channel(902785006173315072)
                         await channel.send(f'''> **Nickname Changed** *(through `os!nick` command)*
**Nickname changed by**: `{author}` ({author.id})
**Nickname changed for**: `{member}` ({member.id})
**Nickname changed to**: `{member.name}` (Default Nickname)''')
                     if len(memlist) == 2:
                         memnick = memlist[1]
                         await member.edit(nick=memnick)
                         await reply(f'**Set the member\'s server nickname to `{memnick}`.**')
                         # log it
                         channel = client.get_channel(902785006173315072)
                         await channel.send(f'''> **Nickname Changed** *(through `os!nick` command)*
**Nickname changed by**: `{author}` ({author.id})
**Nickname changed for**: `{member}` ({member.id})
**Nickname changed to**: `{memnick}`''')
                 except Exception as e:
                      await reply(f'**`Exception:`**` {e}`')
            else:
                  await reply('Specify a user id you dumb dumb dumbo head.')
        else:
             await react('<a:no:901803557014077480>')
             await reply('<a:no:901803557014077480> **You are not whitelisted as a mod!**')
                 

    if msg == 'os!deadchat':
        if author.id in mods:
            await delete()
            await sendmsg('Dead chat...', file=nextcord.File('files/media/dead-chat.mp4'))
        else:
            await react('<a:no:901803557014077480>')
            await reply('<a:no:901803557014077480> **You are not whitelisted as a mod!**')
            
    if msg == 'os!checkthepins' or msg == 'os!ctp':
        if author.id in mods:
            await delete()
            await sendmsg('<a:ctp:901802005230661662>')
        else:
            await reply('**no.**')

    # non-admin-mod
    if msg == 'os!':
        xl = ['???', 'i would love it if you provide a command', 'u srs?', 'bruh specify a command-', '...', '*crickets start chirping*', 'ok', 'ok, you\'ve summoned me. now what?', '_ _', 'do you have brain?', 'if you\'re looking for my commands, do `os!help` instead of summoning me and wasting my time.', 'shut']
        n = len(xl) - 1
        num = random.randint(0, n)
        x = xl[num]
        await reply(x)
        
    if msg == 'os!help':
        await reply('''```py
# Commands - Help - APU Utils
# Prefix: os!
"os!help" - Replies with a list of commands
"os!aliases" - Replies with aliases to commands
"os!fosslist" - Replies with some useful FOSS alternative lists
"os!source" - Replies with the link to source code for APU Utils
"os!instance" - Shows `username@hostname` of the device the bot is running on
"os!ping" - Checks the ping/latency of the bot
"os!userinfo <id>" (where <id> is the member id) - Replies with the info of the member id mentioned
```''')

    if msg == 'os!aliases':
        await reply('''```py
# Aliases - APU Utils
# Prefix: os!
"os!source" - os!sourcecode, os!source-code, os!sc, os!code
"os!ping" - os!latency
```''')

    if msg == 'os!instance':
        await reply(f'Currently running on **{userHost}**.')
    
    if msg == 'os!ping' or msg == 'os!latency':
        await reply(f'<:bluegreen_network_bars:907868507927097405> **My ping:** {round(client.latency * 1000)}ms 🧽')
    
    if msg.startswith('os!userinfo'):
        if msg.startswith('os!userinfo '):
            memid = str(msg.split('os!userinfo ', 1)[1])
            try:
                member = author.guild.get_member(int(memid))
                await reply(f'''> **User info**
**Member**: `{member}`
**Member ID**: {member.id}
**Member Nickname**: `{member.nick}` *(value* `None` *could mean that the user has no nickname)*
**Created at**: {member.created_at} *(Time is in UTC)*
**Joined at**: {member.joined_at} *(Time is in UTC)*
**Bot**: {member.bot}
*Requested by {author.mention}*''')
            except Exception as e:
                await reply(f'**An error occured!**\nusage: `os!userinfo <id>`, where `<id>` is the user id of the member.\n\n**``Exception:``**` {e}`')
        else:
            await reply('usage: `os!userinfo <id>`, where `<id>` is the user id of the member.')

    if msg == 'os!fosslist':
        await reply('''> **Useful lists with FOSS alternatives and software:**
<https://privacytools.io> -- **FOSS** and private alternatives to proprietary crap.
<https://opensource.builders> -- Tool to find **FOSS** alternatives to proprietary software you might use.
*Also allows you to specify the programming language and license.*''')

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
        await reply(file=nextcord.File('files/media/hacc.gif'))
    
    if cum in msg or cum2 in msg:
            if msg == cum or msg == cum2:
                await reply(f'''```py
I am APU Utils, made by Sqd (/home/sqd).
# Prefix: os!
Coded on python using nextcord.

Ran on linux using the python3 package.
Currently running on `{userHost}`
```''')
            elif cum in msg or cum2 in msg:
                if 'are you watching me' in msg or 'are u watching me' in msg or 'are you fucking watching me' in msg or 'are u fucking watching me' in msg:
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
    
    if msg == '@/home/sqd':
        await reply(file=nextcord.File('files/media/--home-sqd.jpg'))

# on disconnect
async def on_disconnect():
    print(f'[{str(time.now)}] Lost Connection to Discord!')

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
    if member.bot == True:
        await sendmsg(f'A bot was invited! ({member})')
    else:
        await channel.send(f'{member.mention} ' + greet)
    print('alerted the server for member join (' + f'{member})')
    # log it
    channel = client.get_channel(902785006173315072)
    memcrt = member.created_at
    memcrtstr = str(memcrt)
    memjoin = member.joined_at
    memjoinstr = str(memjoin)
    membot = member.bot
    membotstr = str(membot)
    await channel.send(f'> **Member Joined,** ({member})\n**__{member.mention}__** joined.\n**ID**: {member.id}\n**Created at**: {memcrtstr}\n**Joined at**: {memjoinstr}\n**Bot**: {membotstr}')

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
    if member.bot == True:
        await sendmsg(f'A bot was removed! ({member})')
    else:
        await sendmsg(f'{member} ' + bye)
    print('alerted the server for member leave (' + f'{member})')
    # log it
    channel = client.get_channel(902785006173315072)
    memcrt = member.created_at
    memcrtstr = str(memcrt)
    memjoin = member.joined_at
    memjoinstr = str(memjoin)
    membot = member.bot
    membotstr = str(membot)
    memnick = member.nick
    if memnick == None:
        os.environ['memnick'] = '`No nickname`'
    else:
        os.environ['memnick'] = memnick
    memnickstr = os.getenv('memnick')
    await channel.send(f'> **Member Left,** ({member})\n**__{member.mention}__** left.\n**ID**: {member.id}\n**Server Nickname**: {memnickstr}\n**Created at**: {memcrtstr}\n**Joined at**: {memjoinstr}\n**Bot**: {membotstr}')

# on raw message delete
@client.event
async def on_raw_message_delete(payload):
    if payload.channel_id == 902785006173315072:
        return
    if payload.cached_message == None:
        logchannel = client.get_channel(902785006173315072)
        channel = client.get_channel(payload.channel_id)
        await logchannel.send(f'''> **Message Deleted**
**Message ID**: {payload.message_id}
**Channel**: #{channel.name} (<#{channel.id}>)
**Channel ID**: {channel.id}
**Cached**: False
» Cache details:
   • No details found, `NOT_CACHED`''')
    else:
        message = payload.cached_message
        logchannel = client.get_channel(902785006173315072)
        channel = client.get_channel(message.channel.id)
        try:
            os.environ['num'] = '0'
            os.environ['a1'] = '`None`'
            os.environ['a2'] = '`None`'
            os.environ['a3'] = '`None`'
            os.environ['a4'] = '`None`'
            os.environ['a5'] = '`None`'
            os.environ['a6'] = '`None`'
            os.environ['a7'] = '`None`'
            os.environ['a8'] = '`None`'
            os.environ['a9'] = '`None`'
            os.environ['a10'] = '`None`'
            for attachment in message.attachments:
                num = os.getenv('num')
                if num == None:
                    os.environ['num'] = '0'
                num = os.getenv('num')
                num = int(num) + 1
                A = 'a' + str(num)
                os.environ[A] = '<' + str(attachment.url) + '>'
                os.environ['num'] = str(num)
            a1 = os.getenv('a1')
            a2 = os.getenv('a2')
            a3 = os.getenv('a3')
            a4 = os.getenv('a4')
            a5 = os.getenv('a5')
            a6 = os.getenv('a6')
            a7 = os.getenv('a7')
            a8 = os.getenv('a8')
            a9 = os.getenv('a9')
            a10 = os.getenv('a10')
            await logchannel.send(f'''> **Message Deleted**
**Message ID**: {message.id}
**Channel**: #{channel.name} (<#{channel.id}>)
**Channel ID**: {channel.id}
**Cached**: True
» Cache details:
**Message content**:
`-----o-----`
{message.content}
`-----x-----`
**Attachments**:
  - **A¹**: {a1}
  - **A²**: {a2}
  - **A³**: {a3}
  - **A⁴**: {a4}
  - **A⁵**: {a5}
  - **A⁶**: {a6}
  - **A⁷**: {a7}
  - **A⁸**: {a8}
  - **A⁹**: {a9}
  - **A¹⁰**: {a10}
**Message author**: {message.author} ({message.author.mention})
**Message author ID**: {message.author.id}''')
        except Exception as e:
            os.environ['num'] = '0'
            os.environ['a1'] = '`None`'
            os.environ['a2'] = '`None`'
            os.environ['a3'] = '`None`'
            os.environ['a4'] = '`None`'
            os.environ['a5'] = '`None`'
            os.environ['a6'] = '`None`'
            os.environ['a7'] = '`None`'
            os.environ['a8'] = '`None`'
            os.environ['a9'] = '`None`'
            os.environ['a10'] = '`None`'
            for attachment in message.attachments:
                num = os.getenv('num')
                num = int(num) + 1
                A = 'a' + str(num)
                os.environ[A] = '<' + str(attachment.url) + '>'
                os.environ['num'] = str(num)
            a1 = os.getenv('a1')
            a2 = os.getenv('a2')
            a3 = os.getenv('a3')
            a4 = os.getenv('a4')
            a5 = os.getenv('a5')
            a6 = os.getenv('a6')
            a7 = os.getenv('a7')
            a8 = os.getenv('a8')
            a9 = os.getenv('a9')
            a10 = os.getenv('a10')
            await logchannel.send(f'''> **Message Deleted**
**Message ID**: {message.id}
**Channel**: #{channel.name} (<#{channel.id}>)
**Channel ID**: {channel.name}
**Cached**: True
» Cache details:
**Message content**: *Refer to the message below* (**`Exception:`**` {e}`)
**Attachments**:
  - **A¹**: {a1}
  - **A²**: {a2}
  - **A³**: {a3}
  - **A⁴**: {a4}
  - **A⁵**: {a5}
  - **A⁶**: {a6}
  - **A⁷**: {a7}
  - **A⁸**: {a8}
  - **A⁹**: {a9}
  - **A¹⁰**: {a10}
**Message author**: {message.author} ({message.author.mention})
**Message author ID**: {message.author.id}''')
            await logchannel.send(f'{message.content}')

# on message edit
@client.event
async def on_message_edit(before, after):
    return
    #print(f'\n\nB E F O R E :   {before}\n')
    #print(f'\n\nA F T E R :   {after}\n')
    pass

# on raw message edit
@client.event
async def on_raw_message_edit(payload):
    return
    print(f'\n\nP A Y L O A D :   {payload}\n')
    json_payloaddata = json.loads(str(payload.data))

# logging into APU Utils
print("Logging into APU Utils...")
client.run(never_gonna_give_you_up)