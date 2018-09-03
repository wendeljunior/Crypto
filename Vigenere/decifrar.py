import sys

alfabeto = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
alfabeto_especial = "áàãâéèêíìîóòõôúùûÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ\n"

def decifrar(chave, textoCifrado):
    textoDecifrado = ""
    textoCifradoAlfabeto = ""
    for char in textoCifrado:
        if (char in alfabeto):
            textoCifradoAlfabeto += char
    for i in range(0, len(textoCifradoAlfabeto)):
        chaveEstendida = chave[i % len(chave)]
        try:
            posicaoLetraTextoCifradoAlfabeto = alfabeto.index(textoCifradoAlfabeto[i])
            posicaoLetraChaveEstendidaAlfabeto = alfabeto.index(chaveEstendida)
            posicaoLetraDecifradaAlfabeto = len(alfabeto) - posicaoLetraChaveEstendidaAlfabeto + posicaoLetraTextoCifradoAlfabeto;
            posicaoLetraDecifradaAlfabeto = posicaoLetraDecifradaAlfabeto % len(alfabeto)
            try:
                textoDecifrado += alfabeto[posicaoLetraDecifradaAlfabeto]
            except IndexError:
                print("ERRO 1" + posicaoLetraDecifradaAlfabeto)
                return None
        except ValueError:
            print("ERRO 2")
            return None
    return textoDecifrado

diretorioChave = sys.argv[1]
diretorioTexto = sys.argv[2]
chave = open(diretorioChave, 'r').read()
texto = open(diretorioTexto, 'r').read()
textoDecifrado = decifrar(chave, texto)
print(textoDecifrado)



