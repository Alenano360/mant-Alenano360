import string
from random import *

def generatePassword():
    minimo = 4
    maximo = 16
    cadena = string.ascii_letters + string.punctuation + string.digits
    contra = "".join(choice(cadena) for x in range(randint(minimo, maximo)))    
    
    print ("La contraseña aleatoria es: "+contra)

generatePassword()
