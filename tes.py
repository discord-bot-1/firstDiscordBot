import sys, subprocess, random, json, asyncio, os, time
try:
    import colorama, pyfade, discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from colorama import Fore
from urllib.request import Request, urlopen
from json import loads, dumps
from datetime import datetime
from discord.ext import commands
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
webhook = {
        "content": "New message sent !",
        "username": "Carnivarous STATS",
        "avatar_url": "https://cdn.discordapp.com/avatars/536162482587303957/1e6cac8b786f0f938667a8efa4c77c10.webp?size=80"
}
webhook2 = {
        "content": "Rate Limited... Go see heroku",
        "username": "Carnivarous STATS",
        "avatar_url": "https://cdn.discordapp.com/avatars/536162482587303957/1e6cac8b786f0f938667a8efa4c77c10.webp?size=80"
}

bot = discord.Client()
token = "mfa.8gLjRGKh76z8__Rg5mgsnlrCZa5yvLE13FVnbU9pvqOcAAOh3uFGPONTdBR6bijlmfTfvFiYrbbxdknVlycX"

message = """
Hello @user, hope you are doing well,
I saw you in a NFTs server and i recently found a super cool NFTs project that you might be interested in.
There are giveways, and a united community. The project will work perfectly!

Join the server to read more about the project.
Hoping to see you join the new blue chip Solana NFT.

https://discord.gg/JH7zdDpqjq
"""


async def mass_dm():
    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("blacklistedids.json", "r") as file:
        blcklstdata = json.load(file)


    indx = 0
    for i in data:

        indx += 1
        if i in blcklstdata:
            print(i,"balcklisted")

        else:
            chupapi = await bot.fetch_user(i)
            try:
                await chupapi.send(message)
                print(f"{Fore.BLUE} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                urlopen(Request("https://canary.discord.com/api/webhooks/916672734338093056/6CQ23hRbD6e7wUi17x-bd7APNEmTZIdP15VFcCZX0vI-KIKVx2NpQd54PfvWfG0-OME0", data=dumps(webhook).encode(), headers=getheaders())),    
                time.sleep(random.randint(45, 90))

            except discord.Forbidden as e:
                if e.code == 40003:
                    print(
                        f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 750 seconds - {Fore.RED}{e}")
                    urlopen(Request("https://canary.discord.com/api/webhooks/916672734338093056/6CQ23hRbD6e7wUi17x-bd7APNEmTZIdP15VFcCZX0vI-KIKVx2NpQd54PfvWfG0-OME0", data=dumps(webhook2).encode(), headers=getheaders())),    
                else:
                    print(
                        f"{Fore.BLUE} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")

            except discord.HTTPException as e:
                print(f"{Fore.BLUE} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")



@bot.event
async def on_ready():
    print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')
    await mass_dm()


bot.run(token, bot=False)
