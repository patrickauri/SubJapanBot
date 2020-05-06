import discord
import gettoken
import os

#token = gettoken.getToken()
token = os.environ['TOKEN']

client = discord.Client()
errorMsg = 'En feil har oppstått. Kontakt administrator! エラーが発生しまいました！管理人を連絡してください！'


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
    if message.content.startswith('.'):
        role_name = None
        # NORSK
        if message.content.startswith('.n1'):
            role_name = "Norsk Nybegynner - ノルウェー語初心者"
        if message.content.startswith('.n2'):
            role_name = "Norsk Mellomnivå - ノルウェー語中級者"
        if message.content.startswith('.n3'):
            role_name = "Norsk Flytende - ノルウェー語流暢"
        if message.content.startswith('.n4'):
            role_name = "Norsk Morsmål - ノルウェー語話者"
        if message.content.startswith('.nh'):
            role_name = "Norsk-Hjelp ノルウェー語助手"
        # JAPANSK
        if message.content.startswith('.j1'):
            role_name = "Japansk Nybegynner - 日本語初心者"
        if message.content.startswith('.j2'):
            role_name = "Japansk Mellomnivå - 日本語中級者"
        if message.content.startswith('.j3'):
            role_name = "Japansk Flytende - 日本語流暢"
        if message.content.startswith('.j4'):
            role_name = "Japansk Morsmål - 日本語話者"
        if message.content.startswith('.jh'):
            role_name = "Japansk-Hjelp 日本語助手"
        # ENGELSK
        if message.content.startswith('.e1'):
            role_name = "Engelsk Nybegynner - 英語初心者"
        if message.content.startswith('.e2'):
            role_name = "Engelsk Mellomnivå - 英語中級者"
        if message.content.startswith('.e3'):
            role_name = "Engelsk Flytende - 英語流暢"
        if message.content.startswith('.e4'):
            role_name = "Engelsk Morsmål - 英語話者"
        if message.content.startswith('.eh'):
            role_name = "Engelsk-Hjelp 英語助手"
        if role_name is not None:
            role = discord.utils.get(
                message.guild.roles, name=role_name)
            if role in message.author.roles:
                try:
                    print(f"Removing role {role} from {message.author}")
                    await message.author.remove_roles(role)
                    await message.channel.send(f"Fjernet rollen: ( {role} )というロールを消しました。")
                except:
                    await message.channel.send(errorMsg)
            else:
                try:
                    print(
                        f'Adding role {role} to {message.author}')
                    await message.author.add_roles(role)
                    await message.channel.send(f"Du har fått rollen ( {role} )というロールを付けました。")
                except:
                    await message.channel.send(errorMsg)
        else:
            if message.content.startswith('.tasukete'):
                title = "Skriv . etterfulgt av en rolle for å få rollen. 欲しいロールを．の後に付けたらロールを貰えます"
                subtitle1 = "Norsk ノルウェー語"
                subtitle2 = "Japansk 日本語"
                subtitle3 = "Engelsk 英語"
                norsk = ".n1 -> Norsk Nybegynner - ノルウェー語初心者\n.n2 -> Norsk Mellomnivå - ノルウェー語中級者\n.n3 -> Norsk Flytende - ノルウェー語流暢\n.n4 -> Norsk Morsmål - ノルウェー語話者"
                japansk = ".j1 -> Japansk Nybegynner - 日本語初心者\n.j2 -> Japansk Mellomnivå - 日本語中級者\n.j3 -> Japansk Flytende - 日本語流暢\n.j4 -> Japansk Morsmål - 日本語話者"
                engelsk = ".e1 -> Engelsk Nybegynner - 英語初心者\n.e2 -> Engelsk Mellomnivå - 英語中級者\n.e3 -> Engelsk Flytende - 英語流暢\n.e4 -> Engelsk Morsmål - 英語話者"
                await message.channel.send(f"** {title} ** \n *{subtitle1}* ```{norsk}``` *{subtitle2}* ```{japansk}``` *{subtitle3}* ```{engelsk}```")
            else:
                await message.channel.send('Skriv .tasukete for hjelp. ヘルプを表示するには .tasukete')


client.run(token)
