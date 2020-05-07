import discord
import os
import sys
from bot_config import *

bot_channel = bot_channel_id
token = os.environ['TOKEN']

client = discord.Client()
errorMsg = 'En feil har oppstått. Kontakt administrator! エラーが発生しまいました！管理人に連絡してください！'

@client.event
async def on_ready():
    print('SubJapanBot running! as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channelid = 696733496592564294
    jikoshokai_id = 705063473364729926
    jikoshokai = client.get_channel(jikoshokai_id)
    channel = client.get_channel(channelid)
    mentionstr = member.mention
    msg = (f"A wild {mentionstr} has appeared! Gjerne introduser deg i {jikoshokai.mention} - 野生の{mentionstr}が現れた！是非 {jikoshokai.mention} で自己紹介してね")
    await channel.send(msg)

@client.event
async def on_message(message):
    content = message.content
    author = message.author
    guild = message.guild
    channel = message.channel
    if bot_channel == channel.id and author.id != client.user.id and content.startswith('.') and author.bot == False:
        if content == '.tasukete':
            await print_help(channel, guild)
        role = None
        for key in role_dict.keys():
            if role_dict[key].get(content, False):
               role = guild.get_role(role_dict[key][content]) 
               remove_key = key 
        if role:
            if role in author.roles:
                await remove_role(channel, author, role)
            else:
                if not remove_key == "Språkjelp 語学助手":
                    for role_code in role_dict[remove_key]:
                        await remove_role(channel, author, guild.get_role(role_dict[remove_key][role_code]), True)
                await set_role(channel, author, role)
        else:
            await channel.send('Skriv .tasukete for hjelp. ヘルプを表示するには .tasukete')
    
async def set_role(channel, author, role):
    try:
       print(f'Adding role {role} to {author}')
       await author.add_roles(role)
       await channel.send(f"Du har fått rollen ( {role} )というロールを付けました。")
    except:
        await channel.send(errorMsg)

async def remove_role(channel, author, role, silent=False):
    try:
        print(f"Removing role {role} from {author}")
        await author.remove_roles(role)
        if not silent:
            await channel.send(f"Fjernet rollen: ( {role} )というロールを消しました。")
    except:
        await channel.send(errorMsg)

async def print_help(channel, guild):
    s = "**Skriv . etterfulgt av en rolle for å få rollen. 欲しいロールを．の後に付けたらロールを貰えます** \n"
    for key in role_dict.keys():
        s += "*" + key + "* ```"
        for level in role_dict[key]:
            s += level + " -> " + guild.get_role(role_dict[key][level]).name + "\n"
        s += "```"
    await channel.send(s)
    

client.run(token)

