

def introduce_nombre(nombre):
    return nombre.strip()

def main():
    nombre=input("Introduce tu nommbre: ")
    print(f"Hola, {introduce_nombre(nombre)}")

if __name__=="__main__":
    main()