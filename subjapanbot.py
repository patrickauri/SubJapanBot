import discord
import gettoken

token = gettoken.getToken()

client = discord.Client()
errorMsg = 'En feil har oppstått. Kontakt administrator! エラーが発生しまいました！管理人を連絡してください！'


@client.event
async def on_ready():
    print('SubJapanBot running! as {0.user}'.format(client))


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
        # JAPANSK
        if message.content.startswith('.j1'):
            role_name = "Japansk Nybegynner - 日本語初心者"
        if message.content.startswith('.j2'):
            role_name = "Japansk Mellomnivå - 日本語中級者"
        if message.content.startswith('.j3'):
            role_name = "Japansk Flytende - 日本語流暢"
        if message.content.startswith('.j4'):
            role_name = "Japansk Morsmål - 日本語話者"
        # ENGELSK
        if message.content.startswith('.e1'):
            role_name = "Engelsk Nybegynner - 英語初心者"
        if message.content.startswith('.e2'):
            role_name = "Engelsk Mellomnivå - 英語中級者"
        if message.content.startswith('.e3'):
            role_name = "Engelsk Flytende - 英語流暢"
        if message.content.startswith('.e4'):
            role_name = "Japansk Morsmål - 日本語話者"
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
                norsk = ".n1 -> Norsk Nybegynner - ノルウェー語初心者\n.n2 -> Norsk Mellomnivå - ノルウェー語中級者\n.n3 -> Norsk Flytende - ノルウェー語流暢\n.n4 -> Norsk Morsmål - ノルウェー語話者"
                japansk = ".j1 -> Japansk Nybegynner - 日本語初心者\n.j2 -> Japansk Mellomnivå - 日本語中級者\n.j3 -> Japansk Flytende - 日本語流暢\n.j4 -> Japansk Morsmål - 日本語話者"
                await message.channel.send(f"** {title} ** \n *{subtitle1}* ```{norsk}``` *{subtitle2}* ```{japansk}```")
            else:
                await message.channel.send('Skriv .tasukete for hjelp. ヘルプを表示するには .tasukete')


client.run(token)
