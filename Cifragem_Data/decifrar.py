import sys
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def recuperarLetra(letra, adicao):
    for i in range(len(alfabeto)):
        if(alfabeto[i] == letra):
            return alfabeto[(i-adicao)% len(alfabeto)]
        else:
            continue

def decifrar(mensagem, data):
    chave = data.replace('/','').lstrip("0")
    mensagem_minuscula = mensagem.lower()
    mensagem_cifrada = ""
        
    for i in range(0, len(mensagem_minuscula)):
        if(mensagem_minuscula[i]== ' '):
            mensagem_cifrada += ' '
            continue
        mensagem_cifrada += recuperarLetra(mensagem_minuscula[i], int(chave[i% len(chave)]))

    print(mensagem_cifrada)

data = sys.argv[1]
diretorio = sys.argv[2]
arquivo = open(diretorio, 'r')
texto = arquivo.read()
decifrar(texto, data)
