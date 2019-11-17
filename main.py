# hiro.py 
import discord

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_ready():
    print('Bot logado como: {0.user}'.format(client))

@client.event
async def on_message(message):
    print('-----------------')
    print('User:')
    print(message.author)
    print('Content:')
    print(message.content)


client.run(token)