import discord
import os
from bardapi import Bard
from termcolor import colored
import datetime

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.isfile(dotenv_path):
    with open(dotenv_path) as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value
my_secret = os.getenv('KEY')

#chatbot
BARDKEY = os.getenv("BARDKEY")#recuerda tener un archivo lalmada .env en la carpeta raiz, con la variable y tu KEY de la API

os.environ["_BARD_API_KEY"] = BARDKEY

#DISCORD BOT CONFIG...
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print(f'WUAAAAA, TODO ESTA BIEEEN {client.user}')

tasks = []

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    if payload.channel_id == 1163145685407903827:
        emoji = payload.emoji.name
        message_id = payload.message_id
        user_id = payload.user_id
        user = await guild.fetch_member(user_id)

        # Obtiene el objeto Role que representa el rol que deseas agregar al usuario
        rol_obj = guild.get_role(1163182355708661900)

        await user.add_roles(rol_obj)

    

@client.event
async def on_message(message):
  global tasks
  ######CONSOLA Y BLOG DE NOTAS
  colores = ['blue', 'magenta', 'red', 'black']
  mensaje=message.content
  canal=message.channel.name
  
  fecha = datetime.datetime.now()
  fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')

  author = message.author
  roles = author.roles[-1]
  if roles.id == 1163180502681911316:
    linea=f'{colored(fecha_formateada, colores[3])}*/*{colored(canal, colores[2])}*/*{colored("ADMIN:", colores[1])}*/*{colored(mensaje, colores[3])}'
    lineatxt=f'{fecha_formateada} */* {canal} */* ADMIN */* {mensaje}'
  if roles.id == 1163182355708661900:
    linea=f'{colored(fecha_formateada, colores[3])}*/*{colored(canal, colores[2])}*/*{colored("USUARIO:", colores[0])}*/*{colored(mensaje, colores[3])}'
    lineatxt=f'{fecha_formateada} */* {canal} */* USUARIO */* {mensaje}'
  if roles.id != 1163180502681911316 and roles.id != 1163182355708661900:
    linea=f'{colored(fecha_formateada, colores[3])}*/*{colored(canal, colores[2])}*/*{colored("BOT:", colores[0])}*/*{colored(mensaje, colores[3])}'
    lineatxt=f'{fecha_formateada} */* {canal} */* BOT */* {mensaje}'
  print('console:', linea)
  
  ruta_archivo = "./informacion/data.txt"
  ruta_completa_archivo = os.path.join(os.path.dirname(__file__), ruta_archivo)
  with open(ruta_completa_archivo, 'a', encoding='utf-8') as archivo:
    archivo.write(f'{lineatxt} **** \n')

  if message.author == client.user:
    return
  ###########3FIN DE CONSOLA Y BLOG DE NOTAS#################


  #####################IA###############################

  if message.channel.id == 1169750972617199696:
    await message.channel.send("```Um... dejame pensar y te digo.```")
    respuesta = Bard().get_answer(str(message.content))['content']
    await message.channel.send(respuesta[:1999])

  ###############FIN IA ###############################


  ##############MENSAJES######################################
  if message.content.startswith('!github'):
    github_message = """
    ```Veo que estás buscando perfiles de GitHub. ¡Aquí tienes los 3 más importantes!```

    **Miguel Diaz (titooUvU)**
    [GitHub de Miguel Diaz](https://github.com/titooUvU)

    **Kaleth Renteria (keileth)**
    [GitHub de Kaleth Renteria](https://github.com/keileth)
    """
    await message.channel.send(github_message)
  

  if message.content.startswith('!newtask'):
    try:
      contenido_sin_comando = message.content.split(' ', 1)[1]
      print("nueva tarea: ", contenido_sin_comando)
      tasks += [contenido_sin_comando]
      mensaje = """
        ```▁ ▂ ▄ ▅ ▆ ▇ █ tarea agreada con exito █ ▇ ▆ ▅ ▄ ▂ ▁```
        """
    except:
      mensaje = """
        ```▁ ▂ ▄ ▅ ▆ ▇ █ No puedes crear una tarea vaciaaa, agrega contenido █ ▇ ▆ ▅ ▄ ▂ ▁```
        """
    await message.channel.send(mensaje)

  if message.content.startswith('!deltask'):
    try:
      contenido_sin_comando = message.content.split(' ', 1)[1]
      print("nueva tarea: ", contenido_sin_comando)
      try:
        del tasks[int(contenido_sin_comando)]
        mensaje = """
        ```tarea Eliminada con exito```
        """
      except:
        mensaje = """
        ```Porfavor agrega datos validos```
        """
    except:
      mensaje = """
      ```ou, peudes decirme que tarea borrar? (coloca el numero)```
      """
    await message.channel.send(mensaje)
  
  if message.content.startswith('< 3'):
    mensaje = "```tito te ama :3```"
    await message.channel.send(mensaje)

  if message.content.startswith('!tasks'):
    print(tasks)
    tareas=""
    for n,i in enumerate(tasks):
      tareas += f'\n🎈 {i}. ({n})'
    mensaje =f"""
    ```Las tareas pendientes son:{tareas}```
    """
    await message.channel.send(mensaje)

  if message.content.startswith('!sourse'):
    mensaje =f"""
    ```Hola!!! estos son nuestros paquetes que mas usamos:```
    **GENERAR FUENTES**:
    [abrir](https://fancy-generator.com/)

    **GENERAR TEMAS DE COLORES**:
    [abrir](https://uicolors.app/create)
    """
    await message.channel.send(mensaje)
  ##############FIN DE MENSAJES################################

client.run(my_secret)