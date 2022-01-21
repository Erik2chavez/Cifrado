# -- coding: utf-8 --

abc= 'ABCDEGHIJKLMNÑOPQRSTUVWXYZ '

def cifrar(cadena, llave):
    texto_cifrado = ''
    
    i = 0
    for letra in cadena:
        s = abc.find(letra) + abc.find(llave[i % len(llave)])
        modulo = int(s) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[modulo])
        i=i+1
    return texto_cifrado

def descifrar(cadena, llave):
    texto_descifrado = ''
    
    i = 0
    for letra in cadena:
        s = abc.find(letra) - abc.find(llave[i % len(llave)])
        modulo = int(s) % len(abc)
        texto_descifrado = texto_descifrado + str(abc[modulo])
        i=i+1
    return texto_descifrado

def main():
    cadena = input("El texto en plano a cifrar es: ").upper()
    llave = input("La palabra clave para cifrar es: ").upper()
    print ("El texto cifrado resultante es: " + cifrar(cadena,llave) )
    
    cadena = input("El texto cifrado a descifrar es: ").upper()
    llave = input("La palabra clave para descifrar es: ").upper()
    print("El texto original es: " + descifrar(cadena, llave) )
    
if __name__== "__main__":
    main()