import sys

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


def encriptar(texto, chave):
    chave_unicode_bytes = [ord(c) for c in chave] #traduzindo cada caractere da chave em unicode
    texto_unicode_bytes = [ord(c) for c in texto] #traduzindo cada caractere do texto em unicode
    fluxoChave = gerarFluxo(chave_unicode_bytes, texto_unicode_bytes)
#    resultado = []
#    for i in range(len(fluxoChave)):
#        resultado.append(fluxoChave[i] ^ texto_unicode_bytes[(i+1) % len(fluxoChave)])
#    for c in resultado:
#        print("%02X" % c)
    for c in texto:
        sys.stdout.write("%02X" % (next(ord(c)) ^ fluxoChave))

chave = 'Key'
texto = 'Plaintext'
encriptar(chave, texto)