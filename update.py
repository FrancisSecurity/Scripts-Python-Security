#!/bin/python3
from paramiko import SSHClient, sftp, sftp_client
from colorama import *
import paramiko
import ipaddress
import os
import socket
import sys

port = 22
user = "root"
senha = "root"


if len(sys.argv) <= 3:
    init(autoreset=True)
    print(Back.RED + "                                  Modo de Usar o sistema FrancisCOPY...:                                    ")
    print("")
    print("Usage: {} [192.168.0.0/24] [origem_arquivo/arquivo.extensao]  [Destino_remoto_arquivo/arquivo.extensao] ".format(sys.argv[0]))
    print("")
    print("Exemplo {} 192.168.20.72 /opt/teste.txt  /opt/teste.txt".format(sys.argv[0]))
   
   # print("Caso queira copiar para toda a rede usar {} 192.168.0.0/24 ".format(sys.argv[0]))
    #print("Caso queira Copiar somente para um unico host retirar a mascar EX {} 192.168.20.72".format(sys.argv[0]) )
    exit()
else:
    for i in ipaddress.ip_network(sys.argv[1], strict=False):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resul = s.connect_ex((str(i),port))
        if resul == 0:
            init(autoreset=True)
            print(Back.BLUE + "*"*100)
            print(Fore.RED  + "conectando em {}".format(i))
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=str(i), username=user, password=senha, port=22)
                sftp_client=ssh.open_sftp()
                print(Fore.RED  + "Copiando Arquivos para ..:  {}".format(i))
                sftp_client.put(sys.argv[2], sys.argv[3])
                sftp_client.close()
                ssh.close()
            except Exception as e:
                print(Back.RED + "Erro ao conectar ",e)
                ssh.close()
print(Fore.MAGENTA + 
"""
 O\\
/(\\
ºnº
 ||
J J 
Obrigado!!
""")                