# bot.py
import os
import random
import discord
import pyrcon
import json
import requests
import numpy as np
import string
import time


with open('config.json') as config_file:
    settings = json.load(config_file)

from discord.ext import commands
from pyrcon import RCON
from time import sleep

rcon = RCON(settings['rcon']['host'], settings['rcon']['password'], port=int(settings['rcon']['port']))
TOKEN = settings['discord']['token']

client = discord.Client()

bot = commands.Bot(command_prefix='=')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='revive')
@commands.has_role(settings['discord']['role'])
async def revive(ctx, arg):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    rcon.send_command('revivepy ' + arg, response=False)
            
@bot.command(name='giveaccountmoney')
@commands.has_role(settings['discord']['role'])
async def revive(ctx, arg1, arg2, arg3):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    rcon.send_command('giveaccountmoneypy ' + arg1 + ' ' + arg2 + ' ' + arg3, response=False)

@bot.command(name='giveitem')
@commands.has_role(settings['discord']['role'])
async def revive(ctx, arg1, arg2):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    rcon.send_command('giveitempy ' + arg1 + ' ' + arg2, response=False)

@bot.command(name='giveweapon')
@commands.has_role(settings['discord']['role'])
async def revive(ctx, arg1, arg2, arg3):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    rcon.send_command('giveweaponpy ' + arg1 + ' ' + arg2 + ' ' + arg3, response=False)
    
@bot.command(name='restart')
@commands.has_role(settings['discord']['role'])
async def restart(ctx, arg):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('restart ' + arg, response=True)
    await ctx.send(response)

@bot.command(name='start')
@commands.has_role(settings['discord']['role'])
async def start(ctx, arg):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('start ' + arg, response=True)
    await ctx.send(response)

@bot.command(name='stop')
@commands.has_role(settings['discord']['role'])
async def stop(ctx, arg):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('stop ' + arg, response=True)
    await ctx.send(response)

@bot.command(name='refresh')
@commands.has_role(settings['discord']['role'])
async def refresh(ctx):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('refresh', response=True)
    await ctx.send(response)

# NEW COMMANDS
@bot.command(name='setjob')
@commands.has_role(settings['discord']['role'])
async def setjob(ctx, arg1, arg2, arg3):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('setjobpy ' + arg1 + ' ' + arg2 + ' ' + arg3, response=True)
 

@bot.command(name='kick')
@commands.has_role(settings['discord']['role'])
async def kick(ctx, arg1, *arg2):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('clientkick ' + ' ' + arg1 + ' ' + " ".join(arg2[:]), response=True)
    await ctx.send('Command has been sent')



@bot.command(name='announce')
@commands.has_role(settings['discord']['role'])
async def announce(ctx, *args):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return

    response = rcon.send_command('say ' + " ".join(args[:]), response=True)
    await ctx.send('Command has been sent')

@bot.command(name='sendto')
@commands.has_role(settings['discord']['role'])
async def sendto(ctx, arg1):
    if ctx.channel.id != settings['discord']['cmd_channel']:
        return
    response = rcon.send_command('sendtopy ' + arg1, response=True)
 
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help for " + settings['general']['servername'] + " Admin Commands", description="All commands available:", color=discord.Color.blue())
    embed.set_thumbnail(url=settings['general']['logourl'])
    embed.set_footer(text = settings['general']['website'], icon_url = settings['general']['logourl'])
    embed.add_field(name="Status", value="Usage: status", inline=False)
    embed.add_field(name="Revive", value="Usage: revive [id]", inline=False)
    embed.add_field(name="Give Account Money", value="Usage: giveaccountmoney [id] [account] [amount]", inline=False)
    embed.add_field(name="Give Item", value="Usage: giveitem [id] [item] [amount]", inline=False)
    embed.add_field(name="Give Weapon", value="Usage: giveweapon [id] [weapon] [ammo]", inline=False)
    embed.add_field(name="Refresh Resources", value="Usage: refresh", inline=False)
    embed.add_field(name="Start Resource", value="Usage: start [resourcename]", inline=False)
    embed.add_field(name="Stop Resource", value="Usage: stop [resourcename]", inline=False)
    embed.add_field(name="Restart Resource", value="Usage: restart [resourcename]", inline=False)   
    embed.add_field(name="Set Job", value="Usage: setjob [id] [job] [grade]", inline=False)
    embed.add_field(name="Kick", value="Usage: kick [id] [reason]", inline=False)
    embed.add_field(name="Announce", value="Usage: announce [message]", inline=False)
    embed.add_field(name="Send To", value="Usage: sendto [id]", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def status(ctx):
    serverstatus = requests.get('http://' + settings['rcon']['host']+':'+settings['rcon']['port']+'/players.json', timeout=5)
    serverdata = serverstatus.json()
    players = []
    ids = []
    
    if serverstatus.status_code == 200:
        for x in range(len(serverdata)):
          players.append(serverdata[x]["name"])
          ids.append(serverdata[x]["id"])
          
        arr1 = np.array(players)
        arr2 = np.array(ids)
        idstring = np.stack((arr1, arr2), axis=1)        
        idsstring = str(idstring).replace("' '", " (**")
        idsstring = str(idsstring).replace("[[", "")
        idsstring = str(idsstring).replace("']", "**)")
        idsstring = str(idsstring).replace("['", "")
        idsstring = str(idsstring).replace("'", "")
        idsstring = str(idsstring).replace("]", "")
        
        embed=discord.Embed(title=settings['general']['servername'], description="All players currently online", color=discord.Color.blue())
        embed.set_thumbnail(url=settings['general']['logourl'])
        embed.set_footer(text = settings['general']['website'], icon_url = settings['general']['logourl'])
        embed.add_field(name="Players (" + str(len(players)) + "/" + str(settings['general']['maxclients']) + ")", value= str(idsstring), inline=True)
        await ctx.send(embed=embed)

bot.run(TOKEN)