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
# pip install bs4
# Then go to Discord.py's GitHub and follow the instructions to download discord.py

# This is the legacy version, built for Python 3.4.2 and below
# If you have 3.4.2 or below, the main will not work for you
# If you have a higher version than 3.4.2 use the main as it is more up to date and this will not work for you

# This version may be slightly buggy with certain things but, if you don't want those bugs, migrate to an earlier version of Python
# The bugs shouldn't be too unbearable though, only minor

token = 'user account token goes here' 

description = '''CupOfJava is a selfbot created by Nyte for automatic moderation and other miscellaneous things'''
bot = commands.Bot(command_prefix='UsernameHere(', description=description, self_bot=True) # Change "UsernameHere(" to say your username followed by an opening parenthesis


@bot.event
@asyncio.coroutine
def on_ready():
    yield from bot.change_presence(game=discord.Game(name='a funny joke or something you want to appear as your playing status'), status=discord.Status.dnd) #Change the string in name=''
    print('CupOfJava - Selfbot version of SmartBrew')
    print('----------------------------------------')
    print('Legacy version - updates will not arrive')
    print('to this version as fast as they will with')
    print('the main due to it being a rare case that')
    print('people are using 3.4.2 or below and that')
    print('it is harder to do things with legacy')
    print('discord.py but I will try my best')
    print('----------------------------------------')
    print('Be sure to keep me updated by going to my')
    print('GitHub repo! There might be an important')
    print('update / bug fix there for you')
    print('----------------------------------------')
    
            
@bot.command(pass_context=True, name='info)')
@asyncio.coroutine
def info(ctx):
    """Just an info command"""
    print('{} | Info ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    yield from bot.say("```md\n[ Command executed ][ Info ]\n< CupOfJava is a selfbot created by Nyte for automatic moderation and other miscellaneous things >\n[ Instance owner ][ {} ]\n[ GitHub link ][ https://github.com/Nytelife26/Discord-Bots ]```".format(bot.user))
    
@bot.command(pass_context=True, name='ping)')
@asyncio.coroutine
def ping(ctx):
    """Does what it says on the tin."""
    print('{} | Ping ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    ping = yield from bot.say("```md\n[ Command executed ][ Ping ]\n< Ping in progress >\n```")
    time = (ping.timestamp - ctx.message.timestamp).total_seconds() * 1000
    yield from bot.edit_message(ping, "```md\n[ Command executed ][ Ping ]\n< Time taken to recieve / process command in milliseconds is {} ms >\n```".format(round(time)))

@bot.command(pass_context=True, name='logout)')
@asyncio.coroutine
def logout(ctx):
    """Gracefully exits CupOfJava - USE THIS INSTEAD OF CONSOLE WHEN POSSIBLE"""
    print('{} | Logout ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    yield from bot.say("```md\n[ Command executed ][ Logout ]\n< LOGGING OUT >\n```")
    yield from bot.logout()

@bot.command(pass_context=True, name="embed)")
@asyncio.coroutine
def embed(ctx, *, content : str=""):
    """Embeds the chosen message"""
    print('{} | Embed ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    if content == "":
        yield from bot.say("```md\n[ Command failed to execute ][ ArgumentError ]\n< Required argument was not defined >\n```")
    else:
        try:
            data = discord.Embed(description="CupOfJava - SELFBOT - Embed", colour=discord.Colour.purple())
            data.add_field(name=message.author.display_name + "#" + message.author.discriminator + " says", value=str(content))
            yield from bot.delete_message(message)
            yield from bot.say(embed=data)
        except:
            yield from bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the embed links permission so we cannot perform the task >\n```")
            
@bot.command(pass_context=True, name='yandere)')
@asyncio.coroutine
def yandere(ctx):
    """Random image from Yande.re | WARNING - DISPLAYS PORNOGRAPHIC CONTENT"""
    print('{} | Yandere ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    try:
        query = ("https://yande.re/post/random")
        page = yield from aiohttp.get(query)
        page = yield from page.text()
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.find(id="highres").get("href")
        yield from bot.edit_message(message, "```md\n[ Command executed ][ Yandere ]\n< Pulling random image from yande.re >\n```\n" + image)
    except Exception as e:
        yield from bot.edit_message("```md\n[ Command failed to execute ][ Non-bot error]\n< {} >".format(e))
        
@bot.command(name='restart)', pass_context=True)
@asyncio.coroutine
def restart(ctx):
    """Restarts CupOfJava"""
    print('{} | Restart ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    message = ctx.message
    yield from bot.edit_message(message, "```md\n[ Command executed ][ Restart ]\n< RESTARTING >\n```")
    os.execlp('python', 'python', '"CupOfJava - Legacy Version.py"')
    yield from bot.logout()
    
@bot.command(name='discrim)', pass_context=True)
@asyncio.coroutine
def discrim(ctx, discrim : str = None):
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
    yield from bot.edit_message(message, "```md\n[ Command executed ][ Discriminator ]\n< Finding users with discriminator {} >\n```".format(str(discrim)))
    yield from bot.edit_message(message, message.content + "\n" + '```md\n[ Users found ][ {} ]\n< Listing users found >'.format(str(discrim)) + '\n#' + '\n#'.join(names) + '```')

# Unfortunately, the purge command will not work in the legacy version. If you wish to help me fix this, DM Nyte#7883 and we can get started    
#@bot.command(name='purge)', pass_context=True)
#@asyncio.coroutine
#def purge(ctx, amount : int=20):
#    """Cleans a channel with a definable limit
#    By defaultthe amount is set to 20"""
#    print('{} | Purge ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
#    invoking = ctx.message
#    if amount <= 1: # if you truly are this lazy, then this limitation can be removed
#        msg = yield from bot.say("```md\n[ Command failed to execute ][ layZ Error ]\n< Don't be so lazy! The defined amount of messages was either one or below, and I mean come on, you can delete one message on your own. It's easy! Just so we don't add to the hassle, we'll delete this for you in about a minute >\n```")
#        yield from asyncio.sleep(60)
#        yield from bot.delete_message(msg)
#    else:
#        message = yield from bot.say("```md\n[ Command executed ][ Purge ]\n < Kick back and have a CupOfJava, while CupOfJava [this selfbot] purges the channel! >\n```")
#        yield from bot.delete_message(invoking)
#        fails = 0
#        for x in bot.logs_from(ctx.message.channel, before=ctx.message.timestamp, limit=amount):
#            try:
#                yield from bot.delete_message(x)
#            except:
#                fails += 1
#        yield from asyncio.sleep(2)
#        yield from bot.edit_message(message, "```md\n[ Command finished ][ Purge ]\n< Purge finished with {} failed attempts >\n```".format(str(fails)))
        
                
@bot.command(name='silence)', pass_context=True)
@asyncio.coroutine
def silence(ctx, user : discord.Member):
    """Mutes a given user"""
    print('{} | Silence ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    server = ctx.message.server
    message = ctx.message
    try:
        for r in server.roles:
            yield from bot.remove_roles(user, r)
        role = discord.utils.get(server.roles, name='Muted')
        yield from asyncio.sleep(1)
        yield from bot.add_roles(user, role)
        yield from bot.edit_message(message, "```md\n[ Command executed ][ Silence ]\n< {}\{}#{} was muted successfully >\n```".format(str(user.id), str(user.display_name), str(user.discriminator)))
    except:
        yield from bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the manage roles permission or the Muted role does not exist so we cannot perform this task >\n```")
        return
        
    
@bot.command(name='uncensor)', pass_context=True)
@asyncio.coroutine
def uncensor(ctx, user : discord.Member):
    """Unmutes a given user"""
    print('{} | Uncensor ran in {}'.format(str(ctx.message.timestamp), ctx.message.server))
    server = ctx.message.server
    message = ctx.message
    try:
        memberrole = discord.utils.get(server.roles, name='Members')
        muterole = discord.utils.get(server.roles, name='Muted')
        yield from bot.remove_roles(user, muterole)
        yield from bot.add_roles(user, role)
        yield from bot.edit_message(message, "```md\n[ Command executed ][ Uncensor ]\n< {}\{}#{} was unmuted successfully >".format(str(user.id), str(user.display_name), str(user.discriminator)))
    except:
        yield from bot.edit_message(message, "```md\n[ Command failed to execute ][ PermissionsError ]\n< We do not have the manage roles permission or the Muted role does not exist so we cannot perform this task >\n```")
        return
        
@bot.group(pass_context=True)
@asyncio.coroutine
def google(ctx):
        """Google search functions."""
        prefix = bot.command_prefix
        message = ctx.message
        if ctx.invoked_subcommand is None:
            yield from bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< No subcommand was passed on a command group >\n[ Retrieving list ][ Subcommands ]\n# images\n# maps\n# search\n[ Subcommands ][ Examples ]\n# {}google images) QUERY\n# {}google maps) QUERY\n# {}google search) QUERY\n ```".format(prefix, prefix, prefix))

@google.command(pass_context=True, name='images)')
@asyncio.coroutine
def images(ctx, *, query):
        message = ctx.message
        if query == "":
            yield from bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/search?tbm=isch&q="
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            yield from bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Imagae search mode\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))

@google.command(pass_context=True, name='maps)')
@asyncio.coroutine
def maps(ctx, *, query):
        message = ctx.message
        if query == "":
            yield from self.bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/maps/search/"
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            yield from bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Maps search mode\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))

@google.command(pass_context=True, name='search)')
@asyncio.coroutine
def search(ctx, *, query):
        message = ctx.message
        if query == "":
            yield from self.bot.edit_message(message, "```md\n[ Command failed to execute ][ ArgumentError ]\n< If you didn't know, to search Google you need to actually search for something >\n#Please define a valid query\n```")
        else:
            url = "https://www.google.com/search?q="
            encode = urllib.parse.quote_plus(query, encoding='utf-8', errors='replace')
            yield from bot.edit_message(message, "```md\n[ Command executed ][ Google ]\n# Generic search mode\n\n# Returning results..\n< {}{} >\n```\n{}{}".format(url, encode, url, encode))
                        
bot.run(token, bot=False)
