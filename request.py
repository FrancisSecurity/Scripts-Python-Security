#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from requests.models import Response
from requests.sessions import session
import hashlib


url='http://134.209.27.142:30576/'
s = requests.session()   #para manter a sessão ativa e preservar o cookie


html = s.get(url).content # estanciado o objeto "S" e usado o parametro get para baixar o html da pagina e armazenado o html na variavel HTML 

soup = BeautifulSoup(html, 'html.parser') # usando a bliblioteca SOUP para encontrar o que quiser no variavel que contem o HTML baixado acima
texto = soup.find("h3").string  #Usado a opção FIND e passado a chave "h3" e obtido somente a string 

md5 = str(hashlib.md5(texto.encode('utf8')).hexdigest()) #encriptando o conteudo que foi pego na opção find acima
response = s.post(url,data={"hash":md5})  #passando o texto encriptado em formato MD5 via POST, obervar sempre se está utilizando o objeto qu mantem a sessão ativa

print(md5)
var = BeautifulSoup(response.content, 'html.parser').prettify() #printa na tela o resultado obtido após passado o parametro via post, que no caso é a chave que precisamos, utilizamos BeautifulSoup para uma saida mais amigavel  
print(var)
