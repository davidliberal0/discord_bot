import os 
import discord

# For API Functions and Requests 
import random 
import requests 
import json 

from discord.ext import commands 


# Linking the .env file 
from dotenv import load_dotenv
load_dotenv()

# Obtaining the token from the .env
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix ='!', intents=intents)


# ---------------------- Display to Terminal -----------------------------------------------------

# Displays to Terminal - Connection Verification (Guild Name and Members)
@client.event
async def on_ready():
     for guild in client.guilds:
          print(
        f'{client.user} has connected to Discord!\n'
        f'Guild: {guild.name} (id: {guild.id})'
        ) 
     members = '\n - '.join([member.name for member in guild.members])
     print(f'Guild Members:\n - {members}')


# -------------------------- Welcome Message ------------------------------------------------------

# Sends a direct message to new members of the server
@client.event
async def on_member_join(member): 
    await member.create_dm()
    await member.send(
        f'Hello {member.name}, welcome to my Discord server!'
    )

# ------------------------ Coding Resource Cammands ----------------------

@client.command(aliases=["cpp"])
async def link_cpp(ctx):
    cpp_resource = "Best CPP Tutorial: https://www.youtube.com/playlist?list=PLAE85DE8440AA6B83"
    response = cpp_resource 
    await ctx.send(response)

@client.command(aliases=["python"])
async def link_python(ctx):
    python_resource = "Python Fundamentals: https://www.youtube.com/watch?v=_uQrJ0TkZlc \nCS Python: https://www.youtube.com/watch?v=8DvywoWv6fI"
    response = python_resource
    await ctx.send(response)

@client.command(aliases=["webdev"])
async def link_webdev(ctx):
    webdev_resource = "Front-End: https://www.youtube.com/watch?v=mU6anWqZJcc \nBack-End: https://www.youtube.com/watch?v=OK_JCtrrv-c"
    response = webdev_resource
    await ctx.send(response)

# ---------------------------- Dynamic Stuff with APIs -------------------------------------------

thumbsup = "👍"
thumbsdown = "👎"



# Obtains the quote from the Zenquoes API
def get_quote(): 
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text) # converts the data into text - the data recieved is a joke 
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

# Obtains the joke from JokeAPI
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    json_data = json.loads(response.text)
    joke = json_data['setup'] + ' ⇒ ' + "||" + json_data['punchline'] + "||"
    return(joke)

def get_meme(): 
    response = requests.get("https://memes.blademaker.tv/api?lang=en")
    json_data = json.loads(response.text)
    meme = json_data['image']
    return(meme)


# Command for jokes (calls the function get_joke() )
@client.command(aliases=["laugh"])
async def laugh_joke(ctx):
    response = get_joke()
    await ctx.send(response)

# Command for quotes (calls the function get_quote() )
@client.command(aliases=["inspire"])
async def inspire_me(ctx):
    response = get_quote()
    await ctx.send(response)

# Commmand for memes 
@client.command(aliases=["meme"])
async def meme_me(ctx):
    response = get_meme()
    meme_r = await ctx.send(response)
    await meme_r.add_reaction(emoji=thumbsup)


# -------------------------------------------------------------------------------

# Command for clearing messages in the chat 
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

















client.run(TOKEN)