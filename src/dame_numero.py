def  comprobar_entero(cadena):
    cadena=cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())
           

def introduce_entero():
    cadena =  input("Introduce un numero entero: ")
    while not comprobar_entero(cadena):
        cadena=input("**ERROR** Eso no es un entero!!!\n\nIntroduce un número entero: ")

    return int(cadena)

def main():
    num = introduce_entero()
    print(f"Has introducido el número {num}")    

if  __name__=="__main__":
    main()    