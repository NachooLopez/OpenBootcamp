from functools import reduce


def impares(lista):
    filtrado = filter((lambda x: x % 2), lista)
    sumatoria = reduce((lambda x, y: x + y), filtrado)
    print(sumatoria)


def main():
    lista = [1, 2, 9, 2, 5, 10, 23, 8]
    impares(lista)


if __name__ == "__main__":
    main()
