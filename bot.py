from twitchio.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()  # Ativa as variáveis de ambiente.


class Bot(commands.Bot):
    def __init__(self):
        """
        Carregamento do token de acesso e parametrização do BOT
        """
        token = getenv("CLIENTE_OAUTH")  # leitura do token de acesso
        super().__init__(token=token, prefix="!", initial_channels=["lfeplay"])
        """
        Neste caso o bot vai responder aos comandos iniciados com !
        No caso da twitch canal_da_twitch
        mas initial_channels pode ser uma lista de canais,
        por exemplo initial_channels=["lfeplay", "seu_canal"]
        e assim por diante
        """

    async def event_ready(self):
        """
        Evento quando o bot é carregado
        exbibe as informações na tela
        """
        print("Login como | Nome_da_conta")
        print("User id é | Id_da_conta")

    async def event_message(self, message):
        """
        Evento ao digitar uma mensagem qualquer no chat
        """
        # Faz o bot ignorar as próprias mensagens para ele não gerar comandos dele mesmo
        if message.echo:
            return

        # Exibe as mensagens do chat no terminal
        print(message.content)

        # Faz o bot lidar com as mensagens que não são dele mesmo,
        # respondendo caso haja a combinação prefixo + comando
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """
        Evento quando alguém digita !hello no canal da twitch
        """
        await ctx.send(
            f"Olá {ctx.author.name}!"
        )  # responde Olá <pessoa_que_enviou_a_mensagem>


bot = Bot()
bot.run()  # Faz o Bot rodar efetivamente
