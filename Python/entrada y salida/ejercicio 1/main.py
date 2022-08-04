

def main():
    archivo = open("./archivo.txt", "w")
    archivo.write("Escribí en el archivo")
    archivo.close()

    archivo = open("archivo.txt", "r")
    datos = archivo.read()
    archivo.close()
    print(datos)


if __name__ == "__main__":
    main()
