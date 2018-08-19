import sys
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def recuperarLetra(letra, adicao):
    for i in range(len(alfabeto)):
        if(alfabeto[i] == letra):
            return alfabeto[(i+adicao)% len(alfabeto)]
        else:
            continue

def cifrar(mensagem, data, diretorioSaida):
    chave = data.replace('/','').lstrip("0")
    mensagem_sem_espacos = mensagem.replace(' ', '').lower()
    mensagem_cifrada = ""
        
    for i in range(0, len(mensagem_sem_espacos)):
        mensagem_cifrada += recuperarLetra(mensagem_sem_espacos[i], int(chave[i% len(chave)]))
    with open(diretorioSaida, 'w') as arquivoSaida:
        arquivoSaida.write(mensagem_cifrada)

data = sys.argv[1]
diretorioEntrada = sys.argv[2]
diretorioSaida = sys.argv[3]
arquivo = open(diretorioEntrada, 'r')
texto = arquivo.read()
cifrar(texto, data, diretorioSaida)



