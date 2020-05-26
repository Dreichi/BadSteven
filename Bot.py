import discord
import random
import json
import sqlite3
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
    print (f"{user} : {msg}")
    await client.process_commands(message)



@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commandes disponibles:",description="Liste des commandes disponibles", color=0x008FFF)
    embed.add_field(name="!help", value="Affiche ce menu", inline=False)
    embed.add_field(name="!love",value="Envoie de l'amour <3", inline=False)
    embed.add_field(name="!avatar <utilisateur>",value="Permet de voir l'avatar de quelqu'un", inline=False)
    embed.add_field(name="!clear <nombre>",value="Supprime le nombre de message spécifié", inline=False)
    embed.add_field(name="!rp <personnage> <rp>",value="Permet de RP sous un pseudo", inline=False)
    embed.add_field(name="!inv <personnage> <objet>",value="Permet d'ajouter un objet à son inventaire (EN CONSTRUCTION)", inline=False)
    embed.add_field(name="!create",value="Permet de créer un personnage (EN CONSTRUCTION)", inline=False)
    await ctx.channel.send(embed=embed)


@client.command()
async def love(ctx):
    await ctx.send("Plein d'amour pour vous!")


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
    embed = discord.Embed(title="Boop !", description=f"**{author}** boop **{member}**!", color=0x176cd5)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/676867450880655360/700021697751023616/1578885267_af30659e164e085c745814bf1174cafb.gif")
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
