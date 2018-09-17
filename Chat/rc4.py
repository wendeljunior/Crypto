import sys
import operator
import codecs

def gerarFluxo(chaveBytes, textoBytes):
    S = []
    for i in range(256):
        S.append(i)

    T = []
    for i in S:
        T.append(chaveBytes[i % len(chaveBytes)])

    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        #swap
        aux = S[i]
        S[i] = S[j]
        S[j] = aux

    i = 0
    j = 0
    for i in range(len(textoBytes)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # swap
        aux = S[i]
        S[i] = S[j]
        S[j] = aux

        t = (S[i] + S[j]) % 256
        k = S[t]
        yield k


def encriptar(chave, texto):
    chave_unicode_bytes = [ord(c) for c in chave] #traduzindo cada caractere da chave em unicode
    texto_unicode_bytes = [ord(c) for c in texto] #traduzindo cada caractere do texto em unicode
    fluxoChave = gerarFluxo(chave_unicode_bytes, texto_unicode_bytes)
    resultado = []
    for c in texto:
        resultado.append("%02X" % operator.xor(ord(c), next(fluxoChave))) #XOR
    return resultado

def decriptar(chave, texto):
    chave_unicode_bytes = [ord(c) for c in chave] #traduzindo cada caractere da chave em unicode
    texto_unicode_bytes = [ord(c) for c in texto] #traduzindo cada caractere do texto em unicode
    fluxoChave = gerarFluxo(chave_unicode_bytes, texto_unicode_bytes)
    resultado = []
    for c in texto:
        resultado.append(chr(operator.xor(ord(c), next(fluxoChave))))  # XOR

        #resultado.append(codecs.decode(codecs.decode(c,'hex'), 'ascii'))
    return resultado

chave = 'segredo'
texto = 'Um texto qualquer'
texto_encriptado = encriptar(chave, texto)
print(texto_encriptado)
int_texto_encriptado = [int(c, 16) for c in texto_encriptado]
chars_texto_encriptado = [chr(c) for c in int_texto_encriptado]
texto_decriptado = decriptar(chave, chars_texto_encriptado)
print(texto_decriptado)
