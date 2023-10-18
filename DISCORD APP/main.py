import discord
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

load_dotenv(dotenv_path)

my_secret = os.getenv('KEY')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'WUAAAAA, TODO ESTA BIENNN {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!github'):
    github_message = """
        **¡Holaaa!** :wave:
        Veo que buscas el GitHub de alguien :smiley:
        Aquí tienes los 3 más importantes:

        **Miguel Diaz (titooUvU)**
        [GitHub](https://github.com/titooUvU)

        **Kaleth Renteria (keileth)**
        [GitHub](https://github.com/keileth)
        """
    await message.channel.send(github_message)


client.run(my_secret)