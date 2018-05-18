import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(msg):
        if msg.author == client.user :
                return
        else:
                ch = client.get_channel('444698990756495362')
                m = msg.content
                c = msg.channel
                f = msg.author.nick+' said :'+m
                if c.name == 'general':
                        await client.send_message(ch, f)
client.run('NDQyODQzNzgyNTk4MDk4OTU0.DdeVPg.kxsNtMsc5SQgw7gCBjJiGbihOQk')