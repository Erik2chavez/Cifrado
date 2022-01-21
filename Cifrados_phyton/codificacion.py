# -- coding: utf-8 --
def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result += chr((ord(char) + s -65) %26  +65)
             
        else:
                result += chr((ord(char) + s - 97) % 26 + 97)
                
    return result

text = input("El texto en plano a cifrar es: ")
    
s = int(input("El desplazamiento de cifrado es: "))
print ("el texto cifrado resultante es: " + encrypt(text, s) )

def des(text,s):
    resul = ""
    
    for i in range(len(text)):
        cha = text[i]
        
        if (cha.isupper()):
            resul += chr((ord(cha) - s -65 ) % 26 + 65)
        else:
            resul += chr((ord(cha) - s -97) %26 + 97)
            
    return resul
            
text = input("Codigo a descifrar: ")
    
s = int(input("El desplazamiento de cifrado es: "))
print ("El texto de cifrado es: " + des(text, s) )