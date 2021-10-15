import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '@Da3s Syoy' in message.clean_content :
        await message.channel.send(f'<@{message.author.id}>أش عندك تمنشن؟')

    
client.run('ODg4ODI0OTc4MDQ3MzczMzUy.YUYUxA.NJpaPrdlOdRqRLV6MAQ7Ri6LSEQ')
