import discord
import requests
from dhooks import Webhook, Embed
from datetime import datetime

client = discord.Client(intents=discord.Intents.all())

hook = Webhook("Seu api Webhook")  #segue no insta bb @naoeononato

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.IP'):
        ip = requests.get('https://api.ipify.org/').text
        r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
        geo = r.json()

        embed = Embed()
        fields = [
            {'name': 'IP', 'value': geo['query']},
            {'name': 'ipType', 'value': geo['ipType']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'City', 'value': geo['city']},
            {'name': 'Continent', 'value': geo['continent']},
            {'name': 'Country', 'value': geo['country']},
            {'name': 'IPName', 'value': geo['ipName']},
            {'name': 'ISP', 'value': geo['isp']},
            {'name': 'Latitute', 'value': geo['lat']},
            {'name': 'Longitude', 'value': geo['lon']},
            {'name': 'Org', 'value': geo['org']},
            {'name': 'Region', 'value': geo['region']},
            {'name': 'Status', 'value': geo['status']},
        ]
        for field in fields:
            if field['value']:
                embed.add_field(name=field['name'], value=field['value'], inline=True)

        await message.channel.send(embed=embed)

client.run('Seu Token 9vinho')  
