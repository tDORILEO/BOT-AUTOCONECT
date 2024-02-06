import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Habilita a intenção de rastrear membros

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

    # Substitua 'ID_DO_SEU_CANAL' pelo ID do canal "ip-servidor"
    canal_desejado_id = 1175100841091399870

    canal_desejado = bot.get_channel(canal_desejado_id)
    if canal_desejado:
        embed_painel = discord.Embed(
            color=0x2f3136,
            title='Sistema de AutoConnect',
            description='**STATUS:**\n🟢Online\n**IP :**\n**FECHE O FIVEM ANTES DE CLICAR NO BOTÃO**'
        )
        embed_painel.set_thumbnail(url=bot.user.display_avatar.url)

        iniciar = discord.ui.Button(
            style=discord.ButtonStyle.link,
            label='🔌 Conectar-se',
            url=''
        )

        view = discord.ui.View()
        view.add_item(iniciar)

        message = await canal_desejado.send(embed=embed_painel, view=view)
    else:
        print("Canal desejado não encontrado.")

# Adicione o seu token do bot aqui
bot.run('')
