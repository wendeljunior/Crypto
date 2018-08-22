import sys

alfabeto = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
alfabetoEspecial = "áâãóôõéíÁÂÃÓÔÕÉÍ"

def decifrar(chave, textoCifrado):
    chaveEstendida = estenderChave(chave, textoCifrado)
    textoDecifrado = ""
    for i in range(0, len(chaveEstendida)):
        if (textoCifrado[i] == '\n'):
            textoDecifrado += '\n'
            continue
        if (textoCifrado[i] in alfabetoEspecial):
            textoDecifrado += textoCifrado[i]
            continue
        try:
            posicaoLetraTextoCifradoAlfabeto = alfabeto.index(textoCifrado[i])
            posicaoLetraChaveEstendidaAlfabeto = alfabeto.index(chaveEstendida[i])
            posicaoLetraDecifradaAlfabeto = len(alfabeto) - posicaoLetraChaveEstendidaAlfabeto + posicaoLetraTextoCifradoAlfabeto;
            posicaoLetraDecifradaAlfabeto = posicaoLetraDecifradaAlfabeto % len(alfabeto)
            try:
                textoDecifrado += alfabeto[posicaoLetraDecifradaAlfabeto]
            except IndexError:
                print(posicaoLetraDecifradaAlfabeto)
                return ""
            #print(textoDecifrado)
        except ValueError:
            textoDecifrado += textoCifrado[i]
            
    return textoDecifrado

def estenderChave(chave, texto):
    chaveEstendida = ""
    for i in range(0, len(texto)):
        chaveEstendida += chave[i % len(chave)]
    return chaveEstendida

diretorioChave = sys.argv[1]
diretorioTexto = sys.argv[2]
chave = open(diretorioChave, 'r').read()
texto = open(diretorioTexto, 'r').read()
textoDecifrado = decifrar(chave, texto)
print(textoDecifrado)



