import discord
import json
import os
import random
import asyncio
import aiofiles
import datetime
import math
import aiosqlite
#from datetime import datetime
from discord.ext import commands
from discord.ui import Select, View
#from discord.ui import Select
from threading import Thread

intents = discord.Intents().all()
intents.members = True
intents.messages = True
client = discord.Client(intents = intents)

def get_prefix(client,message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents = intents)
os.chdir(r'C:\Users\Administrator\Desktop\ccat discord bot')
client.remove_command("help")
client.warnings = {} # guild_id : {member.id: [count, [(admin_id, reason)]]
client.multiplier = 1
commands = 'Commands: 35'
version = 'Version: 1.6'
name = 'ccat | c!help'
streamingurl = 'https://www.youtube.com/watch?v=T4U6JKT-c0c&t=21228s'

async def initialize():
    await client.wait_until_ready()
    client.db = await aiosqlite.connect("expData.db")
    await client.db.execute("CREATE TABLE IF NOT EXISTS guildData (guild_id int, user_id int, exp int, PRIMARY KEY (guild_id, user_id))")

#async def update_presence():
#    while True:
#        await client.change_presence(activity=discord.Game(name='c'))
#        #await asyncio.sleep(0)
#        await client.change_presence(activity=discord.Game(name='cc'))
#        await asyncio.sleep(1)
#        await client.change_presence(activity=discord.Game(name='cca'))
#        await asyncio.sleep(1)
#        await client.change_presence(activity=discord.Game(name='ccat'))
#        await asyncio.sleep(0)

@client.event
async def on_ready():
    print("")

class MySelect(View):

#, emoji="😭"

    @discord.ui.select(
        placeholder="Wähle deine Help Seite",
        options=[
            #discord.SelectOption(label="Help", value="1", description=""),
            discord.SelectOption(label="Moderation", value="2", description=""),
            discord.SelectOption(label="Standart", value="3", description=""),
            discord.SelectOption(label="Leveling", value="4", description=""),
            discord.SelectOption(label="Fun", value="5", description=""),
            discord.SelectOption(label="Settings", value="6", description=""),
            #discord.SelectOption(label="Edit Message", value="2", description="Hi was los 2"),
            #discord.SelectOption(label="Normal Embed", value="3", description="Hi was los 3")
        ]
    )

    async def select_callback(self, select, interaction):
        select.disabled=True
        #if select.values[0] == "1":
            #em = discord.Embed(title = "Hier sind alle Help Seiten")
            ##em.set_author(name="edited embed")
            #em.add_field(name="Help", value="Help", inline=True),
            #em.add_field(name="Moderation", value="Moderation", inline=True),
            #em.add_field(name="Standart", value="Standart", inline=True),
            #em.add_field(name="Leveling", value="Leveling", inline=True),
            #em.add_field(name="Fun", value="Fun", inline=True),
            #em.add_field(name="Settings", value="Settings", inline=True),
            #em.set_footer(text = f"{commands}")
            #await interaction.response.edit_message(embed=em)
        if select.values[0] == "2":
            em2 = discord.Embed(colour=discord.Colour.red(), title = f"Moderation", description=f"`ban`, `unban`, `kick`, `mute`, `unmute`, `clear`, `slowmode`, `nick`, `lock/unlock`, `announce`, `abstimmung`, `addrole`, `removerole`, `delchannel`, `crechannel`")
            em2.set_footer(text = f"{commands}")
            await interaction.response.edit_message(embed=em2)
        if select.values[0] == "3":
            em3 = discord.Embed(colour=discord.Colour.red(), title = f"Standart", description=f"`serverinfo`, `userinfo`, `avatar`, `ping`, `changelog`, `credits`, `createembed`, `invite`, `servers`")
            em3.set_footer(text = f"{commands}")
            await interaction.response.edit_message(embed=em3)
        if select.values[0] == "4":
            em4 = discord.Embed(colour=discord.Colour.red(), title = f"Leveling", description=f"`stats`, `leaderboard`")
            em4.set_footer(text = f"{commands}")
            await interaction.response.edit_message(embed=em4)
        if select.values[0] == "5":
            em5 = discord.Embed(colour=discord.Colour.red(), title = f"Fun", description=f"`cool`, `gay`, `pp`, `hacking`, `emojify`, `roll`")
            em5.set_footer(text = f"{commands}")
            await interaction.response.edit_message(embed=em5)
        if select.values[0] == "6":
            em6 = discord.Embed(colour=discord.Colour.red(), title = f"Settings", description=f"`prefix`, `setup`")
            em6.set_footer(text = f"{commands}")
            await interaction.response.edit_message(embed=em6)
        #if select.values[0] == "3":
        #    await interaction.response.send_message("Hi you SUCK MY DICK")

@client.command()
async def help(ctx):
    helpnew = discord.Embed(title = "Danke das du mich hinzugefügt hast!")
    #em.set_author(name="edited embed")
    #helpnew.add_field(name="Help", value="Help", inline=True),
    #helpnew.add_field(name="Moderation", value="Moderation", inline=True),
    #helpnew.add_field(name="Standart", value="Standart", inline=True),
    #helpnew.add_field(name="Leveling", value="Leveling", inline=True),
    #helpnew.add_field(name="Fun", value="Fun", inline=True),
    #helpnew.add_field(name="Settings", value="Settings", inline=True),
    helpnew.set_footer(text = f"{commands}")

    view = MySelect()
    await ctx.send(embed = helpnew, view=view)

@client.event
async def on_ready():

#    class Menu(discord.ui.View):
#        def __init__(self):
#            super().__init__()
#            self.value = None
#    
#        @discord.ui.button(label="Send Message", style=discord.ButtonStyle.grey)
#        async def menu1(self, button: discord.ui.Button, interaction: discord.Interaction):
#            await interaction.response.send_message("Hi")

#    @client.command()
#    async def menu8(ctx):
#        view = Menu()
#        await ctx.reply(view=view)

    for guild in client.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        client.warnings[guild.id] = {}

    for guild in client.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()#

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]



    #print('ok')
    print('═══════════INFORMS═══════════')
    print('Eingeloggt als:', client.user.name)
    print('Made by ccat')
    print(f'Server: {len(client.guilds)}')
    print(f'{version}')
    print(f'{commands} geladen')
    print('═══════════CONSOLE════════════')
    #await client.change_presence(activity=discord.Game('ccat'))
    #client.loop.create_task(update_presence())

    #main()
    #t = Thread(target=update_presence)
    #t.start()
    #await client.chane_presence(activity = discord.Playing(name = "Fortnite"))
    await client.change_presence(activity = discord.Streaming(name = f"{name}", url = f"{streamingurl}"))

@client.command()
async def servers(ctx):
    servers = discord.Embed(title=f"Ich bin auf {len(client.guilds)} servern drauf", colour=discord.Colour.red())
    #servers.add_field(name="", value=f"")

    await ctx.send(embed = servers)

@client.event
async def on_message(message):
    if not message.author.bot:
        cursor = await client.db.execute("INSERT OR IGNORE INTO guildData (guild_id, user_id, exp) VALUES (?,?,?)", (message.guild.id, message.author.id, 1)) 

        if cursor.rowcount == 0:
            await client.db.execute("UPDATE guildData SET exp = exp + 1 WHERE guild_id = ? AND user_id = ?", (message.guild.id, message.author.id))
            cur = await client.db.execute("SELECT exp FROM guildData WHERE guild_id = ? AND user_id = ?", (message.guild.id, message.author.id))
            data = await cur.fetchone()
            exp = data[0]
            lvl = math.sqrt(exp) / client.multiplier
        
            if lvl.is_integer():
                await message.channel.send(f"{message.author.mention} du bist aufgestiegen! Dein Level: {int(lvl)}.")

        await client.db.commit()

    await client.process_commands(message)

@client.command()
async def stats(ctx, member: discord.Member=None):
    if member is None: member = ctx.author

    # get user exp
    async with client.db.execute("SELECT exp FROM guildData WHERE guild_id = ? AND user_id = ?", (ctx.guild.id, member.id)) as cursor:
        data = await cursor.fetchone()
        exp = data[0]

        # calculate rank
    async with client.db.execute("SELECT exp FROM guildData WHERE guild_id = ?", (ctx.guild.id,)) as cursor:
        rank = 1
        async for value in cursor:
            if exp < value[0]:
                rank += 1

    lvl = int(math.sqrt(exp)//client.multiplier)

    current_lvl_exp = (client.multiplier*(lvl))**2
    next_lvl_exp = (client.multiplier*((lvl+1)))**2

    lvl_percentage = ((exp-current_lvl_exp) / (next_lvl_exp-current_lvl_exp)) * 100

    embed = discord.Embed(title=f"Stats von {member.name}", colour=discord.Colour.gold())
    embed.add_field(name="Level", value=str(lvl))
    embed.add_field(name="Exp", value=f"{exp}/{next_lvl_exp}")
    embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}")
    embed.add_field(name="Level fortschritt", value=f"{round(lvl_percentage, 2)}%")

    await ctx.send(embed=embed)

@client.command()
async def leaderboard(ctx): 
    buttons = {}
    for i in range(1, 6):
        buttons[f"{i}\N{COMBINING ENCLOSING KEYCAP}"] = i # only show first 5 pages

    previous_page = 0
    current = 1
    index = 1
    entries_per_page = 10

    embed = discord.Embed(title=f"Leaderboard Page {current}", description="", colour=discord.Colour.gold())
    msg = await ctx.send(embed=embed)

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        if current != previous_page:
            embed.title = f"Leaderboard Page {current}"
            embed.description = ""

            async with client.db.execute(f"SELECT user_id, exp FROM guildData WHERE guild_id = ? ORDER BY exp DESC LIMIT ? OFFSET ? ", (ctx.guild.id, entries_per_page, entries_per_page*(current-1),)) as cursor:
                index = entries_per_page*(current-1)

                async for entry in cursor:
                    index += 1
                    member_id, exp = entry
                    member = ctx.guild.get_member(member_id)
                    embed.description += f"{index}) {member.mention} : {exp}\n"

                await msg.edit(embed=embed)

        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return await msg.clear_reactions()

        else:
            previous_page = current
            await msg.remove_reaction(reaction.emoji, ctx.author)
            current = buttons[reaction.emoji]

#for filename in os.listdir('cogs'):
#    if filename.endswith('.py'):
#        client.load_extension(f'cogs.{filename[:-3]}')

#@client.event
#async def on_member_join(member):
#    await client.get_channel(988530396067147796).send(f"was geht {member.mention}")

@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
        
    prefixes[str(guild.id)] = "c!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

#@client.event
#async def on_message(message):
#    bot = f'<@>'
#    if message.content == bot:
#        await message.channel.send("Wat willst du den")
#    else:
#        return

@client.command()
async def prefix(ctx, prefix):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)

        await ctx.send(f"Der prefix wurde zu {prefix} geändert")

@client.event
async def on_messages(msg):
    try:

        if msg.mentions[0] == client.user:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
        
            pre = prefixes[str(msg.guild.id)] = "c!"

            await msg.channel.send(f"Mein Prefix für diesen Server ist {pre}")

    except:
        pass

    await client.process_commands(msg)

# Vinted Welcome Message

#@client.event
#async def on_member_join(member):
#     welcome = discord.Embed(title="Willkommen", color=0x3498db)
#    welcome.add_field(name='Vinted Roleplay', value=f"{member.mention}, willkommen auf GTA 5: Vinted Roleplay!", inline=False)
#    welcome.set_image(url="https://cdn.discordapp.com/attachments/972869762663194744/988903523796262962/cc97449acf5602ff880b37a3e0cc9b809d1_1.png?size=4096")
#
#    await client.get_channel(987784611616669716).send(embed=welcome)

# Log System ccat

#@client.event
#async def on_message_edit(before, after):
#    #z = await client.get_channel(994355454333427773)
#    
#    log2 = discord.Embed(title = f"{before.author} hat seine Nachricht bearbeitet", description = f"Davor: {before.content}\nDanach: {after.content}\nSender: {before.author.mention}\nIn Channel: {before.channel.mention}")
#    log2.set_author(name = after.content)
#    #await z.send(embed=log2)
#    await client.get_channel(994355454333427773).send(embed=log2)

#@client.event
#async def on_member_update(before, after):
    #z = await client.get_channel(994355454333427773)

    #if len(before.roles) > len(after.roles):
   #     role = next (role for role in before.roles if role not in after.roles)
   #     log3 = discord.Embed(title = f"{before.author} seine Rolle wurde weg genommen", description = f"{role.name} wurde entfernt von {before.author.mention}")
   ## elif len(after.roles) > len(before.roles):
   #     role = next (role for role in after.roles if role not in before.roles)
   #     log4 = discord.Embed(title = f"{before.author} hat eine rolle bekommen", description = f"{role.name} wurde hinzugefügt zu {before.author.mention}")
  #  elif before.nick != after.nick:
  #      log5 = discord.Embed(title = f"{before.author} sein Nickname wurde geändert", description = f"Davor: {before.nick}\n Danach: {after.nick}")
  #  else:
  #      return
  ##  log3.set_author(name = after.name)
  #  log4.set_author(name = after.name)
 #   log5.set_author(name = after.name)
 ##   await client.get_channel(994355454333427773).send(embed=log3)
 #   await client.get_channel(994355454333427773).send(embed=log4)
#    await client.get_channel(994355454333427773).send(embed=log5)
#    #await z.send(embed = log3)
#    #await z.send(embed = log4)
#    #await z.send(embed = log5)

#@client.event
#async def on_guild_channel_create(channel):
#    #z = await client.get_channel(994355454333427773)
#    
#    log6 = discord.Embed(title = f"{channel.name} wurde erstellt", description = channel.mention)
#    await client.get_channel(994355454333427773).send(embed=log6)
#    #await z.send(embed=log6)

#@client.event
#async def on_guild_channel_delete(channel):
#    #z = await client.get_channel(994355454333427773)
#    
#    log7 = discord.Embed(title = f"{channel.name} wurde gelöscht")
#    await client.get_channel(994355454333427773).send(embed=log7)
#    #await z.send(embed=log7)

# Level

#@client.event
#async def on_member_join(member):
#    with open('users.json', 'r') as f:
#        users = json.load(f)
#
#    await update_data(users, member)
#
#    with open('users.json', 'w') as f:
#        json.dump(users, f)

#@client.event
#async def on_message(message):
#    with open('users.json', 'r') as f:
#        users = json.load(f)
#
#    await update_data(users, message.author)
#    await add_exp(users, message.author, 5)
#    await level_up(users, message.author, message.channel)
#
#   with open('users.json', 'w') as f:
#       json.dump(users, f)

#    async def update_data(users, user):
#        if not user.id in users:
#            users[user.id] = {}
#            users[user.id]['exp'] = 0
#            users[user.id]['level'] = 1

#    async def add_exp(users, user, exp):
#        users[user.id]['exp'] += exp

#    async def level_up(users, user, channel):
#        exp = users[user.id]['exp']
#        lvl_start = users[user.id]['level']
#        lvl_end = int(exp ** (1/4))

#        if lvl_start < lvl_end:
#            await client.send_message(channel, '{} ist ein level aufgestiegen zu level {}'.format(user.mention, lvl_end))

@client.command()
async def delchannel(ctx, channel: discord.TextChannel):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_channels):
        await ctx.send(embed = perm)
        return

    dchannel = discord.Embed(timestamp=ctx.message.created_at, title = f"{channel} wurde gelöscht!")

    await ctx.send(embed = dchannel)
    await channel.delete()

@client.command()
async def crechannel(ctx, channelName):
    guild = ctx.guild

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_channels):
        await ctx.send(embed = perm)
        return

    dchannel = discord.Embed(timestamp=ctx.message.created_at, title = "{} wurde erstellt".format(channelName))

    await ctx.send(embed = dchannel)
    await guild.create_text_channel(name='{}'.format(channelName))

#@client.command()
#async def warn(ctx, member: discord.Member=None, *, reason=None):
#    if member is None:
#        return await ctx.send("Gebe einen User an")
#
#    if reason is None:
#        return await ctx.send("Gebe einen Grund an")
#
#    try:
#        first_warning = False
#        client.warnings[ctx.guild.id][member.id][0] += 1
#        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))
#
#    except KeyError:
#        first_warning = True
#        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]
#
#    count = client.warnings[ctx.guild.id][member.id][0]
#
#    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
#        await file.write(f"{member.id} {ctx.author.id} {reason}\n")
#
#    await ctx.send(f"**{member.mention}** wurde gewarnt!\n\nGrund: `{reason}`")

#@client.command()
#async def warnings(ctx, member: discord.Member=None):
#    if member is None:
#        return await ctx.send("Gebe einen User an")

#    embed = discord.Embed(title=f"Warnings für {member.name}", description="",  colour=discord.Colour.red())
#    try:
#        i = 1
#        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
#            admin = ctx.guild.get_member(admin_id)
#            embed.description += f"**Warning {i}** wurde gegeben von: {admin.mention} für: `{reason}`\n"
#            i += 1

#        await ctx.send(embed=embed)

#    except KeyError:
#        await ctx.send("Dieser User hat keine Warns.")

@client.command()
async def ping(ctx):
    ping = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    ping.add_field(name='Bot Speed', value=f'{round(client.latency * 1000)}ms', inline=False)
    await ctx.send(embed=ping)

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    kick = discord.Embed(timestamp=ctx.message.created_at, title = f"{member.mention} wurde gekickt", color=ctx.author.color)

    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    await member.kick(reason=reason)
    await ctx.send(embed = kick)

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    ban = discord.Embed(timestamp=ctx.message.created_at, title = f"{member.mention} wurde gebannt", color=ctx.author.color)

    #await ctx.send(embed = perm)

    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send(embed = perm)
        await ctx.send('Du hast keine rechte')
        return
    await member.send(f"Du wurdest auf {ctx.guild} gebannt!")
    await member.ban(reason=reason)
    await ctx.send(embed = ban)

@client.command()
async def unban(ctx, *, member):

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    unban = discord.Embed(timestamp=ctx.message.created_at, title = f"{user.mention} wurde entbannt", color=ctx.author.color)

    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed = unban)
            #await ctx.send(f'{user.mention} wurde entbannt')
            return

@client.command()
async def nick(ctx, member: discord.Member, nick):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    nickname = discord.Embed(timestamp=ctx.message.created_at, title = f"Der nickname von {member.name} wurde geändert zu {nick}", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_nicknames):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return

    await member.edit(nick=nick)
    await ctx.send(embed=nickname)

@client.command()
async def lock(ctx):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    lock = discord.Embed(timestamp=ctx.message.created_at, title = f"Hier wird erstmal nicht mehr geschrieben", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_channels):
        await ctx.send(embed = perm)
        return

    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=lock)

@client.command()
async def unlock(ctx):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    unlock = discord.Embed(timestamp=ctx.message.created_at, title = f"Ihr könnt wieder schreiben meine Friends", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_channels):
        await ctx.send(embed = perm)
        return

    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(embed=unlock)

@client.command()
async def clear(ctx, amount=0):

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)
    #await ctx.send(embed = perm)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    #amount = amount+0
    #if amount > 100:
    #    await ctx.send(embed = clear1)
    #    #await ctx.send('Ich kann nicht mehr als 100 nachrichten löschen')
    #else:
    #    await ctx.channel.purge(limit=amount)
    #    await ctx.send(embed = clear2)
    #    #await ctx.send(f'Es wurden {amount} Nachrichten gelöscht')

    if amount > 1000:
        clear1 = discord.Embed(timestamp=ctx.message.created_at, title = f"Ich kann nicht so viele Nachrichten löschen. {amount}/1000", color=ctx.author.color)
        await ctx.send(embed = clear1)
    else:
        count_members = {}
        messages = await ctx.channel.history(limit=amount).flatten()
        for message in messages:
            if str(message.author) in count_members:
                count_members[str(message.author)] += 1
            else:
                count_members[str(message.author)] = 1
        new_string = []
        deleted_messages = 0
        for author, message_deleted in list(count_members.items()):
            new_string.append(f'**{author}**: {message_deleted}')
            deleted_messages += message_deleted
        final_string = '\n'.join(new_string)
        await ctx.channel.purge(limit=amount+1)
        if deleted_messages == 1:
            clear2 = discord.Embed(timestamp=ctx.message.created_at, title = f"{deleted_messages} Nachricht wurde gelöscht!\n\n{final_string}", color=ctx.author.color)
            #clear2.add_field(name=".", value=f"{final_string}", inline=False)
            msg = await ctx.send(embed = clear2)
        elif deleted_messages == 0:
            clear4 = discord.Embed(timestamp=ctx.message.created_at, title = f"Keine Nachrichten wurden gelöscht. Sei dir sicher das die Nachrichten nicht länger als 2 Wochen alt sind", color=ctx.author.color)
            #clear2.add_field(name=".", value=f"{final_string}", inline=False)
            msg = await ctx.send(embed = clear4)
        else:
            clear3 = discord.Embed(timestamp=ctx.message.created_at, title = f"{deleted_messages} Nachrichten wurden gelöscht!\n\n{final_string}", color=ctx.author.color)
            #clear2.add_field(name=".", value=f"{final_string}", inline=False)
            msg = await ctx.send(embed = clear3)
        await asyncio.sleep(8)
        await msg.delete()

@client.command()
async def mute(ctx, member:discord.Member, *, reason=None):
    guild = ctx.guild

    mute1 = discord.Embed(timestamp=ctx.message.created_at, title = f"Ich habe {member.name} gemuted", color=ctx.author.color)

    mute2 = discord.Embed(timestamp=ctx.message.created_at, title = f"Du wurdest gemutet | Grund: {reason}", color=ctx.author.color)

    #mute2 = discord.Embed(timestamp=ctx.message.created_at, title = f"du wurdest auf **{guild.name}** gemuted | Grund: **{reason}**", color=ctx.author.color)

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    mutedRole = discord.utils.get(guild.roles, name='Muted')

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed = mute1)
    await member.send(embed = mute2)

@client.command()
async def createembed(ctx, *, title=None):
    createembed = discord.Embed(timestamp=ctx.message.created_at, title = f"", description=f"{title}", color=ctx.author.color)
    #createembed.add_field(name=f"{name}", value=f"{value}", inline=False)
    await ctx.send(embed = createembed)

@client.command()
async def setup(ctx):
    guild = ctx.guild

    setup = discord.Embed(timestamp=ctx.message.created_at, title = "Setup wurde ausgeführt", color=ctx.author.color)

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_guild):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)
        await ctx.send(embed = setup)
        return

@client.command()
async def addrole(ctx, member:discord.Member, role:discord.Role):
    guild = ctx.guild

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_roles):
        await ctx.send(embed = perm)
        return

    addrole = discord.Embed(timestamp=ctx.message.created_at, title = "Rolle wurde gegeben!", color=ctx.author.color)

    role = discord.utils.get(guild.roles, name=f'{role}')

    await member.add_roles(role)
    await ctx.send(embed = addrole)

@client.command()
async def removerole(ctx, member:discord.Member, role:discord.Role):
    guild = ctx.guild

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_roles):
        await ctx.send(embed = perm)
        return

    removerole = discord.Embed(timestamp=ctx.message.created_at, title = "Rolle wurde entfernt!", color=ctx.author.color)

    role = discord.utils.get(guild.roles, name=f'{role}')

    await member.remove_roles(role)
    await ctx.send(embed = removerole)

@client.command()
async def unmute(ctx, member:discord.Member, *, reason=None):
    unmute1 = discord.Embed(timestamp=ctx.message.created_at, title = "Die mute Rolle wurde nicht gefunden", color=ctx.author.color)

    unmute2 = discord.Embed(timestamp=ctx.message.created_at, title = "Ich habe ihn unmuted", color=ctx.author.color)

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name='Muted')

    if not mutedRole:
        await ctx.send(embed = unmute1)
        #await ctx.send("Die mute Rolle wurde nicht gefunden")
        return

    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(embed = unmute2)
    #await ctx.send('Ich habe ihn unmuted')

@client.command()
async def slowmode(ctx,time:int):
    slowmode1 = discord.Embed(timestamp=ctx.message.created_at, title = "Der Slowmodus wurde ausgeschalten", color=ctx.author.color)

    slowmode2 = discord.Embed(timestamp=ctx.message.created_at, title = "Der Slowmodus geht nicht über 6 stunden", color=ctx.author.color)

    slowmode3 = discord.Embed(timestamp=ctx.message.created_at, title = f"Der Slowmodus ist jetzt aktiv. Die Member können alle {time} sekunden eine Nachricht schreiben", color=ctx.author.color)

    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)
    #await ctx.send(embed = perm)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        #await ctx.send('Du hast keine rechte')
        return
    try:
        if time == 0:
            await ctx.send(embed = slowmode1)
            #await ctx.send('Slowmode ausgeschaltet')
            await ctx.channel.edit(slowmode_delay = 0)
        elif time > 21600:
            await ctx.send(embed = slowmode2)
            #await ctx.send('Du kannst nicht den Slowmode über 6 stunden machen')
            return
        else:
            await ctx.channel.edit(slowmode_delay = time)
            await ctx.send(embed = slowmode3)
            #await ctx.send(f'Der Slowmode ist jetzt aktiv. Die member können alle {time} sekunden eine Nachricht schreiben')
    except Exception:
        await print('Slowmode hat nen error lol')

@client.command()
async def serverinfo(ctx):
    owner = ctx.guild.owner_id
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    serverinfoEmbed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name='Server Name', value=f"{ctx.guild.name}", inline=True)
    serverinfoEmbed.add_field(name='Server Owner', value=f"<@{owner}>", inline=True)
    serverinfoEmbed.add_field(name='Server ID', value=f"{ctx.guild.id}", inline=True)
    serverinfoEmbed.add_field(name='Text Channels', value=len(ctx.message.guild.text_channels), inline=True)
    serverinfoEmbed.add_field(name='VC Channels', value=len(ctx.message.guild.voice_channels), inline=True)
    serverinfoEmbed.add_field(name='Kategorien', value=len(ctx.message.guild.categories), inline=True)
    serverinfoEmbed.add_field(name='Mitglieder', value=ctx.guild.member_count, inline=True)
    serverinfoEmbed.add_field(name='Verify Level', value=str(ctx.guild.verification_level), inline=True)
    serverinfoEmbed.add_field(name='Höchste Rolle', value=ctx.guild.roles[-2], inline=True)
    serverinfoEmbed.add_field(name='Rollen', value=str(role_count), inline=True)
    serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=True)
    #serverinfoEmbed.add_field(name='Religion', value=ctx.message.guild.religion, inline=True)
    serverinfoEmbed.add_field(name='Erstellt am', value=ctx.guild.created_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=True)
    #serverinfoEmbed.set_author(name=ctx.guild.name,icon_url=ctx.guild.icon_url)

    await ctx.send(embed = serverinfoEmbed)

@client.command()
async def userinfo(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
        if role.name != "@everyone":
            rlist.append(role.mention)
    b = ','.join(rlist)

    userinfo = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    userinfo.set_author(name=f"User Info - {user}"),
    #userinfo.set_thumbnail(url=ctx.avatar_url),
    #userinfo.set_footer(text=f'Angefragt von - {ctx.author}'),
    #icon_url=user.avatar_url

    userinfo.add_field(name='ID:', value=user.id, inline=True)
    userinfo.add_field(name='Name', value=user.display_name, inline=True)
    userinfo.add_field(name='Tag', value=user.discriminator, inline=True)
    #userinfo.add_field(name=f'Rollen:({len{rlist}})', value=''.join([b])), inline=False)
    userinfo.add_field(name='Höchste Rolle:', value=user.top_role.mention, inline=True)
    userinfo.add_field(name='Erstellt am:', value=user.created_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=True)
    userinfo.add_field(name='Gejoint am:', value=user.joined_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=True)
    userinfo.add_field(name='Bot?', value=user.bot, inline=True)
    await ctx.send(embed=userinfo)

@client.command()
async def avatar(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    memberAvatar = member.avatar_url

    avaEmbed = discord.Embed(timestamp=ctx.message.created_at, title = f"{member.name} profilbild", color=ctx.author.color)
    avaEmbed.set_image(url = memberAvatar)
    #await ctx.send(embed = avaEmbed)

@client.command()
async def gay(ctx, member : discord.Member = None):
#    bot = f'<@988469919840604241>'
    #if ctx.content == bot:

    #if member == 940390771553628201:
    #    gay2Embed = discord.Embed(timestamp=ctx.message.created_at, title = f"ccat weiß wie gay du bist :d", color=ctx.author.color)
    #    gay2Embed.add_field(name = f"**{member.name}**", value = f"ist 0% gay", inline=True)
    #await ctx.send(embed = gay2Embed)

    if member == None:
        member = ctx.author

#    if ctx.content == bot:
#        await ctx.send("Bots sind nicht Gay")

    gayEmbed = discord.Embed(timestamp=ctx.message.created_at, title = f"ccat weiß wie gay du bist :d", color=ctx.author.color)
    gayEmbed.add_field(name = f"**{member.name}**", value = f"ist {random.randrange(101)}% gay", inline=True)
    await ctx.send(embed = gayEmbed)

@client.command()
async def cool(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    coolEmbed = discord.Embed(timestamp=ctx.message.created_at, title = f"ccat weiß wie cool du bist :d", color=ctx.author.color)
    coolEmbed.add_field(name = f"**{member.name}**", value = f"ist {random.randrange(101)}% cool", inline=True)
    await ctx.send(embed = coolEmbed)

@client.command()
async def pp(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    ppEmbed = discord.Embed(timestamp=ctx.message.created_at, title = f"ccat weiß wie groß dein cock ist :d", color=ctx.author.color)
    ppEmbed.add_field(name = f"**{member.name}**", value = f"hat einen {random.randrange(101)} zentimeter langen cock", inline=True)
    await ctx.send(embed = ppEmbed)

#@client.command()
#async def emojify(ctx, *, text=None):
#    emojis = []
#    for s in text.lower():
#        if s.isdecimal():
#            num2emo = {'0':'zero','1':'one','2':'two',
#                       '3':'three','4':'four','5':'five',
#                       '6':'six','7':'seven','8':'eight','9':'nine'}
#            emojis.append(f':{num2emo.get(text)}:')
#        elif text.isalpha():
#            emojis.append(f':regional_indicator_{text}:')
#        else:
#            emojis.append(s)
#    await ctx.send(' '.join(emojis))

@client.command()
async def emojify(ctx,*,text):
    emojis = []
    for beans in text.lower():
        if beans.isdecimal():
            num2word = {
                '0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
            emojis.append(f'f:{num2word.get(beans)}:')
        elif beans.isalpha():
            emojis.append(f':regional_indicator_{beans}:')
        else:
            emojis.append(beans)
    await ctx.send(' '.join(emojis))

@client.command()
async def invite(ctx):
    invite = discord.Embed(colour=discord.Colour.red(), title = f"Füg mich jetzt hinzu", description=f"**https://discord.com/api/oauth2/authorize?client_id=988469919840604241&permissions=8&scope=bot%20applications.commands**")
    await ctx.send(embed = invite)

@client.command()
async def changelog(ctx):
    changelog = discord.Embed(timestamp=ctx.message.created_at, title = "Changelogs", color=ctx.author.color)
    changelog.add_field(name = "12.07.2022", value = "Server counter", inline=False)
    changelog.add_field(name = "10.07.2022", value = "Serverinfo und Userinfo rework", inline=False)
    changelog.add_field(name = "10.07.2022", value = "2x Neue Commands", inline=False)
    changelog.add_field(name = "09.07.2022", value = "2x Neue Commands", inline=False)
    changelog.add_field(name = "09.07.2022", value = "Help rework", inline=False)
    changelog.set_footer(text= f"{version}")
    await ctx.send(embed = changelog)

@client.command()
async def credits(ctx):
    changelog = discord.Embed(timestamp=ctx.message.created_at, title = "Credits", color=ctx.author.color)
    changelog.add_field(name = "Ersteller", value = "'savage.#3881", inline=False)
    await ctx.send(embed = changelog)

@client.command()
async def abstimmung(ctx, channel: discord.TextChannel, *, abstimmun):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        return

    announce = discord.Embed(timestamp=ctx.message.created_at, title="Eine Abstimmung wurde erstellt", color=ctx.author.color)
    #announce.add_footer(text=f'Erstellt von {ctx.author.mention}')
    announce.add_field(name="Text: ", value=f'{abstimmun}', inline=True)
    announce.add_field(name="Channel: ", value=f"**{channel.mention}**", inline=True)
    #announce.add_footer(text=f'Erstellt von {ctx.author.mention}')
    
    await ctx.send(embed=announce)

    await ctx.channel.purge(limit=1)
    
    abstimmungEmbed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
    abstimmungEmbed.add_field(name='Abstimmung!', value=f'{abstimmun}')
    #abstimmungEmbed.add_footer(text=f'Erstellt von {ctx.author.mention}')
    message = await channel.send(embed=abstimmungEmbed)

    await message.add_reaction('✅')
    await message.add_reaction('❌')

@client.command()
async def announce(ctx, channel: discord.TextChannel, *, message):
    perm = discord.Embed(timestamp=ctx.message.created_at, title = "Du hast keine rechte", color=ctx.author.color)

    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send(embed = perm)
        return

    announce = discord.Embed(timestamp=ctx.message.created_at, title="Eine Announce wurde erstellt", color=ctx.author.color)
    #announce.add_footer(text=f'Erstellt von {ctx.author.mention}')
    announce.add_field(name="Text: ", value=message, inline=True)
    announce.add_field(name="Channel: ", value=f"**{channel.mention}**", inline=True)
    #announce.add_footer(text=f'Erstellt von {ctx.author.mention}')
    
    await ctx.send(embed=announce)

    announce=discord.Embed(timestamp=ctx.message.created_at, title=f"Announce", description=message, color=ctx.author.color)
    await channel.send(embed=announce)

@client.command()
async def hacking(ctx, *, member: discord.Member = None):  

    message = await ctx.send(f"Jetzt wird {member.name} gehackt...")
    await asyncio.sleep(1)

    await message.edit(content=f"Steam Account wird gesucht...")
    await asyncio.sleep(2)

    await message.edit(content=f"Steam Account gefunden und werden jetzt auf MMOGA verkauft")
    await asyncio.sleep(3)

    await message.edit(content=f"""Gefunden:
    Email: __***`{member.name}{random.randrange(1000)}@gmail.com`***__
    Passwort: __***`{member.name}{random.randrange(64)}`***__""")
    await asyncio.sleep(4)

    await message.edit(content=f"Weiter Accounts werden gesucht...")
    await asyncio.sleep(5)

    await message.edit(content=f"Discord Account gefunden")
    await asyncio.sleep(1)

    await message.edit(content=f"""Gefunden:
    Email: __***`{member.name}{random.randrange(70000)}`***__
    Passwort: __***`{member.name}{random.randrange(764)}`***__""")

@client.command()
async def giveaway(ctx):
    await ctx.send("Okay lass uns das Giveaway starten! Du hast zeit die fragen zu beantworten in 15 Sekunden")

    questions = ["In welchem Channel soll das Giveaway gehostet werden?", "Wielange soll das Giveaway gehen? (s|m|h|d)", "Was ist der Preis was man gewinnen kann?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Du warst nicht schnell genug sei bitte nächstes mal schneller!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"Du hast denn Channel nicht richtig gepingt. So musst du es machen {ctx.channel.mention}")

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"Du hast die zeit nicht richtig angegeben. Benutze (s|m|h|d)")
        return
    elif time == -2:
        await ctx.send(f"Gebe eine Zeit an mit (s|m|h|d)")
        return

    prize = answers[2]

    await ctx.send(f"Das Giveaway wird in {channel.mention} und wird enden in {answers[1]}")

    giveaway = discord.Embed(title = "Giveaway!", description = f"{prize}", color = discord.Colour.blue())

    giveaway.add_field(name = "Hosted by:", value = ctx.author.mention)

    giveaway.set_footer(text = f"endet in {answers[1]}")

    my_msg = await channel.send(embed = giveaway)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"{winner.mention} hat {prize} gewonnen! 🥳")

# 5 h = 5 * 60 * 60

def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

#@client.command()
#async def reroll(ctx, channel : discord.TextChannel, id_ : int):
#    try:
#        new_msg = await channel.fetch_message(id_)
#    except:
#        await ctx.send("Die ID ist inkorrekt eingegeben")
#        return
    
#    users = await new_msg.reactions[0].users().flatten()
#    users.pop(users.index(client.user))
#
#    winner = random.choice(users)

#    await channel.send(f"{winner.mention} ist der neue Gewinner. Und hat {prize} gewonnen!")

# Ticket System

#@client.event
#async def on_reaction_add(reaction,user):
#    ticket2 = discord.Embed(title=f"", description="Das **Team** wird sich um dein **Problem** kümmern", colour=discord.Colour.blue())
#    #ticket.set_author(name="TICKET")
#    #ticket.add_field(name="", value="um ein Ticket zu erstellen")
#    #ticket.set_footer(text=f"Angefordert von {ctx.author}")

#    if user.id == 988469919840604241:
#        return

#    if user.id != 988469919840604241:
#        guild = guildticket
#        #botrolle = discord.utils.get(guild.roles,id=994355275509268540)
#        channelexists = discord.utils.get(guild.text_channels, name=user.name.lower())
#        if channelexists:
#            None
#        else:
#            botrolle = discord.utils.get(guild.roles,id=988469919840604241)
#    emoji = '❌'
#    emoji2 = '✅'
#    if reaction.emoji == '🎫':
#        category = discord.utils.get(guild.categories, id=994355305456603177)
#        channel = await guild.create_text_channel(name=f"{user.name}", category=category)
#        await channel.set_permissions(user,send_messages=True)
#        message = await channel.send(embed = ticket2)
#        await message.add_reaction(emoji=emoji)
#        #await message.add_reaction(emoji=emoji)
#        #await channel.send("**```Das Team wird sich um dein Problem kümmern```**")
#        #await channel.send(f"{botrolle.mention}")

#    if reaction.emoji == '✅':
#        await reaction.message.channel.delete(reason=None)

#    if reaction.emoji == '❌':
#        channel = client.get_channel(name=f"{user.name}")
#        #channel = await guild.create_text_channel(name=f"{user.name}", category=category)
#        emoji3 = '✅'
#        message = await channel.send("Willst du wirklich dieses Ticket löschen?")
#        await message.add_reaction(emoji=emoji3)

#@client.command()
#async def close(ctx):
#        emoji = '✅'
#        emoji2 = '❌'
#        message = await ctx.send("Willst du wirklich dieses Ticket löschen?")
#        await message.add_reaction(emoji=emoji)
#        await message.add_reaction(emoji=emoji2)

#@client.command()
#async def ticket(ctx):
#    global guildticket
#    guildticket = ctx.guild
#    ticket = discord.Embed(title=f"", colour=discord.Colour.blue())
#    ticket.set_author(name="TICKET")
#    ticket.add_field(name="Drück auf das Emoji", value="um ein Ticket zu erstellen")
#    ticket.set_footer(text=f"Angefordert von {ctx.author}")

#    emoji= '🎫'
#    await ctx.channel.purge(limit=1)
#    message = await ctx.send(embed = ticket)
#    await message.add_reaction(emoji=emoji)

@client.command()
async def roll(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    rollEmbed = discord.Embed(timestamp=ctx.message.created_at, title = f"ccat weiß wie wieviel du würfeln kannst :d", color=ctx.author.color)
    rollEmbed.add_field(name = f"**{member.name}**", value = f"hat {random.randrange(6)} gewürfelt", inline=True)
    await ctx.send(embed = rollEmbed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe einen Member an", color=ctx.author.color)

        await ctx.send(embed=perm)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe einen Member an", color=ctx.author.color)

        await ctx.send(embed=perm)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe einen Member an", color=ctx.author.color)

        await ctx.send(embed=perm)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe einen Member an", color=ctx.author.color)

        await ctx.send(embed=perm)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe einen Member an", color=ctx.author.color)

        await ctx.send(embed=perm)

@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        perm = discord.Embed(timestamp=ctx.message.created_at, title = "Gebe die Sekunden an", color=ctx.author.color)

        await ctx.send(embed=perm)

if os.path.exists(os.getcwd() + "/token.json"):

    with open("./token.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]

client.loop.create_task(initialize())
client.run(token)
asyncio.run(client.db.cloe())