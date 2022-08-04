def main():
    paises_input = input("Introduce los paises separados por coma: ")
    paises = paises_input.split(", ")
    paises_unicos = set(paises)

    print(sorted(paises_unicos))


if __name__ == "__main__":
    main()
