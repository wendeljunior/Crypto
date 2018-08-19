import sys
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteresEspeciais = ",()!.?;:<>*%$#@/-_ "        

def decifrar(texto, chave):
    mensagem = ""
    for char in texto:
        if(char in alfabeto_minusculo):
            mensagem += alfabeto_minusculo[(alfabeto_minusculo.index(char) - chave) % 26]
        elif(char in alfabeto_maiusculo):
            mensagem += alfabeto_maiusculo[(alfabeto_maiusculo.index(char) - chave) % 26]
        elif(char in caracteresEspeciais):
            mensagem += char
    return mensagem
        
arquivoMensagem = sys.argv[1]
chave = sys.argv[2]
mensagem_cifrada = open(arquivoMensagem, 'r').read()
mensagem_decifrada = decifrar(mensagem_cifrada, int(chave))
print(mensagem_decifrada)