# Realizado por 
# Juliana Castillo
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def obtenerModo():
    while True:
        print('¿Quieres encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in ('encriptar', 'e', 'desencriptar', 'd'):
            return modo
        else:
            print('Por favor, ingresa "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa un número de clave (1-26):')
        clave = int(input())
        if 1 <= clave <= 26:
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    traduccion = ''

    mensaje = mensaje.upper()

    for simbolo in mensaje:
        if simbolo in ALFABETO:
            num = ALFABETO.index(simbolo)
            
            if modo[0] == 'd':
                num -= clave
            else:
                num += clave

            if num < 0:
                num += len(ALFABETO)
            elif num >= len(ALFABETO):
                num -= len(ALFABETO)

            traduccion += ALFABETO[num]
        else:
            traduccion += simbolo

    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

print('Tu mensaje traducido es:')
print(obtenerMensajeTraducido(modo, mensaje, clave))