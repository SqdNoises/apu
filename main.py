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
print('  - Importing datetime...')
import datetime
print('  - Importing pytz...')
import pytz
print('  - Importing json...')
import json
print('  - Importing psutil...')
import psutil
print('  - Importing urllib...')
import urllib
print('  - Importing requests...')
import requests
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
    rldinf = os.getenv('reloadinfo')
    channel = os.getenv('channel')
    logchannel = client.get_channel(902785006173315072)
    if rldinf == 'reloading':
        channel = client.get_channel(int(channel))
        os.environ['reloadinfo'] = 'connected'
        await channel.send('**Reloaded!**')
        await logchannel.send(f'> **Connected to Discord!**\n**Running on**: {userHost}\n**Status**: `Reloaded`\n**Latency**: {round(client.latency * 1000)}ms')
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Reloaded! Running on `{userHost}`.'), status=nextcord.Status.online)
        await wait(5)
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Running on `{userHost}`'), status=nextcord.Status.online)
    elif rldinf == 'connected' or rldinf == None:
        await logchannel.send(f'> **Connected to Discord!**\n**Running on**: {userHost}\n**Status**: `Connected`\n**Latency**: {round(client.latency * 1000)}ms')
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Connected to Discord! Running on `{userHost}`.'), status=nextcord.Status.online)
        await wait(5)
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Running on `{userHost}`'), status=nextcord.Status.online)

# NEXTCORD.UI
# highlow
class highlow(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.userIn = None
        self.user = user
    
    @nextcord.ui.button(label='Lower', style=nextcord.ButtonStyle.blurple)
    async def lower(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = interaction.user
        if self.user == user:
            self.userIn = 'lower'
            self.stop()
        else:
            await interaction.response.send_message(f'**This is not your highlow game. This is `{self.user.name}`\'s highlow game.**', ephemeral=True)
    
    @nextcord.ui.button(label='JACKPOT!', style=nextcord.ButtonStyle.blurple)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = interaction.user
        if self.user == user:
            self.userIn = 'jackpot'
            self.stop()
        else:
            await interaction.response.send_message(f'**This is not your highlow game. This is `{self.user.name}`\'s highlow game.**', ephemeral=True)
    
    @nextcord.ui.button(label='Higher', style=nextcord.ButtonStyle.blurple)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = interaction.user
        if self.user == user:
            self.userIn = 'higher'
            self.stop()
        else:
            await interaction.response.send_message(f'**This is not your highlow game. This is `{self.user.name}`\'s highlow game.**', ephemeral=True)
    
    @nextcord.ui.button(label='Quit', style=nextcord.ButtonStyle.red)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        user = interaction.user
        if self.user == user:
            self.userIn = 'quit'
            self.stop()
        else:
            await interaction.response.send_message(f'**This is not your highlow game. This is `{self.user.name}`\'s highlow game.**', ephemeral=True)
    
# highlow disabled
class highlow_disabled(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow lower red
class highlow_lowred(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', style=nextcord.ButtonStyle.red, disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow lower green
class highlow_lowgreen(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', style=nextcord.ButtonStyle.green, disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow jackpot red
class highlow_jackred(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', style=nextcord.ButtonStyle.red, disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow jackpot green
class highlow_jackgreen(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', style=nextcord.ButtonStyle.green, disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
        
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow higher red
class highlow_highred(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', style=nextcord.ButtonStyle.red, disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow higher green
class highlow_highgreen(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', style=nextcord.ButtonStyle.green, disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

# highlow quit
class highlow_quit(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label='Lower', disabled=True)
    async def lower(self, button: nextcord.ui.Button):
        self.stop()
    
    @nextcord.ui.button(label='JACKPOT!', disabled=True)
    async def jackpot(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Higher', disabled=True)
    async def higher(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()
    
    @nextcord.ui.button(label='Quit', style=nextcord.ButtonStyle.red, disabled=True)
    async def quit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.stop()

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
    cum2 = cum.replace('<@', '<@!')
    logchannel = client.get_channel(902785006173315072)
    modlogchannel = client.get_channel(917038857814433804)
    p = os.getenv('prefix')
    if p == None: os.environ['prefix'] = 'os!'
    p = os.getenv('prefix')
    prefix = p
    yes = '<a:Animated_Checkmark:901803000861966346>'
    no = '<a:no:901803557014077480>'
    
    # colours
    c = nextcord.Colour
    blue = c.blue()
    blurple = c.blurple()
    brand_green = c.brand_green()
    brand_red = c.brand_red()
    dark_blue = c.dark_blue()
    dark_gold = c.dark_gold()
    dark_gray = c.dark_gray()
    dark_green = c.dark_green()
    dark_grey = c.dark_grey()
    dark_magenta = c.dark_magenta()
    dark_orange = c.dark_orange()
    dark_purple = c.dark_purple()
    dark_red = c.dark_red()
    dark_teal = c.dark_teal()
    dark_theme = c.dark_theme()
    darker_gray = c.darker_gray()
    darker_grey = c.darker_grey()
    default = c.default()
    fuchsia = c.fuchsia()
    gold = c.gold()
    green = c.green()
    greyple = c.greyple()
    light_gray = c.light_gray()
    light_grey = c.light_grey()
    lighter_gray = c.lighter_gray()
    lighter_grey = c.lighter_grey()
    magenta = c.magenta()
    red = c.red()
    teal = c.teal()
    yellow = c.yellow()
    
    # checks if message is from guild
    if message.guild == None:
       if author == client.user: return
       dmlog = client.get_channel(917091525219991592)
       try: await dmlog.send(f'**```{author}``` ({author.id})**: {msg}')
       except Exception as e:
           await dmlog.send(f'**```{author}``` ({author.id})**: —> **`Exception:`**` {e}` (Resending DM message, but only content. Check the below message)')
           await dmlog.send(msg)
       if msg.startswith(f'{p}'):
           await reply('**{no} You cannot use my commands in DMs!**')
           return
       elif msg == cum or msg == cum2: return
       else: return
    
    # Emoji Packs
    if message.guild.id == 901800331204259870:
        if msg == f'{p}help': await reply(f'''> **Goffy's Bot' Emoji Pack 1 - Help**
#> **Prefix:** `{prefix}`
**{p}emojis** - Sends all emojis one by one in separate measages''')
        elif msg == f'{p}emojis':
            await reply('**List of emojis:**')
            for emoji in message.guild.emojis:
                await sendmsg(f'{emoji} - {emoji.id}')
                await sendmsg(f'\{emoji}')
                await sendmsg('`-------`')
        elif msg == cum or msg == cum2: await reply(f'**Prefix:** `{prefix}`')
    elif message.guild == 909453627096178688:
        if msg == f'{p}help': await reply(f'''> **APU Utils Emoji Pack 1 - Help**
#> **Prefix:** `{prefix}`
**{p}emojis** - Sends all emojis one by one in separate measages''')
        elif msg == f'{p}emojis':
            await reply('**List of emojis:**')
            for emoji in message.guild.emojis:
                await sendmsg(f'{emoji} - {emoji.id}')
                await sendmsg(f'\{emoji}')
                await sendmsg('`-------`')
        elif msg == cum or msg == cum2: await reply(f'**Prefix:** `{prefix}`')
    
    # Anti Proprietary Union
    if message.guild.id == 901201688008990750: pass
    else: return
    
    # Functions
    async def setstatus():
        activity = os.getenv('activity')
        status = os.getenv('status')
        state = os.getenv('state')
        if activity == 'watching' and status != 'ⁿ⁰ⁿ³':
            if state == 'online' or state == 'ⁿ⁰ⁿ³': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=status), status=nextcord.Status.online)
            elif state == 'idle': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=status), status=nextcord.Status.idle)
            elif state == 'dnd': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=status), status=nextcord.Status.dnd)
        elif activity == 'playing' and status != 'ⁿ⁰ⁿ³':
            if state == 'online' or state == 'ⁿ⁰ⁿ³': await client.change_presence(activity=nextcord.Game(name=status), status=nextcord.Status.online)
            elif state == 'idle': await client.change_presence(activity=nextcord.Game(name=status), status=nextcord.Status.idle)
            elif state == 'dnd': await client.change_presence(activity=nextcord.Game(name=status), status=nextcord.Status.dnd)
        elif activity == 'listening to' and status != 'ⁿ⁰ⁿ³':
            if state == 'online' or state == 'ⁿ⁰ⁿ³': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=status), status=nextcord.Status.online)
            elif state == 'idle': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=status), status=nextcord.Status.idle)
            elif state == 'dnd': await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=status), status=nextcord.Status.dnd)
        elif activity == 'streaming' and status != 'ⁿ⁰ⁿ³': await client.change_presence(activity=nextcord.Streaming(name=status, url=None))
        elif activity == 'ⁿ⁰ⁿ³':
            if state == 'online' or status == 'ⁿ⁰ⁿ³': await client.change_presence(activity=None, status=nextcord.Status.online)
            elif state == 'idle': await client.change_presence(activity=None, status=nextcord.Status.idle)
            elif state == 'dnd': await client.change_presence(activity=None, status=nextcord.Status.dnd)
    
    # is_me
    def is_me(m): return m.author == client.user
    
    # ping to member id
    def ping_replace(mem):
        os.environ['memid'] = mem
        mem = os.getenv('memid')
        if '<' in mem and '@' in mem and '>' in mem:
            mem = mem.replace('<', '')
            mem = mem.replace('@', '')
            mem = mem.replace('>', '')
            if '!' in mem:
                mem = mem.replace('!', '')
                os.environ['memid'] = mem
            else: os.environ['memid'] = mem
        mem = os.getenv('memid')
        return int(mem)
    
    # remove prefix
    def remprefix(msg):
        p = os.getenv('prefix')
        p = p.lower()
        lowmsg = msg.lower()
        if lowmsg.startswith(f'{p}'):
            if lowmsg.startswith(f'{p} '):
                p = os.getenv('prefix')
                try:
                    msg = msg.split(f'{p} ', 1)[1]
                    os.environ['rempref'] = 'pass'
                    os.environ['msg'] = msg
                except:
                    try:
                        p = p.lower()
                        msg = msg.split(f'{p} ', 1)[1]
                        os.environ['rempref'] = 'pass'
                        os.environ['msg'] = msg
                    except:
                        try:
                            p = p.upper()
                            msg = msg.split(f'{p} ', 1)[1]
                            os.environ['rempref'] = 'pass'
                            os.environ['msg'] = msg
                        except: os.environ['rempref'] = 'fail'
            else:
                p = os.getenv('prefix')
                try:
                    msg = msg.split(f'{p}', 1)[1]
                    os.environ['rempref'] = 'pass'
                    os.environ['msg'] = msg
                except:
                    try:
                        p = p.lower()
                        msg = msg.split(f'{p}', 1)[1]
                        os.environ['rempref'] = 'pass'
                        os.environ['msg'] = msg
                    except:
                        try:
                            p = p.upper()
                            msg = msg.split(f'{p}', 1)[1]
                            os.environ['rempref'] = 'pass'
                            os.environ['msg'] = msg
                        except: os.environ['rempref'] = 'fail'
            msg = os.getenv('msg')
            rempref = os.getenv('rempref')
            return [msg, rempref]

    # time rn
    def timenow(debug=True):
        os.environ['time'] = '-[!] Error-'
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        if debug == True:
            time = f'[ {hour}:{minute}:{second} ]'
            os.environ['time'] = time
        elif debug == False:
            time = f'{hour}:{minute}:{second}'
            os.environ['time'] = time
        time = os.getenv('time')
        return time
    
    # get a post from a subreddit
    def get_post(subreddit):
        base_url = f'https://www.reddit.com/r/{subreddit}/random.json?count=1&t=month'
        try:
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
            post = request.json()
            post = post[0]['data']['children'][0]['data']
            title = post['title']
            image_url = post['url']
            nsfw = post['over_18']
            upvotes = post['ups']
            subreddit = post['subreddit_name_prefixed']
            comments = post['num_comments']
            link = 'https://reddit.com' + post['permalink']
            author = post['author']
            downvotes = post['downs']
            flair = post['link_flair_text']
            description = post['selftext']
            return [title, link, image_url, subreddit, author, upvotes, comments, nsfw, downvotes, flair, description]
        except: return 'error'
    
    # admins
    def admins():
        guild = client.get_guild(901201688008990750)
        role = guild.get_role(901202878784487454)
        members = []
        for member in role.members:
            members.append(member.id)
        return members
     
    # Muted role setting up
    channel = message.channel
    channeltype = str(type(channel))
    guild = client.get_guild(901201688008990750)
    role = guild.get_role(917241786160783410)
    await channel.set_permissions(role, send_messages = False, reason='Making sure Muted people cannot send messages to this channel')
     
    # staff
    sqd = 477683725673693184
    sqdalt = 742219790638383114
    admins = admins()
    
    # sqd
    getsqd = message.guild.get_member(sqd)
    sqdavatar = str(getsqd.avatar.url)
    sqdname = str(getsqd.name)
    
    # main
    # if author is bot itself
    if author == client.user:
        if msg == 'Ping?':
            await wait(2.5)
            await delete()
        elif msg.endswith('` of my messages in this channel!'):
            await wait(5)
            try: await delete()
            except: pass
        elif msg.endswith('` messages in this channel!**'):
            await wait(5)
            try: await delete()
            except: pass
        elif msg == '** _ _ **':
            await wait(15)
            res = os.getenv(str(message.id))
            secret = os.getenv(f'{message.id}secret')
            randnum = os.getenv(f'{message.id}randnum')
            authorid = os.getenv(f'{message.id}id')
            author = message.guild.get_member(int(authorid))
            if res == None or res == 'got res':
                return
            elif res == 'no res':
                emb = nextcord.Embed(description=f'Too late.\nThe number was **`{secret}`** and your hint was **`{randnum}`**.', color=default)
                emb.set_author(name=f'{author.name}\'s expired high-low game', icon_url=author.avatar.url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                view = highlow_disabled()
                await message.edit(embed=emb, view=view)
        else: return
    
    # if lowmessage starts with lowprefix
    lowprefix = prefix.lower()
    if lowmsg.startswith(lowprefix):
        # removing prefix from msg
        msgrempref = remprefix(msg)
        msg = msgrempref[0]
        rempref = msgrempref[1]
        if rempref == 'pass': pass
        elif rempref == 'fail':
            await reply(f'If you are trying to use one of my commands, please use `{p}`.')
            return
        
        # log in console
        time = timenow()
        print(f'\n{time} Command `{p}{msg}` called by `{author}` ({author.id})')
        
        # ''
        if msg == '':
            xl = ['???', 'i would love it if you provide a command', 'u srs?', 'bruh specify a command-', '...', '*crickets start chirping*', 'ok', 'ok, you\'ve summoned me. now what?', 'do you have brain?', f'if you\'re looking for my commands, do `{p}help` instead of summoning me and wasting my time.', 'shut', 'hello']
            n = len(xl) - 1
            num = random.randint(0, n)
            x = xl[num]
            await reply(x)
        
        # test
        elif msg == 'test' or msg.startswith('test '):
            if author.id == sqd or author.id in admins:
                if msg.startswith('test create'):
                    emb = msg.split('\n', 2)
                    embtitle = emb[1]
                    embdesc = emb[2]
                    embedVar = nextcord.Embed(title=embtitle, description=embdesc, colour=0x00FFFF)
                    #embedVar.add_field(name="Die", value="hi", inline=False)
                    #embedVar.add_field(name="Die 2", value="hi 2", inline=False)
                    embedVar.set_author(name='APU Utils', icon_url=client.user.avatar.url)
                    await message.channel.send(embed=embedVar)
                elif msg == 'test':
                    m = await sendmsg('yoo tets dudd')
                    print(m)
                elif msg.startswith('test add '):
                    a = int(msg.split('test add ', 1)[1])
                    roles = author.roles
                    guild = client.get_guild(901201688008990750)
                    roleadd = guild.get_role(a)
                    roles.append(roleadd)
                    await author.edit(roles=roles, reason=f'{p}test add command used by {str(author)}')
                elif msg.startswith('test rem '):
                    a = int(msg.split('test rem ', 1)[1])
                    roles = author.roles
                    guild = client.get_guild(901201688008990750)
                    roleadd = guild.get_role(a)
                    roles.remove(roleadd)
                    await author.edit(roles=roles, reason=f'{p}test rem command used by {str(author)}')
            else: await reply('u nono is are have permision to use dis comand')
        
        # help
        elif msg == 'help':
            emb = nextcord.Embed(title='Commands - Help - APU Utils', description=f'''
```
Prefix: {prefix}
```
**`{p}help`** - Replies with a list of commands
**`{p}aliases`** - Shows aliases for commands
''', color=author.top_role.colour)
            emb.add_field(name='Fun', value=f'''
**`{p}say <what to say>`** - Makes the bot say what you want it to!
**`{p}roast [optional: user/message]`** - Sends a roast message
**`{p}summon <user/message>`** - `/summon` someone or something
**`{p}highlow`** - Try your luck! Guess if the secret number is higher or lower than a number
**`{p}meme`** - Sends a meme
**`{p}reddit <subreddit>`** - Sends a random post from the subreddit you specify
**`{p}simprate`** - Check how much of a simp a person is!
**`{p}gayrate`** - Check how gay a person is!
''', inline=False)
            emb.add_field(name='Utilities', value=f'''
**`{p}userinfo <member>`** - Replies with the info of the member mentioned/id specified
**`{p}avatar`** - Replies with the mentioned user's avatar
**`{p}timer <number of seconds> [optional: timer name]`** - A timer command that sets a timer for the specified amount of time then ping you!
''', inline=False)
            emb.add_field(name='Useful', value =f'''
**`os!fosslist`** - Replies with some useful FOSS alternative lists
''', inline=False)
            emb.add_field(name='Bot', value=f'''
**`{p}ping`** - Replies with the bot latency
**`{p}sourcecode`** - Replies with the bot's source code
**`{p}instance`** - Replies with username@hostname of the bot instance
**`os!sourcecode`** - Replies with the link to source code for APU Utils
''', inline=False)
            emb.set_author(name='APU Utils', icon_url=client.user.avatar.url)
            emb.set_footer(text=f'Made by {sqdname}', icon_url=sqdavatar)
            await reply(embed=emb)
            if author.id == sqd or author.id in admins:
                try:
                    dm = await author.create_dm()
                    emb = nextcord.Embed(title='Commands - Admin Help - APU Utils', description=f'''
```
Prefix: {prefix}
```
**`{p}help`** - Replies with a list of commands and DMs this help page
''', color=0x25C059)
                    emb.add_field(name='Fun', value=f'''
**`{p}delsay <what to say>`** - Deletes your message and sends what you want the bot to say
**`{p}send <channel> <message>`** - Sends a message anonymously to the channel you specify
**`{p}deadchat`** - Sends a dead chat meme
**`{p}dmsend <user> <message>`** - Sends a DM with the message you want to send to the specified member
''', inline=False)
                    emb.add_field(name='Moderation', value=f'''
**`{p}warn <member> [optional: reason]`** - Warns the member with the reason specified or no reason
**`{p}mute <member> [optional: reason]`** - Mutes the member with the reason specified or no reason
**`{p}unmute <member> [optional: message]`** - Unmutes the member
**`{p}kick <member> [optional: reason]`** - Kicks the member with the reason specified or no reason
**`{p}ban <member> [optional: reason]`** - Bans the member with the reason specified or no reason
**`{p}unban <member>`** - Unbans the member
**`{p}modnick <member id>`** - Moderates a member's nickname to _`moderated username (random number)`_
**`{p}nick <member> [new nick]`** - Changes a nickname of a user to the one specified, if no nickname is given, it resets their nickname
**`{p}rules`** - Deletes your message and sends a list of rules
**`{p}rule <rule number>`** - Deletes your message and sends the rule you specified
''', inline=False)
                    emb.add_field(name='Bot', value=f'''
**`{p}prefix change <new prefix>`** - Changes the prefix to the new prefix specified
**`{p}status <command> [input]`** - Changes the activity, status and state of the bot. Do 'g!status' for help 
**`{p}reload`** - Reloads the bot
**`{p}killprocess`** - Kills the process of the bot
**`{p}clientclose`** - `client.close()`s the bot
**`{p}test`** - Test command for testing stuff
''', inline=False)
                    emb.add_field(name='Other', value=f'''
**`{p}slowmode <number>`** - Changes the slowmode of the current channel to the number specified or None
**`{p}clear`** - Clear the bots messages in a channel
**`{p}purge <number>`** - Deletes messages in a channel
**`{p}announce <what to announce>`** - Announce something in the announcements channel
**`{p}apuannounce <what to announce>`** - Announce something in the apu announcements channel
**`{p}proprietary <member>`** - Changes the nick of the member specified to `proprieraryuser`
**`{p}checkthepins`** - Deletes your message and sends a message containing the <a:ctp:901802005230661662> animated emoji
''', inline=False)
                    emb.add_field(name='Aliases', value=f'''
**`{p}reload`** - {p}r
**`{p}killprocess`** - {p}kp
**`{p}clientclose`** - {p}cc
**`{p}proprietary`** - {p}p
**`{p}checkthepins`** - {p}ctp
''', inline=False)
                    emb.set_author(name='APU Utils', icon_url=client.user.avatar.url)
                    emb.set_footer(text=f'Made by {sqdname}', icon_url=sqdavatar)
                    await dm.send(embed=emb)
                except Exception as e:
                    await sendmsg(f'Hey {author.mention}, please enable your DMs!\n**`Exception:`**` {e}`')
            if author.id == sqd:
                try:
                    dm = await author.create_dm()
                    emb = nextcord.Embed(title='Commands - Sqd Help - APU Utils', description=f'''
```
Prefix: {prefix}
```
**`{p}help`** - Replies with a list of commands and DMs this help page 
''', color=0x82C021)
                    emb.add_field(name='Fun', value=f'''
**`{p}die`** - Dies a person lol
''', inline=False)
                    emb.set_author(name='APU Utils', icon_url=client.user.avatar.url)
                    emb.set_footer(text=f'Made by {sqdname}', icon_url=sqdavatar)
                    await dm.send(embed=emb)
                except Exception as e: await sendmsg(f'Hey {author.mention}, please enable your DMs!\n**`Exception:`**` {e}`')
        # aliases
        elif msg == 'aliases':
            emb = nextcord.Embed(title='Aliases - APU Utils', description=f'''
```
Prefix: {prefix}
```
**`{p}highlow`** - {p}hl
**`{p}ping`** - {p}latency
**`{p}instance`** - {p}i
**`{p}sourcecode`** - {p}source, {p}source-code, {p}sc, {p}code
''', color=author.top_role.colour)
            emb.set_author(name='APU Utils', icon_url=client.user.avatar.url)
            emb.set_footer(text=f'Made by {sqdname}', icon_url=sqdavatar)
            await reply(embed=emb)
        # checkthepins
        elif msg == 'checkthepins' or msg == 'ctp':
            if author.id in admins or author.id == sqd:
                await delete()
                await sendmsg('<a:ctp:901802005230661662>')
            else: await reply('**No.**')
        # rule <rule number>
        elif msg.startswith('rule'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('rule '): pass
                elif msg == 'rule':
                    await reply('Rule number pls?')
                    return
                else:
                    await reply(f'**Command `{p}{msg}` not found!**')
                    return
                try:
                    p = message.guild.get_member(840644782673100870)
                    rulelist = ['NO PROPRIETARY SOFTWARE.', 'No bigotry', 'No slurs', 'No NSFW in non-NSFW channels', 'No illegal stuff', 'No arguing about stupid stuff', 'NO BEING UNFUNNY!!!', 'No spamming/chat flood', 'No advertising except in <#901860994446405692>, and even then, only advertise open-source stuff', 'English only', 'No disagreeing with `{p.name}`.']
                    rule = msg.split('rule ', 1)[1]
                    rulenum = int(rule) - 1
                    rulestr = rulelist[rulenum]
                    await sendmsg(f'> **Rule {rule}**\n   - {rulestr}')
                    await delete()
                except:
                    await reply('That rule number doesn\'t exist...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # rules
        elif msg == 'rules':
            if author.id in admins or author.id == sqd:
                await delete()
                p = message.guild.get_member(840644782673100870)
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
**10)** English only
**11)** No disagreeing with `{p.name}`.

*Not following these rules will result in a mute, warn or ban depending on the severity of the rule you break and which rule you broke.*''')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # meme
        elif msg == 'meme':
            embmeme = await sendmsg('**Fetching Post...**')
            subreddits = ['memes', 'dankmemes', 'engrish', 'me_irl', 'AdviceAnimals', 'ComedyCemetery', 'terriblefacebookmemes', 'funny', 'Dank', 'linuxmemes', 'programmerhumour', 'MemeEconomy']
            subredditchoosenum = random.randint(0, len(subreddits)-1)
            subreddit = subreddits[subredditchoosenum]
            meme = get_post(subreddit)
            if meme == 'error':
                await embmeme.edit('**An error occured! Please try executing the command again.**')
                return
            await embmeme.edit('**Loading Meme... ` Progress 0/2 `**')
            memeTitle = meme[0]
            memeLink = meme[1]
            memeImage_url = meme[2]
            memeSubreddit = meme[3]
            memeAuthor = meme[4]
            memeUpvotes = meme[5]
            memeComments = meme[6]
            memeNSFW = meme[7]
            await embmeme.edit('**Loading Meme... ` Progress 1/2 `**')
            if memeNSFW:
                emb = nextcord.Embed(title=memeTitle, description=f'`👍 Upvotes: `**`{memeUpvotes}`**   `💬 Comments: `**`{memeComments}`**\n**NSFW**', url=memeLink, color=dark_red)
                emb.set_author(name=f'Posted by u/{memeAuthor} on {memeSubreddit}', icon_url=author.avatar.url)
                emb.set_image(url=memeImage_url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await embmeme.edit('**Meme Loaded. ` Progress 2/2 `**')
                await embmeme.edit('_ _', embed=emb)
            else:
                emb = nextcord.Embed(title=memeTitle, description=f'`👍 Upvotes: `**`{memeUpvotes}`**   `💬 Comments: `**`{memeComments}`**', url=memeLink, color=blurple)
                emb.set_author(name=f'Posted by u/{memeAuthor} on {memeSubreddit}', icon_url=author.avatar.url)
                emb.set_image(url=memeImage_url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await embmeme.edit('**Meme Loaded. ` Progress 2/2 `**')
                await embmeme.edit('_ _', embed=emb)
        # reddit
        elif msg.startswith('reddit'):
            if msg == 'reddit':
                await reply(f'''```
Usage: {p}reddit <subreddit>
```''')
            elif msg.startswith('reddit '):
                subreddit = msg.split('reddit ', 1)[1]
                embpost = await sendmsg('**Fetching Post...**')
                post = get_post(subreddit)
                if post == 'error':
                    await embpost.edit('**An error occured! Please check if that subreddit actually exists.** *(I only fetch posts that were posted in a month.)*')
                    return
                await embpost.edit('**Loading Post... ` Progress 0/2 `**')
                postTitle = post[0]
                postLink = post[1]
                postImage_url = post[2]
                postSubreddit = post[3]
                postAuthor = post[4]
                postUpvotes = post[5]
                postComments = post[6]
                postNSFW = post[7]
                postDownvotes = post[8]
                postFlair = post[9]
                postDescription = post[10]
                await embpost.edit('**Loading Post... ` Progress 1/2 `**')
                if postNSFW:
                    emb = nextcord.Embed(title=postTitle, description=f'`👍 Upvotes: `**`{postUpvotes}`**   `💬 Comments: `**`{postComments}`**   `👎 Downvotes (if any): `**`{postDownvotes}`**\n**Flair:** {postFlair}\n**NSFW**\n\n{postDescription}', url=postLink, color=dark_red)
                    emb.set_author(name=f'Posted by u/{postAuthor} on {postSubreddit}', icon_url=author.avatar.url)
                    emb.set_image(url=postImage_url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    await embpost.edit('**Post Loaded. ` Progress 2/2 `**')
                    await embpost.edit('_ _', embed=emb)
                else:
                    emb = nextcord.Embed(title=postTitle, description=f'`👍 Upvotes: `**`{postUpvotes}`**   `💬 Comments: `**`{postComments}`**   `👎 Downvotes (if any): `**`{postDownvotes}`**\n**Flair:** {postFlair}\n\n{postDescription}', url=postLink, color=blurple)
                    emb.set_author(name=f'Posted by u/{postAuthor} on {postSubreddit}', icon_url=author.avatar.url)
                    emb.set_image(url=postImage_url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    await embpost.edit('**Post Loaded. ` Progress 2/2 `**')
                    await embpost.edit('_ _', embed=emb)
            else: await reply(f'**Command `{p}{msg}` not found!**')
        # prefix [change] <new prefix>
        elif msg.startswith('prefix'):
            if msg == 'prefix': await reply(f'My prefix is `{prefix}`!')
            elif msg.startswith('prefix '):
                if msg.startswith('prefix change'):
                    if author.id in admins or author.id == sqd:
                        if msg.startswith('prefix change '):
                            pass
                            newprefix = msg.split('prefix change ', 1)[1]
                            await reply(f'**Changing the prefix to `{newprefix}`...** (__Old__: {prefix})')
                            os.environ['prefix'] = newprefix
                            await sendmsg(f'**Prefix changed to `{newprefix}`!**')
                            await logchannel.send('''> **Prefix Changed**
**Changed by:** `{str(author)} ({author.id})
**Old:** {prefix}
**New:** {newprefix}''')
                        else: await reply('**New prefix please?**')
                    else: await reply(f'**{no} You do not have permission to use this command!**')
                else: await reply(f'**Command `{msg}` not found!**')
        # reload
        elif msg == 'reload' or msg == 'r':
             if author.id == sqd or author.id in admins:
               channel = message.channel.id
               os.environ['reloadinfo'] = 'reloading'
               os.environ['channel'] = str(channel)
               await reply('**Reloading...**')
               await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Reloading!'), status=nextcord.Status.dnd)
               await logchannel.send(f'**{p}{msg}** called by Sqd. Reloading the bot!')
               time = timenow()
               print(f'\n{time} Reloading Bot...\n')
               os.system('python3 main.py')
               os._exit(1)
             else: await reply(f'**{no} You do not have permission to use this command!**')
        # killprocess
        elif msg == 'killprocess' or msg == 'kp':
            if author.id == sqd or author.id in admins:
                await reply('**Killing my process...**')
                await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Process killed.'), status=nextcord.Status.dnd)
                await logchannel.send(f'**{p}{msg}** called by Sqd. Killing the process!')
                time = timenow()
                print(f'\n{time} Process Killed.\n')
                os._exit(1)
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # clientclose
        elif msg == 'clientclose' or msg == 'cc':
            if author.id == sqd or author.id in admins:
                await reply('**`client.close()`ing...**')
                await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'`client.close()`ed.'), status=nextcord.Status.dnd)
                await logchannel.send(f'**{p}{msg}** called by Sqd. `client.close()`ing!')
                time = timenow()
                print('\n{time} `client.close()`ed.')
                await client.close()
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # status <command> [input]
        elif msg.startswith('status'):
            if author.id == goffy or author.id == sqd:
                if msg.startswith('status '):
                    if msg.startswith('status activity'):
                        if msg.startswith('status activity '):
                            activity = msg.split('status activity ', 1)[1]
                            activity = activity.lower()
                            if activity == 'watching':
                                os.environ['activity'] = 'watching'
                                activity = activity.capitalize()
                                await reply(f'**Activity** `{activity}` **will be set as the bot\'s activity once `{p}status update` is called.**')
                            elif activity == 'playing':
                                os.environ['activity'] = 'playing'
                                activity = activity.capitalize()
                                await reply(f'**Activity** `{activity}` **will be set as the bot\'s activity once `{p}status update` is called.**')
                            elif activity == 'listening' or activity == 'listening to':
                                os.environ['activity'] = 'listening to'
                                activity = activity.capitalize()
                                await reply(f'**Activity** `{activity}` **will be set as the bot\'s activity once `{p}status update` is called.**')
                            elif activity == 'streaming':
                                os.environ['activity'] = 'streaming'
                                activity = activity.capitalize()
                                await reply(f'**Activity** `{activity}` **will be set as the bot\'s activity once `{p}status update` is called.**')
                            elif activity == 'none':
                                os.environ['activity'] = 'ⁿ⁰ⁿ³'
                                os.environ['status'] = 'ⁿ⁰ⁿ³'
                                await reply('**Activity and status are now removed.**')
                            else:
                                await reply(f'**Activity `{activity}` doesn\'t exist!**')
                                await sendmsg(f'''```
Usage:
→ {p}status activity <activity>
  - Where <activity> is one of the below
    - watching
    - playing
    - listening / listening to
    - streaming
    - none (No activity)
    @ If no status is set, activity wouldn't be shown
```''')
                        else: await reply(f'''```
Usage:
→ {p}status activity <activity>
  - Where <activity> is one of the below
    - watching
    - playing
    - listening / listening to
    - streaming
    - none (No activity)
    @ If no status is set, activity wouldn't be shown
```''')
                    elif msg.startswith('status status'):
                        if msg.startswith('status status '):
                            status = msg.split('status status ', 1)[1]
                            statusnone = status.lower()
                            if statusnone == 'none':
                                os.environ['activity'] = 'ⁿ⁰ⁿ³'
                                os.environ['status'] = 'ⁿ⁰ⁿ³'
                                await reply('**Activity and status are now removed.**')
                            else:
                                os.environ['status'] = status
                                await reply(f'**Status `{status}` will be set as the bot\'s status once `{p}status update` is called.**')
                        else: await reply(f'''```
Usage:
→ {p}status status <status>
  - Where <status> is the status you want to put
  - none (No status, if no status then no activity)
  @ If no activity is set, status wouldn't be shown
```''')
                    elif msg.startswith('status state'):
                         if msg.startswith('status state '):
                             state = msg.split('status state ', 1)[1]
                             state = state.lower()
                             if state == 'online' or state == 'none' or state == 'default':
                                 os.environ['state'] = 'online'
                                 await reply(f'**State will be set to `Online` as the bot\'s status once `{p}status update` is called.**')
                             elif state == 'idle':
                                 os.environ['state'] = 'idle'
                                 await reply(f'**State will be set to `Idle` as the bot\'s status once `{p}status update` is called.**')
                             elif state == 'dnd' or state == 'do not disturb':
                                 os.environ['state'] = 'dnd'
                                 await reply(f'**State will be set to `Do not disturb/DND` as the bot\'s status once `{p}status update` is called.**')
                             elif state == 'invisible' or state == 'offline':
                                 await reply('I, a bot, cannot go invisible.')
                                 await sendmsg(f'''```
Usage:
→ {p}status state <state>
  - Where state <state> is the state you want the bot in (one of the below)
    - online
    - idle
    - dnd / do not disturb
    - none (online)
    - default (online)
```''')
                             else:
                                 await reply(f'**State `{state}` doesn\'t exist!**')
                                 await sendmsg(f'''```
Usage:
→ {p}status state <state>
  - Where state <state> is the state you want the bot in (one of the below)
    - online
    - idle
    - dnd / do not disturb
    - none (online)
    - default (online)
```''')
                         else: await reply(f'''```
Usage:
→ {p}status state <state>
  - Where state <state> is the state you want the bot in (one of the below)
    - online
    - idle
    - dnd / do not disturb
    - none (online)
    - default (online)
```''')
                    elif msg == 'status update':
                        await reply('**Updating my status...**')
                        await setstatus()
                        await sendmsg('**Status set!**')
                    elif msg == 'status check-variables' or msg == 'status cv':
                        activity = os.getenv('activity')
                        status = os.getenv('status')
                        state = os.getenv('state')
                        await reply(f'''```py
# Variables
Activity: {str(activity)}
Status: {str(status)}
State: {str(state)}
```''')
                    else: await reply(f'''```
Usage:
→ {p}status activity <activity>
  - Where <activity> is one of the below
    - watching
    - playing
    - listening ('listening to' activity)
    - streaming
    - none (No activity)
    @ If no status is set, activity wouldn't be shown
→ {p}status status <status>
  - Where <status> is the status you want to put
  - none (No status, if no status then no activity)
  @ If no activity is set, status wouldn't be shown
→ {p}status state <state>
  - Where state <state> is the state you want the bot in (one of the below)
    - online
    - idle
    - dnd
    - none (online)
    - default (online)
→ {p}status update
  - Updates the bot status, activity and/or state to what you set
→ {p}status check-variables / {p}status cv
  - Something that Sqd will understand lol

Please note: I, a bot, cannot go invisible.
```''')
                else: await reply(f'''```
Usage:
→ {p}status activity <activity>
  - Where <activity> is one of the below
    - watching
    - playing
    - listening ('listening to' activity)
    - streaming
    - none (No activity)
    @ If no status is set, activity wouldn't be shown
→ {p}status status <status>
  - Where <status> is the status you want to put
  - none (No status, if no status then no activity)
  @ If no activity is set, status wouldn't be shown
→ {p}status state <state>
  - Where state <state> is the state you want the bot in (one of the below)
    - online
    - idle
    - dnd
    - none (online)
    - default (online)
→ {p}status update
  - Updates the bot status, activity and/or state to what you set
→ {p}status check-variables / {p}status cv
  - Something that Sqd will understand lol

Please note: I, a bot, cannot go invisible.
```''')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # instance
        elif msg == 'instance' or msg == 'i':
            time = timenow(debug=False)
            ram = psutil.virtual_memory()
            await reply(f'''> **Running on `{userHost}`!**
**user@host:** {userHost}
**RAM Stats:**
   - **Usage Percent:** {ram.percent}%
   **@Calculated**
     - **Available%:** {ram.available/ram.total * 100}%
     - **Used%:** {ram.used/ram.total * 100}%
     - **Free%:** {ram.free/ram.total * 100}%
**Time:** {time}
**Ping:** {round(client.latency * 1000)}ms 🧽''')
        # ping
        elif msg == 'ping' or msg == 'latency': await reply(f'**Pong! {round(client.latency * 1000)}ms** 🏓')
        # warn
        elif msg.startswith('warn'):
            if author.id in admins or author.id == sqd:
                if msg == 'warn': await reply('Who do you want me to warn???')
                elif msg.startswith('warn '):
                    memidreason = msg.split('warn ', 1)[1]
                    memlist = memidreason.split(' ', 1)
                    mem = memlist[0]
                    os.environ[f'{message.id}memid'] = mem
                    os.environ[f'{message.id}reason'] = 'ñ0res'
                    memid = ping_replace(mem)
                    try:
                        member = author.guild.get_member(int(memid))
                        if author.id == goffy and member.id == goffy:
                            await reply('No you can\'t warn yourself Mr. Gold Fish.')
                            return
                        elif member.id == goffy:
                            await reply('What are you doing??? You can\'t warn the king!')
                            return
                        elif member.id == client.user.id:
                            await reply('Bruh imagine warning me')
                            return
                        try:
                            reason = memlist[1]
                            os.environ[f'{message.id}reason'] = reason
                        except: os.environ[f'{message.id}reason'] = 'ñ0res'
                        reason = os.getenv(f'{message.id}reason')
                        if reason == 'ñ0res':
                            try:
                                dm = await member.create_dm()
                                emb = nextcord.Embed(title='You have been warned!', description=f'You have been warned in **{message.guild.name}**!', color=red)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await dm.send(embed=emb)
                                emb = nextcord.Embed(description=f'✅ ***{member.mention} has been warned.***', color=green)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await sendmsg(embed=emb)
                            except Exception as e:
                                emb = nextcord.Embed(description=f'✅ ***{member.mention} has been warned.***', color=green)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await sendmsg(f'**{member.mention}, you have been warned!**', embed=emb)
                            await logchannel.send(f'> **Member Muted** ({str(member)} *using the {p}warn command*\n**Warned:** {str(member)}**Warned by:** `{str(author)}`')
                        else:
                            try:
                                dm = await member.create_dm()
                                emb = nextcord.Embed(title='You have been warned!', description=f'You have been warned in **{message.guild.name}** for `{reason}`!', color=red)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await dm.send(embed=emb)
                                emb = nextcord.Embed(description=f'✅ ***{member.mention} has been warned for*** {reason}***.***', color=green)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await sendmsg(embed=emb)
                            except:
                                emb = nextcord.Embed(description=f'✅ ***{member.mention} has been warned for*** `{reason}`***.***', color=green)
                                emb.set_author(name=f'Warned by {str(author)}', icon_url=author.avatar.url)
                                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                                await sendmsg(f'**{member.mention}, you have been warned for** {reason}**!**', embed=emb)
                            await logchannel.send(f'> **Member Muted** ({str(member)} *using the {p}warn command*\n**Warned:** {str(member)}**Warned by:** `{str(author)}`\n**Warned for:** `{reason}`')
                    except Exception as e: await reply(f'Got an error, have you pinged a person or given their ID?\n**`Exception:`**` {e}`')
                else: await reply(f'**Command `{p}{msg}` not found!**')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # kick
        elif msg.startswith('kick'):
            if author.id in admins or author.id == sqd: await reply('Coming soon...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # mute
        elif msg.startswith('mute'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('mute '):
                    memidreason = msg.split('mute ', 1)[1]
                    memlist = memidreason.split(' ', 1)
                    mem = memlist[0]
                    os.environ['memid'] = mem
                    os.environ['reason'] = 'No reason given'
                    memid = ping_replace(mem)
                    try:
                        member = author.guild.get_member(int(memid))
                        roles = member.roles
                        guild = client.get_guild(901201688008990750)
                        mutedrole = guild.get_role(917241786160783410)
                        for x in roles:
                            if x == mutedrole:
                                await reply('That person is already muted!')
                                return
                        roles.append(mutedrole)
                        try:
                            reason = memlist[1]
                            os.environ['reason'] = reason
                        except: os.environ['reason'] = 'No reason given'
                        reason = os.getenv('reason')
                        await member.edit(roles=roles, reason=f'Muted by {author}, reason: {reason}')
                        if member.nick == None: os.environ['memnick'] = 'None'
                        else: os.environ['memnick'] = 'exist'
                        nick = os.getenv('memnick')
                        if nick == 'exist': await reply(f'**Muted `{member.nick}`!**\n**Reason:** `{reason}`')
                        elif nick == 'None': await reply(f'**Muted `{member.name}`!**\n**Reason:** `{reason}`')
                        await logchannel.send(f'> **Member Muted** ({str(member)} *using the {p}mute command*\n**Muted by:** `{str(member)}`')
                    except Exception as e: await reply(f'Got an error, have you pinged a person or given their ID?\n**`Exception:`**` {e}`')
                else: await reply('Who do you want me to mute?')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # ban
        elif msg.startswith('ban'):
            if author.id in admins or author.id == sqd: await reply('Coming soon...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # unmute
        elif msg.startswith('unmute'):
            if author.id in admins or author.id == sqd:
                 if msg.startswith('unmute '):
                    mem = msg.split('unmute ', 1)[1]
                    mem = mem.split(' ', 1)[0]
                    memid = ping_replace(mem)
                    try:
                        member = author.guild.get_member(int(memid))
                        roles = member.roles
                        guild = client.get_guild(901201688008990750)
                        mutedrole = guild.get_role(917241786160783410)
                        try: roles.remove(mutedrole)
                        except:
                            await reply('The person is not muted!')
                            return
                        await member.edit(roles=roles, reason=f'Unmuted by {author}')
                        if member.nick == None: os.environ['memnick'] = 'None'
                        else: os.environ['memnick'] = 'exist'
                        nick = os.getenv('memnick')
                        if nick == 'exist': await reply(f'**Unmuted `{member.nick}`!**')
                        elif nick == 'None': await reply(f'**Unmuted `{member.name}`!**')
                    except Exception as e: await reply(f'Got an error, have you pinged a person or given their ID?\n**`Exception:`**` {e}`')
                 else: await reply('Who do you want me to unmute?')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # unban
        elif msg.startswith('unban'):
            if author.id in admins or author.id == sqd: await reply('Coming soon...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # modnick
        elif msg.startswith('modnick'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('modnick '):
                    memid = msg.split('modnick ', 1)[1]
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
                        await sendmsg(f'**Moderated the nickname to `{modnick}`.**')
                        await modlogchannel.send(f'''> **Nickname Moderated**
**Nickname moderated by**: ```{author}``` ({author.id})
**Nickname moderated for**: ```{member}``` ({member.id})
**Nickname moderated to**: {modnick}''')
                    except Exception as e: await sendmsg(f'**``Exception:``**` {e}`')
                else: await reply('Please specify a user id!')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # nick
        elif msg.startswith('nick'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('nick '):
                    memidnick = msg.split('nick ', 1)[1]
                    memlist = memidnick.split(' ', 1)
                    mem = memlist[0]
                    mem = ping_replace(mem)
                    try:
                        memid = int(mem)
                        member = author.guild.get_member(memid)
                        prevnick = member.nick
                        if len(memlist) == 1:
                            await member.edit(nick=None)
                            await reply('**Set the member\'s server nickname back to default.**')
                            await modlogchannel.send(f'''> **Nickname Changed** *(through `{p}nick` command)*
**Nickname changed by**: ```{author}``` ({author.id})
**Nickname changed for**: ```{member}``` ({member.id})
**Previous nickname**: ```{prevnick}``` (None could mean that they did not have a nickname)
**Nickname changed to**: ```{member.name}``` (Default Nickname)''')
                        if len(memlist) == 2:
                            memnick = memlist[1]
                            await member.edit(nick=memnick)
                            await reply(f'**Set the member\'s server nickname to `{memnick}`.**')
                            await modlogchannel.send(f'''> **Nickname Changed** *(through `{p}nick` command)*
**Nickname changed by**: ```{author}``` ({author.id})
**Nickname changed for**: ```{member}``` ({member.id})
**Previous nickname**: ```{prevnick}``` (None could mean that they did not have a nickname)
**Nickname changed to**: ```{memnick}```''')
                    except Exception as e:await reply(f'**`Exception:`**` {e}`')
                else: await reply('Please mention or specify a user id!')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # slowmode
        elif msg.startswith('slowmode'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('slowmode '):
                    try:
                        num = int(msg.split('slowmode ', 1)[1])
                        channel = message.channel
                        await channel.edit(slowmode_delay=num, reason=f'Slowmode changed by {author} in {channel.name} using {p}slowmode')
                        await reply(f'**Slowmode is now set to `{num}`.**')
                    except Exception as e: await reply(f'**An error occured!**\n**`Exception:`**` {e}`')
                else: await reply(f'**Current slowmode is `{channel.slowmode_delay}`.**')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # commands
        elif msg == 'commands': await reply(f'Are you looking for my commands? If yes, please type `{p}help` for a list of my commands!')
        # send
        elif msg.startswith('send'):
            if author.id in admins or author.id == sqd: await reply('Coming soon...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # dmsend
        elif msg.startswith('dmsend'):
            if author.id in admins or author.id == sqd: await reply('Coming soon...')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # say
        elif msg.startswith('say'):
            if msg.startswith('say '):
                say = msg.split('say ', 1)[1]
                saysend = f'{say}\n - {author.mention}'
                try:
                    await delete()
                    await sendmsg(saysend)
                except Exception as e: await reply(f'I just got an error, it could be because the bot sent a message over 2000 characters.\n**`Exception:`**` {e}`')
            else: await reply('What do you want me to say?')
        # delsay
        elif msg.startswith('delsay'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('delsay '):
                    await delete()
                    say = msg.split('delsay ', 1)[1]
                    saysend = f'{say} ** _ _ **'
                    await sendmsg(saysend)
                else: await reply('What do you want me to say?')
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # userinfo
        elif msg.startswith('userinfo'):
            if msg.startswith('userinfo '):
                mem = msg.split('userinfo ', 1)[1]
                os.environ['memid'] = mem
                memid = ping_replace(mem)
                try:
                    member = author.guild.get_member(int(memid))
                    await reply(f'''> **User info**
**Member**: `{member}`
**Member ID**: {member.id}
**Member Nickname**: `{member.nick}` *(value* `None` *could mean that the user has no nickname)*
**Avatar URL:** <{member.avatar.url}>
**Created at**: {member.created_at} *(Time is in UTC)*
**Joined at**: {member.joined_at} *(Time is in UTC)*
**Bot**: {member.bot}
*Requested by {author.mention}*''')
                except Exception as e: await reply(f'**An error occured!**\nUsage: `{p}userinfo <member>`\n\n**`Exception:`**` {e}`')
            else: await reply(f'Usage: `{p}userinfo <member>`')
        # die
        elif msg.startswith('die'):
            if author.id == sqd:
                if msg == 'die': await reply('ok, you\'re dead. now what?')
                elif msg.startswith('die '):
                    user = msg.split('die ', 1)[1]
                    await sendmsg(f'{user}, death.')
            else: await reply('**Sqd only command** UwU')
        # deadchat
        elif msg.startswith('deadchat'):
            if author.id in admins or author.id == sqd:
                await delete()
                await sendmsg('Dead chat?', file=nextcord.File('files/media/dead-chat.mp4'))
            else:
                await typing()
                await wait(0.25)
                await sendmsg('Look,')
                await wait(0.1)
                await typing()
                await wait(2)
                await sendmsg('I don\'t know if this chat is dead or not, could be dead idk,')
                await wait(0.1)
                await typing()
                await wait(0.15)
                await sendmsg('but')
                await wait(0.1)
                await typing()
                await wait(1.5)
                await reply('You don\'t have permission to use that command...')
                await wait(0.1)
                await typing()
                await wait(0.25)
                await sendmsg('yeahhh.....')
        # roast
        elif msg.startswith('roast'):
            if str(client.user.id) in msg or 'APU Utils' in lowmsg:
                await reply('Imagine roasting the person who roasts people')
                return
            xl = ["Listen, you have no damn brain.", "I am the nerd, you are the dummy, but I have common sense, you just run to your mummy", "I'm not saying that I hate you, I'm just saying that if you got hit by a bus, I would be driving that bus", "I'm sorry what language you are speaking? It sounds like it's bullshit.", "You are a stupid.", "I'd slap you, but that'd be animal abuse.", "Don't get mad when I pull a **you** on **you**", "Aww... My middle finger likes you", "You must've been born on a highway because that's where most accidents happen","You're so bald I could use your head as a mirror", "You're so salty you would sink in the Dead Sea", "Where'd ya get those pants? The toilet store?", "I'm not being rude, you are just insignificant", "You are like clouds, when they disappear it's a beautiful day", "Maybe you should eat some makeup, so you can be pretty on the inside too", "You are like software updates, whenever I see you, I go **nope**", "Oh darling, go buy a personality", "You look like a dehydrated horse", "I don't hate you, I'm just not necessarily excited about your existence", "Mirrors don't lie. YOU'RE LUCKY THEY DON'T LAUGH EITHER", "Too bad, you can't even photoshop an ugly personality", "I'm not saying I hate you, but I would unplug your life support just to charge my phone.", "LMAO sucks to be YOU", "Why don’t you crawl back to whatever micro-organism cesspool you came from, and try not to breath any of our oxygen on the way there?", "You know they say 90% of dust is dead human skin? That's what you are to me.", "I've never met someone who's at once so thoughtless, selfish, and uncaring of other people's interests, while also having such lame and boring interests of his own. You don't have friends, because you shouldn't.", "Your birth certificate is an apology letter from the abortion clinic.", "You look like you chomp on tree bark for fun", "the only thing you're fucking is natural selection", "I'm not mad. I'm just... disappointed.", "Your mother may have told you that you could be anything you wanted, but a **douchebag** wasn't what she meant.", "Just because your head is shaped like a light bulb doesn't mean you have good ideas", "You're an example of why animals eat their young.", "I hope you win the lottery and lose your ticket.", "You may think people like being around you- but remember this: there is a difference between being liked and being tolerated.", "Don't play hard to get when you are hard to want", "I can smell cat piss by just looking at you", "You know, one of the many, many things that confuses me about you is that you remain unmurdered.", "You are like the end piece of bread in a loaf, everyone touches you but no one wants you", "Your identity is more confusing than the Japanese alphabet", "You don't have to tell us you're a vegan, we can all tell", "You're like a penny on the floor of a public restroom - filthy, untouchable and practically worthless.", "You're just a hormonal banana", "There are two ugly people in this chat, and you're both of them.", "Twelve must be difficult for you. I don’t mean BEING twelve, I mean that being your IQ.", "People like you are the reason God doesn't talk to us anymore", "If there was a single intelligent thought in your head it would have died from loneliness.", "at least my mom pretends to love me", "We all dislike you, but not quite enough that we bother to think about you.", "When you die, people will struggle to think of nice things to say about you.", "If you were a potato you'd be a stupid potato.", "You are dumber than a block of wood and not nearly as useful"]
            n = len(xl) - 1
            num = random.randint(0, n)
            x = xl[num]
            await sendmsg(x)
        # timer
        elif msg.startswith('timer'):
            if msg.startswith('timer '):
                numberreason = msg.split('timer ', 1)[1]
                numreslist = msg.split(' ', 2)
                num = numreslist[1]
                try:
                    num = int(num)
                    if num > 28800:
                        await reply('Sorry, but I won\'t set a timer that is above 28800 seconds! (i.e., 8 hours)')
                        return
                except:
                    await reply('Please specify the number of seconds!')
                    return
                envname = f'timer{author.id}reason'
                os.environ[envname] = 'None'
                try:
                    reason = numreslist[2]
                    os.environ[envname] = reason
                except: os.environ[envname] = 'Unnamed Timer'
                reason = os.getenv(envname)
                try:
                    number = float(num)
                    if number == 1.0:
                        await reply(f'Ok, I will now set a timer named ` {reason} ` for a second and after finishing, ping you!')
                        await wait(number)
                        await sendmsg(f'{author.mention},\nYour timer ` {reason} ` of ` 1.0 ` second just ended!')
                    else:
                        await reply(f'Ok, I will now set a timer named ` {reason} ` for ` {number} ` seconds and after finishing, ping you!')
                        await wait(number)
                        await sendmsg(f'{author.mention},\nYour timer ` {reason} ` of ` {number} ` seconds just ended!')
                except Exception as e: await reply(f'An error occured, did you specify a number?\n**`Exception:`**` {e}`')
            else: await reply(f'''```
* Usage:
 → {p}timer <seconds> [optional: timer name]
## Pings you after the time you specify is over. Timer name is optional.
```''')
        # clear
        elif msg.startswith('clear'):
            if author.id == sqd or author.id in admins: pass
            else:
                await reply(f'**{no} You do not have permission to use this command!**')
                return
            try:
                deleted = await message.channel.purge(limit=100, check=is_me)
                await message.channel.send(f'Deleted `{len(deleted)}` of my messages in this channel!')
                await wait(3)
                await delete()
            except Exception as e: await sendmsg(f'`{e}`')
        # purge
        elif msg.startswith('purge'):
            if author.id == sqd or author.id in admins: pass
            else:
                await reply(f'**{no} You do not have permission to use this command!**')
                return
            if msg.startswith('purge '):
                try: num = int(msg.split('purge ', 1)[1])
                except: await reply('Please provide a correct number!')
                repeat_100=int(num/100)
                last_repeat=num%100
                await reply(f'**Deleting `{num}` messages in this channel!**')
                time = timenow(debug=False)
                print(f'\n--- PURGE COMMAND --- {time}\nDeleting {num} messages in {str(channel)}')
                delet = []
                os.environ['delet_spacelist'] = '0'
                print(f'I am going to delete {num} messages by repeat-deleting 100 messages {repeat_100} times and then delete {last_repeat} messages.')
                try: 
                    for x in range(repeat_100):
                        deleted = await message.channel.purge(limit=100)
                        delet.append(len(deleted))
                        deletstr = str(delet)
                        deletstr = deletstr.replace('[', '')
                        deletstr = deletstr.replace(']', '')
                        deletstr = deletstr.replace(',', '')
                        os.environ['delet_spacelist'] = deletstr
                        time = timenow()
                        print(f'{time} repeat_100: {len(deleted)} messages deleted')
                        print(deletstr)
                except: pass
                delet = os.getenv('delet_spacelist')
                delet = delet.split()
                try:
                    deleted = await message.channel.purge(limit=last_repeat)
                    delet.append(len(deleted))
                    time = timenow()
                    print(f'{time} last_repeat: {last_repeat} messages deleted')
                    print(delet)
                    num = 0
                    for x in delet:
                        num = num + int(x)
                        os.environ['num'] = str(num)
                    deleted = int(os.getenv('num'))
                    await sendmsg(f'**Deleted `{deleted}` messages in this channel!**')
                    time = timenow()
                    print(f'{time} Deleted {deleted} messages in {str(channel)}\n\n')
                except Exception as e: await sendmsg(f'`{e}`')
            elif msg == 'purge':
                await reply('Defaulting to delete 100 messages.')
                await reply('Deleting 100 messages in this channel...') 
                time = timenow(debug=False)
                print(f'\n--- PURGE COMMAND --- {time}\nDeleting 100 messages in {str(channel)}')
                try:
                    deleted = await message.channel.purge(limit=100)
                    await sendmsg(f'**Deleted `{len(deleted)}` messages in this channel!**')
                    time = timenow()
                    print(f'{time} Deleted {len(deleted)} messages in {str(channel)}\n\n')
                except Exception as e: await sendmsg(f'`{e}`')
            else: await reply(f'**Command `{p}{msg}` not found!**')
        # announce
        elif msg.startswith('announce'):
            if author.id == sqd or author.id in admins: pass
            else:
                await reply(f'**{no} You do not have permission to use this command!**')
                return
            if msg.startswith('announce '):
                ancon = msg.split('announce ', 1)[1]
                anchan = client.get_channel(901401261860085790)
                try: await anchan.send(f'{ancon}\n - *Announced by {author.mention}*')
                except Exception as e:
                    await reply('**`Exception:`**` {e}`')
                    return
                await reply('Announced! Check <#901401261860085790>!')
            elif msg == 'announce': await reply(f'''```
* Usage:
→ {p}announce <what to announce>
  - Where <what to announce> is what is going to be announced. (COULD BE USED WITH MORE LINES)
```''')
        # apuannounce
        elif msg.startswith('apuannounce'):
            if author.id == sqd or author.id in admins: pass
            else:
                await reply(f'**{no} You do not have permission to use this command!**')
                return
            if msg.startswith('apuannounce '):
                ancon = msg.split('apuannounce ', 1)[1]
                anchan = client.get_channel(907983368635953162)
                try: await anchan.send(f'{ancon}\n - *Announced by {author.mention}*')
                except Exception as e:
                    await reply('**`Exception:`**` {e}`')
                    return
                await reply('Announced! Check <#907983368635953162>!')
            elif msg == 'apuannounce': await reply(f'''```
* Usage:
→ {p}apuannounce <what to announce>
  - Where <what to announce> is what is going to be announced. (COULD BE USED WITH MORE LINES)
```''')
        # summon
        elif msg.startswith('summon'):
            if msg == 'summon': await reply(f'`Usage: {p}summon <user/message>`')
            elif msg.startswith('summon '):
                sum = msg.split('summon ', 1)[1]
                await delete()
                await sendmsg(f'/summon {sum}')
            else: await reply(f'**Command `{p}{msg}` not found!**')
        # avatar
        elif msg.startswith('avatar'):
            if msg == 'avatar':
                emb = nextcord.Embed(title=f'Avatar of `{str(author)}`', description=f'Avatar URL: {author.avatar.url}', color=author.top_role.colour)
                emb.set_image(url=author.avatar.url)
                emb.set_author(name=author.name, icon_url=author.avatar.url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await reply(embed=emb)
            elif msg.startswith('avatar '):
                mem = msg.split('avatar ', 1)[1]
                try:
                    memid = ping_replace(mem)
                    member = guild.get_member(memid)
                    emb = nextcord.Embed(title=f'Avatar of `{str(member)}`', description=f'Avatar URL: {member.avatar.url}', color=author.top_role.colour)
                    emb.set_image(url=member.avatar.url)
                    emb.set_author(name=member.name, icon_url=member.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    await reply(embed=emb)
                except Exception as e: await reply('Please specify a correct user!\n`{e}`')
            else: await reply(f'**Command `{p}{msg}` not found!**')
        # highlow
        elif msg == 'highlow' or msg == 'hl':
            secret = random.randint(2, 99)
            randnum = random.randint(2,99)
            view = highlow(author)
            # if secret is greater than randnum
            if secret > randnum:
                emb = nextcord.Embed(description=f'I\'ve just chosen a number between 1 and 100.\nIs this number *higher* or *lower* than **`{randnum}`**?\n*(The jackpot button is if you think it\'s the same!)*', color=author.top_role.colour)
                emb.set_author(name=f'{author.name}\'s high-low game', icon_url=author.avatar.url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                game = await reply('** _ _ **', embed=emb, view=view)
                os.environ[str(game.id)] = 'no res'
                os.environ[f'{game.id}secret'] = str(secret)
                os.environ[f'{game.id}randnum'] = str(randnum)
                os.environ[f'{game.id}id'] = str(author.id)
                await view.wait()
                os.environ[str(game.id)] = 'got res'
                if view.userIn is None:
                    return
                elif view.userIn == 'lower':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_lowred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'jackpot':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_jackred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'higher':
                    emb = nextcord.Embed(description=f'You won! Great Job.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=green)
                    emb.set_author(name=f'{author.name}\'s winning high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_highgreen()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'quit':
                    emb = nextcord.Embed(description=f'scaredy cat\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=dark_red)
                    emb.set_author(name=f'{author.name}\'s quitted high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_quit()
                    await game.edit(embed=emb, view=view)
            # if secret is lesser than randnum
            elif secret < randnum:
                emb = nextcord.Embed(description=f'I\'ve just chosen a number between 1 and 100.\nIs this number *higher* or *lower* than **`{randnum}`**?\n*(The jackpot button is if you think it\'s the same!)*', color=author.top_role.colour)
                emb.set_author(name=f'{author.name}\'s high-low game', icon_url=author.avatar.url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                game = await reply('** _ _ **', embed=emb, view=view)
                os.environ[str(game.id)] = 'no res'
                os.environ[f'{game.id}secret'] = str(secret)
                os.environ[f'{game.id}randnum'] = str(randnum)
                os.environ[f'{game.id}id'] = str(author.id)
                await view.wait()
                os.environ[str(game.id)] = 'got res'
                if view.userIn is None:
                    return
                elif view.userIn == 'lower':
                    emb = nextcord.Embed(description=f'You won! Great Job.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=green)
                    emb.set_author(name=f'{author.name}\'s winning high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_lowgreen()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'jackpot':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_jackred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'higher':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_highred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'quit':
                    emb = nextcord.Embed(description=f'scaredy cat\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=dark_red)
                    emb.set_author(name=f'{author.name}\'s quitted high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_quit()
                    await game.edit(embed=emb, view=view)
            # if secret is same as randnum
            elif secret == randnum:
                emb = nextcord.Embed(description=f'I\'ve just chosen a number between 1 and 100.\nIs this number *higher* or *lower* than **`{randnum}`**?\n*(The jackpot button is if you think it\'s the same!)*', color=author.top_role.colour)
                emb.set_author(name=f'{author.name}\'s high-low game', icon_url=author.avatar.url)
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                game = await reply('** _ _ **', embed=emb, view=view)
                os.environ[str(game.id)] = 'no res'
                os.environ[f'{game.id}secret'] = str(secret)
                os.environ[f'{game.id}randnum'] = str(randnum)
                os.environ[f'{game.id}id'] = str(author.id)
                await view.wait()
                os.environ[str(game.id)] = 'got res'
                if view.userIn is None:
                    return
                elif view.userIn == 'lower':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_lowred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'jackpot':
                    emb = nextcord.Embed(description=f'You win! Great Job.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=green)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_jackgreen()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'higher':
                    emb = nextcord.Embed(description=f'Nope. You lost.\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=red)
                    emb.set_author(name=f'{author.name}\'s losing high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_highred()
                    await game.edit(embed=emb, view=view)
                elif view.userIn == 'quit':
                    emb = nextcord.Embed(description=f'scaredy cat\nYour hint was **`{randnum}`** and the number was **`{secret}`**.', color=dark_red)
                    emb.set_author(name=f'{author.name}\'s quitted high-low game', icon_url=author.avatar.url)
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    view = highlow_quit()
                    await game.edit(embed=emb, view=view)
            else: await reply('An error occured while setting up your high-low game!')
        # simprate
        elif msg.startswith('simprate'):
            rate = random.randint(0, 100)
            def colour(rate):
                if rate <= 30:
                    return green
                elif rate <= 65 and rate > 30:
                    return yellow
                elif rate <= 90 and rate > 65:
                    return red
                elif rate <=100 and rate > 90:
                    return dark_red
            if msg == 'simprate':
                colour = colour(rate)
                emb = nextcord.Embed(description=f'You are {rate}% simp', color=colour)
                emb.set_author(name=f'simp r8 machine')
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await reply(embed=emb)
            elif msg.startswith('simprate '):
                person = msg.split('simprate ', 1)[1]
                lowperson = person.lower()
                if str(client.user.id) in person or 'APU Utils' in lowperson:
                    emb = nextcord.Embed(description=f'I am 0% simp.', color=green)
                    emb.set_author(name=f'simp r8 machine')
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    await reply(embed=emb)
                    return
                colour = colour(rate)
                emb = nextcord.Embed(description=f'{person} is {rate}% simp', color=colour)
                emb.set_author(name=f'simp r8 machine')
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await reply(embed=emb)
        # gayrate
        elif msg.startswith('gayrate'):
            rate = random.randint(0, 100)
            def colour(rate):
                if rate <= 30:
                    return green
                elif rate <= 65 and rate > 30:
                    return yellow
                elif rate <= 90 and rate > 65:
                    return red
                elif rate <=100 and rate > 90:
                    return dark_red
            if msg == 'gayrate':
                colour = colour(rate)
                emb = nextcord.Embed(description=f'You are {rate}% gay 🏳️‍🌈', color=colour)
                emb.set_author(name=f'gay r8 machine')
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await reply(embed=emb)
            elif msg.startswith('gayrate '):
                person = msg.split('gayrate ', 1)[1]
                lowperson = person.lower()
                if str(client.user.id) in person or 'APU Utils' in lowperson:
                    emb = nextcord.Embed(description=f'I am 0% gay 🏳️‍🌈.', color=green)
                    emb.set_author(name=f'gay r8 machine')
                    emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                    await reply(embed=emb)
                    return
                colour = colour(rate)
                emb = nextcord.Embed(description=f'{person} is {rate}% gay 🏳️‍🌈', color=colour)
                emb.set_author(name=f'gay r8 machine')
                emb.set_footer(text=f'APU Utils | Made by {sqdname}', icon_url=client.user.avatar.url)
                await reply(embed=emb)
        # crash
        elif msg == 'crash':
            if author.id == sqd or author.id in admins:
                await reply('**`client.close()`ing...**')
                await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'`client.close()`ed.'), status=nextcord.Status.dnd)
                await logchannel.send(f'**{p}{msg}** called by Sqd. Trying to crash on railway!')
                time = timenow()
                print('\n{time} trying to crash lol')
                await Cbsbs()
                await gg(f='Goffy liek Tea!',fg='345')
                await Nit
                await time
                await random.rsndint()
                await e
                await cmon_crash
            else: await reply(f'**{no} You do not have permission to use this command!**')
        # proprietary
        elif msg.startswith('proprietary') or msg.startswith('p'):
            if author.id in admins or author.id == sqd:
                if msg.startswith('proprietary ') or msg.startswith('p '):
                    if msg.startswith('proprietary '):
                        msg = msg.split('proprietary ', 1)[1]
                        os.environ['msg'] = msg
                    if msg.startswith('p '):
                        msg = msg.split('p ', 1)[1]
                        os.environ['msg'] = msg
                    id = os.getenv('msg')
                    id = ping_replace(id)
                    try:
                        member = author.guild.get_member(int(id))
                        await member.edit(nick='proprieraryuser')
                        await reply(f'**Successfully proprieraried {member.mention}\'s nickname.**')
                        return
                    except Exception as e:
                        await reply(f'usage: `{p}proprietary <member>`\n**`Exception:`**` {e}`')
                        return
            else:
                await reply(f'**{no} You do not have permission to use this command!**')
        # fosslist
        elif msg == 'fosslist': await reply('''> **Useful lists with FOSS alternatives and software:**
<https://privacytools.io> -- **FOSS** and private alternatives to proprietary crap.
<https://opensource.builders> -- Tool to find **FOSS** alternatives to proprietary software you might use.
*Also allows you to specify the programming language and license.*''')
        # sourcecode
        elif msg == 'sc' or msg == 'sourcecode' or msg == 'source-code' or msg == 'source' or msg == 'code': await reply('shut up and here\'s my code: <https://github.com/SqdNoises/apu>')
        ### TYPE COMMANDS ABOVE THIS LINE ###
        else: await reply(f'**Command `{p}{msg}` not found!**')
    
    if msg == cum or msg == cum2: await reply(f'Hi! I am **APU Utils**.\nMy prefix is `{p}` and if you want a list of my commands, please type `{p}help`.\n\nRan on limux using the python3 package.\n**Currently running on:** `{userHost}`\n**Ping:** {round(client.latency * 1000)}ms\n*Coded by Sqd in Python with the `nextcord` library.*')
    
    if '🥺' in msg: await react('<:3D_Pleading_Face:909657424099700808>')
    
    if lowmsg == 'ping' or lowmsg == 'i hate ping' or msg == 'i hate pings':
        await reply('Ping?')
        await sendmsg('<a:Angry_Ping_Happy:909658888511586314>')
    
    if lowmsg == 'ollie': await reply('<:ollie:909659005197094913>')
    
    if lowmsg == 'uwu': await reply('owo')
    
    if lowmsg == 'owo': await reply('uwu')
    
    if lowmsg == 'hi' or lowmsg == 'hello': await sendmsg('<a:Birb_Waving:909658044416270356>')
    
    if '😳' in msg: await react('<:cursed_flushed:914769560043946025>')
    
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

    if 'closed-source' in lowmsg or 'closed source' in lowmsg: await reply('**Proprietary software** is **__bad__** for your **health** and **privacy**')
        
    if 'proprietary' in lowmsg and 'anti-proprietary' not in lowmsg and 'antiproprietary' not in lowmsg and 'anti proprietary' not in lowmsg and 'not proprietary' not in lowmsg and 'closed-source' not in lowmsg and 'closed source' not in lowmsg: await reply('**Proprietary software** is **__bad__** for your **health** and **privacy**')

    if lowmsg == ':gigachad:':
        await reply('Here, lemme help you.')
        await sendmsg('<:gigachad:901804317512720394>')

    if 'gigachad' in lowmsg and ':gigachad:' not in lowmsg or 'giga chad' in lowmsg or 'i use arch btw' in lowmsg or 'i use debian btw' in lowmsg or 'i use mint btw' in lowmsg or 'i use garuda btw' in lowmsg: await react('<:gigachad:901804317512720394>')
    
    if lowmsg == 'manjaro': await sendmsg('<:manjaro:901827004704374854>')
    
    if lowmsg == 'kali': await sendmsg('<:kali:901833149644963870>')

    if lowmsg == 'arch': await sendmsg('<:arch:901825671746166845>')
    
    if lowmsg == 'debian': await sendmsg('<:debian:901826706107686982>')
    
    if lowmsg == 'mint': await sendmsg('<:mint:901826533537247334>')

    if lowmsg == 'your mom': await reply('what?')
    
    if lowmsg == 'hack' or lowmsg == 'hacked': await reply(file=nextcord.File('files/media/hacc.gif'))
        
    if cum in msg or cum2 in msg:
        if 'are you watching me' in msg or 'are u watching me' in msg or 'are you fucking watching me' in msg or 'are u fucking watching me' in msg: await reply('I\'m watching you.')
    
    if msg == '<@&903299738542161962>': await reply('You\'re pinging my integration role, you dum dummy dumbo head.')

    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa pee you you tils'): await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa p u u tils'): await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaa pu utils'): await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if lowmsg.startswith('aaa') and lowmsg.endswith('aaapu utils'): await reply('No, it\'s **APU Utils**, not **' + msg + '** you dumbo head.')
    
    if msg == '@/home/sqd': await reply(file=nextcord.File('files/media/--home-sqd.jpg'))

# on member join
@client.event
async def on_member_join(member):
    # Anti Proprietary Union
    if member.guild.id == 901201688008990750: pass
    else: return
    print(f'{member} joined')
    channel = await member.create_dm()
    try:
        await channel.send('Hello ' + member.mention + '!\nWelcome to **Anti Proprietary Union**!\n__Here\'s what you should do to get started__:\n> Read the rules to avoid getting punished. (<#901519584102854687>)\n> Talk in <#911904177603633162> chat!\nHope you have fun in our server.\n**Server invite:** https://discord.gg/7bDvDnpUZC\n\n**#open-source-gang** ❤️')
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
    # Anti Proprietary Union
    if member.guild.id == 901201688008990750: pass
    else: return
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
    return
    # Anti Proprietary Union
    if payload.guild_id == 901201688008990750: pass
    else: return
    if payload.channel_id == 902785006173315072: return
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
                if num == None: os.environ['num'] = '0'
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
**Message author**: `{message.author}`
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
**Message author**: `{message.author}`
**Message author ID**: {message.author.id}''')
            await logchannel.send(f'{message.content}')

# on message edit
@client.event
async def on_message_edit(before, after):
    # Anti Proprietary Union
    if before.guild.id == 901201688008990750: pass
    else: return
    return
    #print(f'\n\nB E F O R E :   {before}\n')
    #print(f'\n\nA F T E R :   {after}\n')
    pass

# on raw message edit
@client.event
async def on_raw_message_edit(payload):
    # Anti Proprietary Union
    if payload.guild_id == 901201688008990750: pass
    else: return
    return
    print(f'\n\nP A Y L O A D :   {payload}\n')
    json_payloaddata = json.loads(str(payload.data))

# on reaction add
@client.event
async def on_reaction_add(reaction, user):
    # Anti Proprietary Union
    if payload.guild_id == 901201688008990750: pass
    else: return
    react = reaction.message.add_reaction
    if str(reaction) == '😳': await react('<:cursed_flushed:914769560043946025>')

# logging into APU Utils
print("Logging into APU Utils...\n\n")
client.run(never_gonna_give_you_up)