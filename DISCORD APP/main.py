import discord
import os
from termcolor import colored
from dotenv import load_dotenv
import datetime

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)
my_secret = os.getenv('KEY')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'WUAAAAA, TODO ESTA BIENNN {client.user}')

tasks = []



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

  ##############MENSAJES######################################
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
  

  if message.content.startswith('!newtask'):
    try:
      contenido_sin_comando = message.content.split(' ', 1)[1]
      print("nueva tarea: ", contenido_sin_comando)
      tasks += [contenido_sin_comando]
      mensaje = """
        ▁ ▂ ▄ ▅ ▆ ▇ █ tarea agreada con exito █ ▇ ▆ ▅ ▄ ▂ ▁
        """
    except:
      mensaje = """
        ▁ ▂ ▄ ▅ ▆ ▇ █ No puedes crear una tarea vaciaaa, agrega contenido :angry:█ ▇ ▆ ▅ ▄ ▂ ▁
        """
    await message.channel.send(mensaje)

  if message.content.startswith('!deltask'):
    try:
      contenido_sin_comando = message.content.split(' ', 1)[1]
      print("nueva tarea: ", contenido_sin_comando)
      try:
        del tasks[int(contenido_sin_comando)]
        mensaje = """
        :white_check_mark: tarea Eliminada con exito
        """
      except:
        mensaje = """
        :x: Porfavor agrega datos validos
        """
    except:
      mensaje = """
      :x: ou, peudes decirme que tarea borrar? (coloca el numero)
      """
    await message.channel.send(mensaje)
  
  if message.content.startswith('< 3'):
    message = """
      :<3: tito te ama :3
      """
    await message.channel.send(message)

  if message.content.startswith('!tasks'):
    print(tasks)
    tareas=""
    for n,i in enumerate(tasks):
      tareas += f'\n:white_check_mark:  {i}. ({n})'
    mensaje =f"""
    Las tareas pendientes son:{tareas}
    """
    await message.channel.send(mensaje)

  if message.content.startswith('!sourse'):
    mensaje =f"""
    Hola!!! estos son nuestros paquetes que mas usamos:

    GENERAR FUENTES:
    --> https://fancy-generator.com/es#:~:text=Este%20generador%20de%20letras%20gratuito%20lo%20ayuda%20a,Twitter%20y%20otros%20sitios%20que%20admiten%20caracteres%20Unicode
    """
    await message.channel.send(mensaje)
  ##############FIN DE MENSAJES################################

client.run(my_secret)