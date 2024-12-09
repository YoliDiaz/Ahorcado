dibujo_ahorcado = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    ======= 
    ''',
    '''
     +---+
     |   |
     o   |
         |
         |
         |
    ======= 
    ''',
    '''
     +---+
     |   |
     o   |
     |   |
         |
         |
    ======= 
    ''',
    '''
     +---+
     |   |
     o   |
    /|   |
         |
         |
    ======= 
    ''',
    '''
     +---+
     |   |
     o   |
    /|\  |
         |
         |
    ======= 
    ''',
    ''' 
    +---+
     |   |
     o   |
    /|\  |
    /    |
         |
    ======= 
    ''',
]

palabra = list('calavera')
palabra_oculta =['_']*len(palabra)
intentos = 6
lista_abecedario = list('abcdefghijklmnñopqrstuvwxyz')
letras_descartadas = []

def mostrar_estado():
    print(f'Intentos restantes: {intentos}')
    print(f'Letras descartadas: {",".join(letras_descartadas)}\n')
    print(f'Palabra: {" ".join(palabra_oculta)}\n')
    print(dibujo_ahorcado[6 - intentos])

def letra_valida(letra):
    if len(letra) != 1:
        print("Has puesto más de una letra, inténtalo de nuevo")
        return False
    elif letra not in lista_abecedario:
        print("No has introducido una letra del abecedario")
        return False
    elif letra in letras_descartadas:
        print("Esa letra ya la habías dicho, intentalo de nuevo")
        return False
    else:
        return True

def gestion_letra(letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            palabra[i] = "_"

print("☠️ BIENVENIDO AL JUEGO DE AHORACADO ☠️\n")
print("Reglas de juego: Introduce letras para adivinar la palabra oculta")
print(f'Tienes {intentos} intentos. ¡Buena Suerte! 🥳')

while intentos > 0 and '_' in palabra_oculta:
    mostrar_estado()
    print('-'*50)
    letra = input("INTRODUCE LETRA: ").lower()

    while not letra_valida(letra):
        letra = input("INTRODUCE OTRA LETRA: ").lower()

    if letra in palabra:
        gestion_letra(letra)
        print('-'*50)
        print("¡Has acertado la letra! 🥳. Sigue asi")
    else:
        print('-'*50)
        print("¡Has fallado la letra! 😭")
        letras_descartadas.append(letra)
        intentos -= 1

if '_' not in palabra_oculta:
    print("\n\n🏆🎉¡ENHORABUENA! ¡HAS GANDO EL JUEGO!🎉🏆")
else:
    print(f'\nVaya... Lo siento ¡HAS PERDIDO!☠️  ☠️'
    '''\n
    +---+
     |   |
    💀   |
    /|\  |
    / \  |
         |
    ======= 
    ''')
