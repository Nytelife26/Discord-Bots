import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import os
import sys
import urllib
# If you don't have bs4 installed or discord.py, go to terminal or CMD or whatever you use and type the following:
# pip3 install bs4
# Then go to Discord.py's GitHub and follow the instructions to download it or run python3 -m pip install -U discord.py[voice] in CMD or Terminal

# WARNING - this bot only works on Python 3.5.x and above
# For earlier versions of Python go to the "legacy" folder

token = 'user account token goes here' 

description = '''CupOfJava is a selfbot created by Nyte for automatic moderation and other miscellaneous things'''
bot = commands.Bot(command_prefix='UsernameHere(', description=description, self_bot=True) # Change "UsernameHere(" to say your username followed by an opening parenthesis


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='a funny joke or something you want to appear as your playing status'), status=discord.Status.dnd) #Change the string in name=''
    print('CupOfJava - Selfbot version of SmartBrew')
    print('----------------------------------------')
    print('Be sure to keep me updated by going to my')
    print('GitHub repo! There might be an important')
    print('update / bug fix there for you')
    print('----------------------------------------')
    
            
@bot.command(pass_context=True, name='info)')
async def info(ctx):
    """Just an info command"""
    print('{} | Info ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    await bot.say("```md\n[ Command executed ][ Info ]\n< CupOfJava is a selfbot created by Nyte for automatic moderation and other miscellaneous things >\n[ Instance owner ][ {} ]\n[ GitHub link ][ https://github.com/Nytelife26/Discord-Bots ]```".format(bot.user))
    
@bot.command(pass_context=True, name='ping)')
async def ping(ctx):
    """Does what it says on the tin."""
    print('{} | Ping ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    ping = await bot.say("```md\n[ Command executed ][ Ping ]\n< Ping in progress >\n```")
    time = (ping.timestamp - ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(ping, "```md\n[ Command executed ][ Ping ]\n< Time taken to recieve / process command in milliseconds is {} ms >\n```".format(round(time)))

@bot.command(pass_context=True, name='logout)')
async def logout(ctx):
    """Gracefully exits CupOfJava - USE THIS INSTEAD OF CONSOLE WHEN POSSIBLE"""
    print('{} | Logout ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    await bot.say("```md\n[ Command executed ][ Logout ]\n< LOGGING OUT >\n```")
    await bot.logout()

@bot.command(pass_context=True, name="embed)")
async def embed(ctx, *, content : str=""):
    """Embeds the chosen message"""
    print('{} | Embed ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    if content == "":
        await bot.say("```md\n[ Command failed to execute ][ ArgumentError ]\n< Required argument was not defined >\n```")
    else:
        try:
            data = discord.Embed(description="CupOfJava - SELFBOT - Embed", colour=discord.Colour.purple())
            data.add_field(name=message.author.display_name + "#" + message.author.discriminator + " says", value=str(content))
            await bot.delete_message(message)
            await bot.say(embed=data)
        except:
            await bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the embed links permission so we cannot perform the task >\n```")
            
@bot.command(pass_context=True, name='yandere)')
async def yandere(ctx):
    """Random image from Yande.re | WARNING - DISPLAYS PORNOGRAPHIC CONTENT"""
    print('{} | Yandere ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    try:
        query = ("https://yande.re/post/random")
        page = await aiohttp.get(query)
        page = await page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="highres").get("href")
        await bot.edit_message(message, "```md\n[ Command executed ][ Yandere ]\n< Pulling random image from yande.re >\n```\n" + image)
    except Exception as e:
        await bot.edit_message("```md\n[ Command failed to execute ][ Non-bot error]\n< {} >".format(e))
        
@bot.command(name='restart)', pass_context=True)
async def restart(ctx):
    """Restarts CupOfJava"""
    print('{} | Restart ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    await bot.edit_message(message, "```md\n[ Command executed ][ Restart ]\n< RESTARTING >\n```")
    os.execlp('python', 'python', 'CupOfJava.py')
    await bot.logout()
    
@bot.command(name='discrim)', pass_context=True)
async def discrim(ctx, discrim : str = None):
    """Lists users with a certain discriminator"""
    print('{} | Discrim ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    if discrim == None:
        discrim = bot.user.discriminator
    discovered = []
    names = []
    for s in bot.servers:
        for m in s.members:
            if str(m.discriminator) == discrim and m != bot.user and not m.id in discovered:
                names.append(m.name)
                discovered.append(m.id)
    await bot.edit_message(message, "```md\n[ Command executed ][ Discriminator ]\n< Finding users with discriminator {} >\n```".format(str(discrim)))
    await bot.edit_message(message, message.content + "\n" + '```md\n[ Users found ][ {} ]\n< Listing users found >'.format(str(discrim)) + '\n#' + '\n#'.join(names) + '```')
    
@bot.command(name='purge)', pass_context=True)
async def purge(ctx, amount : int=20):
    """Cleans a channel with a definable limit
    By defaultthe amount is set to 20"""
    print('{} | Purge ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    invoking = ctx.message
    if amount <= 1: # if you truly are this lazy, then this limitation can be removed
        msg = await bot.say("```md\n[ Command failed to execute ][ layZ Error ]\n< Don't be so lazy! The defined amount of messages was either one or below, and I mean come on, you can delete one message on your own. It's easy! Just so we don't add to the hassle, we'll delete this for you in about a minute >\n```")
        await asyncio.sleep(60)
        await bot.delete_message(msg)
    else:
        message = await bot.say("```md\n[ Command executed ][ Purge ]\n < Kick back and have a CupOfJava, while CupOfJava [this selfbot] purges the channel! >\n```")
        await bot.delete_message(invoking)
        fails = 0
        async for x in bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=amount):
            try:
                await bot.delete_message(x)
            except:
                fails += 1
        await asyncio.sleep(2)
        await bot.edit_message(message, "```md\n[ Command finished ][ Purge ]\n< Purge finished with {} failed attempts >\n```".format(str(fails)))
        
                
@bot.command(name='silence)', pass_context=True)
async def silence(ctx, user : discord.Member):
    """Mutes a given user"""
    print('{} | Silence ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    server = ctx.message.server
    message = ctx.message
    try:
        for r in server.roles:
            await bot.remove_roles(user, r)
        role = discord.utils.get(server.roles, name='Muted')
        await asyncio.sleep(1)
        await bot.add_roles(user, role)
        await bot.edit_message(message, "```md\n[ Command executed ][ Silence ]\n< {}\{}#{} was muted successfully >\n```".format(str(user.id), str(user.display_name), str(user.discriminator)))
    except:
        await bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the manage roles permission or the Muted role does not exist so we cannot perform this task >\n```")
        return
        
    
@bot.command(name='uncensor)', pass_context=True)
async def uncensor(ctx, user : discord.Member):
    """Unmutes a given user"""
    print('{} | Uncensor ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    server = ctx.message.server
    message = ctx.message
    try:
        memberrole = discord.utils.get(server.roles, name='Members')
        muterole = discord.utils.get(server.roles, name='Muted')
        await bot.remove_roles(user, muterole)
        await bot.add_roles(user, role)
        await bot.edit_message(message, "```md\n[ Command executed ][ Uncensor ]\n< {}\{}#{} was unmuted successfully >".format(str(user.id), str(user.display_name), str(user.discriminator)))
    except:
        await bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the manage roles permission or the Muted role does not exist so we cannot perform this task >\n```")
        return
        
@bot.group(pass_context=True)
async def google(ctx):
        """Google search functions."""
        prefix = bot.command_prefix
        message = ctx.message
        if ctx.invoked_subcommand is None:
            await bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< No subcommand was passed on a command group >\n[ Retrieving list ][ Subcommands ]\n# images\n# maps\n# search\n[ Subcommands ][ Examples ]\n# {}google images) QUERY\n# {}google maps) QUERY\n# {}google search) QUERY\n ```".format(prefix, prefix, prefix))

@google.command(pass_context=True, name='images)')
async def images(ctx, *, query):
        message = ctx.message
        if query == "":
            await bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/search?tbm=isch&q="
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            await bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Imagae search mode\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))

@google.command(pass_context=True, name='maps)')
async def maps(ctx, *, query):
        message = ctx.message
        if query == "":
            await bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/maps/search/"
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            await bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Maps search mode\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))

@google.command(pass_context=True, name='search)')
async def search(ctx, *, query):
        message = ctx.message
        if query == "":
            await bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/search?q="
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            await bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Generic search mode\n\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))
                
@bot.command(pass_context=True, name='heil)')
async def heil(ctx):
    """HEIL!"""
    message = ctx.message
    await bot.edit_message(message, "***HEIL ~~HITLER~~ NYTE!***")
    await bot.say(":joy: :joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :rage: :rage: :rage: :rage: :rage: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :rage: :rage: :rage: :joy: :rage: :rage: :rage: :joy: \n:joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :rage: :rage: :joy: :joy: :joy: :rage: :rage: :rage: \n:rage: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :rage:\n:rage: :rage: :rage: :joy: :joy: :joy: :rage: :rage: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: \n:joy: :rage: :rage: :rage: :joy: :rage: :rage: :rage: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :rage: :rage: :rage: :rage: :rage: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :rage: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: \n:joy: :joy: :joy: :joy: :joy: :joy: :joy: :joy: :rage: :rage: :joy: :joy: :joy: :joy: :joy: :joy: :joy:")
        
        
@bot.command(pass_context=True, name='stfu)')
async def stfu(ctx):
    """Show people just how much you hate them with this command!"""
    message = ctx.message
    await bot.say("Shut the fuck up\nYou're a fucking cunt\nShut the fuck up\nYou're a stupid cunt, suck my dick\nShut the fuck up\nStop being a fucking cunt\nShut the fuck up\nNobody even wants you here")
    await asyncio.sleep(2)
    await bot.say("\n\nWhat?\nI just want to let you know, you're a stupid fucking cunt\nGo ahead and run your mouth, pussy, I don't give a fuck\nYou're a stupid piece of shit, you're a stupid fucking bitch\nGet the fuck up off my dick, get the fuck up off my dick, like\nPlease end your fucking life, please end your fucking life\nI really gotta emphasise, no one cares if you're alive\nYou're a fucking penis-hole, grab a dick and eat it whole\nI need to know if you were dropped when you were just a fetus though\nYou're so fucking ugly and your face is fucking foul, jeez\nYou're so fucking loud, can you shut your fucking mouth, can you")
    await asyncio.sleep(2)
    await bot.say("\n\nShut the fuck up\nYou're a fucking cunt\nShut the fuck up\nYou're a stupid cunt, suck my dick\nShut the fuck up\nStop being a fucking cunt\nShut the fuck up\nNobody even wants you here")
    await asyncio.sleep(2)
    await bot.say("\n\nClose your fucking mouth, you're just really fucking dense\nIf you hate me, why you talking? You don't make no fucking sense\nGot a sad life, sad life, go to fucking hell\nAre you stupid or disabled, man, I can't fucking tell\nMeh\nYou're a fucking dumb shit, you don't even run shit\nGet the fuck up out of my face and go to hell and eat a dick\nCome and catch these hands, boy\nCome and match these bands, boy\nI'm not crazy, I just do it all because I can, boy\nI hope you fucking die in a high-speed car crash\nI hope you fucking fall head-first and get your neck cracked\nI hope you have some beautiful children that die from cancer\nI hope you catch Zika when your wife gets pregnant\nI hope you win the lottery and die the next day\nAnd your daughter has to see you getting lowered in your grave")
    await asyncio.sleep(2)
    await bot.say("\n\nLike, uh, ooh- that was a little dark\nI'm sorry. Tha-that was a little dark. Very poor taste\nShut the fuck up\nI shouldn't have said that\nYou're a fucking cunt\nActually, no, I should have\nShut the fuck up\nActually, I didn't say enough\nYou're a stupid cunt, suck my dick\nShut the fuck up\nStop being a fucking cunt\nShut the fuck up\nNobody even wants you here")
    await asyncio.sleep(1)
    await bot.say("That song right there? `Pink Guy - STFU`, and it represents my feelings towards you :middle_finger:")
   
bot.run(token, bot=False)
