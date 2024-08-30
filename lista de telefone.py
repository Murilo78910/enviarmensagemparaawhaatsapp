'''Lembre-se de colocar os números na lista, sempre com o código do país e do estado'''

import pywhatkit
import pywhatkit.whats
import pyautogui
import time

# Função para ler os números de telefone do arquivo .txt
def ler_numeros_de_telefone(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            numero = linha.strip() # Remover espaços em branco e quebras de linha
            numeros.append(numero)
    return numeros

# Ler os números de telefone do arquivo
arquivo_telefones = "lista_de_telefone.txt"
numeros_de_telefone = ler_numeros_de_telefone(arquivo_telefones)

# Escreve a mensagem que você quer
mensagem = input("Digite a mensagem que deseja enviar: ")

for numero in numeros_de_telefone:
    pywhatkit.sendwhatmsg_instantly(numero, mensagem)
    time.sleep(5) # Aguarda um tempo para enviar a mensagem
    pyautogui.hotkey('alt', 'f4') # Fecha a janela
    time.sleep(10) # Aguarda um tempo antes de enviar a próxima mensagem
    