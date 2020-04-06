import discord
# from discord.ext import commands

token = "Njk2NzcwMDM3OTQ3Njk1MTA0.Xotjxg.GbZmCe9KVeD8h4LZAUK2WgDeAYI"

# client = commands.Bot(command_prefix='.')
client = discord.Client()


@client.event
async def on_ready():
    print('SubJapanBot running! as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('.'):
        role_name = None
        if message.content.startswith('.n1'):
            role_name = "Norsk Nybegynner - ノルウェー語初心者"
        if message.content.startswith('.n2'):
            role_name = "Norsk Viderekommen - ノルウェー語中級者"
        if message.content.startswith('.n3'):
            role_name = "Norsk Flytende - ノルウェー語流暢"
        if message.content.startswith('.nn'):
            role_name = "Norsk Morsmål - ノルウェー語話者"
        if message.content.startswith('.j1'):
            role_name = "Japansk Nybegynner - 日本語初心者"
        if message.content.startswith('.j2'):
            role_name = "Japansk Viderekommen - 日本語中級者"
        if message.content.startswith('.j3'):
            role_name = "Japansk Flytende - 日本語流暢"
        if message.content.startswith('.jn'):
            role_name = "Japansk Morsmål - 日本語話者"
        if message.content.startswith('.test'):
            role_name = "Test"
        if role_name is not None:
            role = discord.utils.get(
                message.guild.roles, name=role_name)

            try:
                print(f'Adding role {role} ({role_name}) to {message.author}')
                await message.author.add_roles(role)
                await message.channel.send(f'Du har fått rollen ( {role} )というロールを付けました。')
            except:
                await message.channel.send(
                    'En feil har oppstått. Kontakt administrator! エラーが発生しまいました！管理人を連絡してください！')
        if message.content.startswith('.tasukete'):
            await message.channel.send('Hjelp')
    else:
        # client.send_message(message.channel, 'Denne rollen finnes ikke')
        await message.channel.send('Denne rollen finnes ikke! Skriv .tasukete for hjelp. このロールは存在していません。ヘルプを表示するには .tasukete')


client.run(token)
