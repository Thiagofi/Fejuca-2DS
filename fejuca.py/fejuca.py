import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'programacao', 'inteligencia', 'artificial']
    return random.choice(palavras)

def exibir_estado(palavra, letras_certas):
    return ' '.join(letra if letra in letras_certas else '_' for letra in palavra)

import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'programacao', 'inteligencia', 'artificial']
    return random.choice(palavras)

def exibir_estado(palavra, letras_certas):
    return ' '.join(letra if letra in letras_certas else '_' for letra in palavra)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\n" + exibir_estado(palavra, letras_certas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        tentativa = input("Digite uma letra: ").lower()
        
        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if tentativa in palavra:
            letras_certas.add(tentativa)
            if set(palavra) == letras_certas:
                print("\nParabéns! Você ganhou!")
                print(f"A palavra era: {palavra}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1

        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()

