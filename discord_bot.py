from datetime import datetime
import os
import discord
import mensa
import json


def main():

    with open('config.json', 'r') as f:
        config1 = json.load(f)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content == "!mensa":
            essensliste = mensa.mensa_grap_thisweek()
            embedVar = discord.Embed(title="Mensaspeiseplan 🥗🌮🥪", description="[Was gibt es denn heute leckeres?](https://www.studentenwerk-wuerzburg.de/bamberg/essen-trinken/speiseplaene/mensa-austrasse-bamberg.html)", color=0xffff)
            embedVar.add_field(name=essensliste[0] + "    🌑",value=essensliste[1] + "\n", inline=False)
            embedVar.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar.add_field(name=essensliste[2] + "     🌒", value=essensliste[3] + "\n", inline=False)
            embedVar.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar.add_field(name=essensliste[4] + "     🌓", value=essensliste[5] + "\n", inline=False)
            embedVar.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar.add_field(name=essensliste[6] + "     🌔", value=essensliste[7] + "\n", inline=False)
            embedVar.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar.add_field(name=essensliste[8] + "     🌖🎉", value=essensliste[9] + "\n", inline=False)
            embedVar.set_footer(text="Mensa Bot by Oreok", icon_url="https://avatars.githubusercontent.com/u/20826515?s=400&u=d1ccbf0cabd8e8e1e70d879e9f21a4d2c95406fc&v=4")
            embedVar.timestamp = datetime.now()
            await message.channel.send(embed=embedVar)

        elif message.content == "!mensa2":
            essensliste = mensa.mensa_grap_nextweek()
            embedVar2 = discord.Embed(title="Mensaspeiseplan 🥗🌮🥪", description="[Was gibt es denn heute leckeres?](https://www.studentenwerk-wuerzburg.de/bamberg/essen-trinken/speiseplaene/mensa-austrasse-bamberg.html)", color=0xffff)
            embedVar2.add_field(name=essensliste[0] + "    🌑",value=essensliste[1] + "\n", inline=False)
            embedVar2.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar2.add_field(name=essensliste[2] + "     🌒", value=essensliste[3] + "\n", inline=False)
            embedVar2.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar2.add_field(name=essensliste[4] + "     🌓", value=essensliste[5] + "\n", inline=False)
            embedVar2.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar2.add_field(name=essensliste[6] + "     🌔", value=essensliste[7] + "\n", inline=False)
            embedVar2.add_field(name="\u200B", value="\u200B" , inline=False)
            embedVar2.add_field(name=essensliste[8] + "     🌖🎉", value=essensliste[9] + "\n", inline=False)
            embedVar2.set_footer(text="Mensa Bot by Oreok", icon_url="https://avatars.githubusercontent.com/u/20826515?s=400&u=d1ccbf0cabd8e8e1e70d879e9f21a4d2c95406fc&v=4")
            embedVar2.timestamp = datetime.now()
            await message.channel.send(embed=embedVar2)
            
    client.run(config1["Discord_Bot_Token"])


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()  


        
        

    
        



