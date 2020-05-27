import discord
import random
import json
import sqlite3
import datetime
import os
from datetime import timezone, tzinfo, timedelta
from discord.ext import commands

client = commands.Bot(command_prefix="!s ")
client.remove_command("help")

CHANNEL = "671497752328273939"

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('fansub BNA'))
    print("Connecté en tant que")
    print(client.user.name)
    print("--------")


@client.event
async def on_member_join(member):
    channel = client.get_channel(CHANNEL)
    await channel.send(f"Bienvenue sur le serveur {member.mention}!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(CHANNEL)
    await channel.send(f"Au revoir {member.mention} ...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = message.author.name
    msg = message.content
    channel = message.channel
    guild = message.guild
    time = datetime.datetime.now()
    print(f"{time} : {user} : {msg}")
    if guild:
        path = f"chatlogs/{guild}"
        file_path = path + f"/{channel.name}.txt"
        if not os.path.exists(path):
            os.makedirs(path)
        with open(file_path, 'a+', encoding="utf-8") as f:
            print(f"{time} : {user} : {msg}".format(message), file=f)
    await client.process_commands(message)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commandes disponibles:",description="Liste des commandes disponibles", color=0x008FFF)
    embed.add_field(name="!s help", value="Affiche ce menu", inline=False)
    embed.add_field(name="!s love",value="Envoie de l'amour <3", inline=False)
    embed.add_field(name="!s avatar <utilisateur>",value="Permet de voir l'avatar de quelqu'un", inline=False)
    embed.add_field(name="!s clear <nombre>",value="Supprime le nombre de message spécifié", inline=False)
    embed.add_field(name="!s rp <personnage> <rp>",value="Permet de RP sous un pseudo", inline=False)
    embed.add_field(name="!s inv <personnage> <objet>",value="Permet d'ajouter un objet à son inventaire (EN CONSTRUCTION)", inline=False)
    embed.add_field(name="!s create",value="Permet de créer un personnage (EN CONSTRUCTION)", inline=False)
    embed.add_field(name="!s kick", value="Permet de kick", inline=False)
    embed.add_field(name="!s ban", value="Permet de ban", inline=False)
    embed.add_field(name="!s mute", value="Permet de mute", inline=False)
    await ctx.channel.send(embed=embed)


@client.command()
async def love(ctx):
    embed = discord.Embed(title="Plein d'amour pour vous !", color=0x176cd5)
    embed.set_image(url='https://gifimage.net/wp-content/uploads/2017/06/furry-gif-13-1.gif')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} a été kick du serveur.')


@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, self, member: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f'{member} a été mute sûrement pour une bonne raison =w=')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, self, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} a été ban du serveur.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    author = ctx.message.author
    if amount > 0:
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{author.mention} a supprimé {amount} message(s)!")
    else:
        await ctx.message.delete()
        await ctx.send(f"Merci de spécifier un nombre valide, {author.name}")


@client.command()
async def avatar(ctx, member: discord.Member, pass_context=True):
    embed = discord.Embed(colour=member.color,timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar de {member}")
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def create(ctx, word1):
    with open("char.json", "r") as json_file:
     char = json.load(json_file)
     if "nom" in char:
      char["nom"] += word1
     else:
      char["nom"] = word1
     json_file.close()

    with open("char.json", "w") as json_file:
        json.dump(char, json_file)
    

@client.command(pass_context=True)
async def rp(ctx, word1, *, words, amount=1):
    await ctx.message.delete()
    await ctx.send("**" + word1 + ": " + "** " + words)

@client.command()
async def inv(ctx, word1, words):
    desk = "C:/Users/Damien/Desktop/RPbot/"
    file = open(desk + "inv.txt", "r+")
    print (list(file))
    if word1 in file:
        file.writelines(f' {words}')
        await ctx.send("L'objet: " + words + " a été rajouté à votre inventaire")
        file.close()
    else:
         await ctx.send("Le personnage n'existe pas")
    file.close()


@client.command()
async def boop(ctx, member):
    author = ctx.message.author.name
    boops = [
        'https://cdn.discordapp.com/attachments/676867450880655360/700021697751023616/1578885267_af30659e164e085c745814bf1174cafb.gif',
        'https://cdn.discordapp.com/attachments/469849157784567809/569994696945041418/1549948814.rukaisho_yasha_and_zayne_hugs_gif.gif',
        'https://media.tenor.com/images/f6f87118730878c578e0f188da5270fc/tenor.gif',
        'https://pa1.narvii.com/6394/cd574351837c6181222057412f91f9d1c1bfe3db_hq.gif',
        'https://i.pinimg.com/originals/f7/1a/5d/f71a5d5f59441a724e820dc7f46ea94e.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715137595352416326/636IDPR.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715137954837954681/inconnu.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715138082441003029/inconnu.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715138093233078333/inconnu.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715138449228824606/15905726850882738996636693413586.gif',
    ]
    boop = random.choice(boops)
    embed = discord.Embed(title="Boop !", description=f"**{author}** boop **{member}**!", color=0x176cd5)
    embed.set_image(url=boop)
    await ctx.send(embed=embed)


@client.command()
async def nom(ctx, member):
    author = ctx.message.author.name
    noms = [
        'https://cdn.discordapp.com/attachments/714608745065480274/715159629012795443/tenor_1.gif',
    ]
    nom = random.choice(noms)
    embed = discord.Embed(
        title="Nom !", description=f"**{author}** nom **{member}**!", color=0x176cd5)
    embed.set_image(url=nom)
    await ctx.send(embed=embed)


@client.command()
async def mordille(ctx, member):
    author = ctx.message.author.name
    mords = [
        'https://cdn.discordapp.com/attachments/714608745065480274/715165486475903026/chien-qui-mordille-l-oreille-du-chat.gif',
        'https://cdn.discordapp.com/attachments/714608745065480274/715165486954053700/ca332c5a7e37bdd95c045ac1fb1ddc8c.gif'
    ]
    mord = random.choice(mords)
    embed = discord.Embed(title="Attention !", description=f"**{author}** mordille **{member}**!", color=0x176cd5)
    embed.set_image(url=mord)
    await ctx.send(embed=embed)


@client.command()
async def hug(ctx, member):
    author = ctx.message.author.name
    hugs = [
        'https://cdn.discordapp.com/attachments/714608745065480274/715166152493498368/tenor_2.gif',
        'https://cdn.discordapp.com/attachments/714608745065480274/715166153697132584/5553845_170x100.gif',
        'https://cdn.discordapp.com/attachments/714608745065480274/715166153147940905/tumblr_af0732ecfd70d02a6ed3c0740ab767a1_ad57ae67_1280.webp',
        'https://cdn.discordapp.com/attachments/706968022279127110/715167806219485254/tenor.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715168637765550150/84a06e18c6413b092b754b9fbec6801a.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715168961087406100/6812fb166abe2aa58b3a1875174538e437c22f6980752f13d33a5150e95d190a.gif',
        ''
    ]
    hug = random.choice(hugs)
    embed = discord.Embed(title="Câlin !", description=f"**{author}** câline **{member}**!", color=0x176cd5)
    embed.set_image(url=hug)
    await ctx.send(embed=embed)


@client.command()
async def gratouille(ctx, member):
    author = ctx.message.author.name
    grattes = [
        'https://cdn.discordapp.com/attachments/714608745065480274/715160055791616050/DisfiguredWelllitBongo-size_restricted.gif',
    ]
    gratte = random.choice(grattes)
    embed = discord.Embed(title="Gratouille !", description=f"**{author}** grattouille **{member}**!", color=0x176cd5)
    embed.set_image(url=gratte)
    await ctx.send(embed=embed)


@client.command()
async def kiss(ctx, member):
    author = ctx.message.author.name
    kisses = [
        'https://d.facdn.net/art/kusuguttai/1550707158/1550707158.kusuguttai_kissandnibble.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715139472169107516/15905729298983769141377727103849.gif',
        'https://thumbs.gfycat.com/AcrobaticUnconsciousHyrax-small.gif',
        'https://media.discordapp.net/attachments/706968022279127110/715139786494705684/15905730047521705077081053990760.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715140059065614366/15905730710611323851964894586756.gif',
        'https://memestatic.fjcdn.com/gifs/Cute+kiss+smalli+have+a+soft+spot+for+that+sweden_4d9e32_6366724.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715140576798048327/15905731898017745238231433871181.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715141088591216640/f1eea14bc88ca4a30332c9140c64e1a8.gif',
        'https://cdn.discordapp.com/attachments/706968022279127110/715141822565056522/94e59d8acaa3539b9635341f11fd0f58.gif',
    ]
    kiss = random.choice(kisses)
    embed = discord.Embed(title="Kiss !", description=f"**{author}** a embrassé **{member}**! >w<", color=0x176cd5)
    embed.set_image(url=kiss)
    await ctx.send(embed=embed)


@client.command()
async def dice(ctx, number: int = 6):
    if ctx.author.id == 489159659475959809:
        throw = random.randint(1, number/2)
        await ctx.send(f"Dé: {number}\nLancer: {throw}")
    else:
        throw = random.randint(1, number)
        await ctx.send(f"Dé: {number}\nLancer: {throw}")

with open("conf.json") as json_file:
    conf = json.load(json_file)
    json_file.close()
client.run(conf["TOKEN"])
