class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_nota(self):
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")

    def esta_aprobado(self):
        print("Desaprobado" if self.nota < 5 else "Aprobado")


mi_alumno = Alumno("Nacho", 5)
mi_alumno2 = Alumno("Juan", 4)

mi_alumno.imprimir_nota()
mi_alumno.esta_aprobado()

mi_alumno2.imprimir_nota()
mi_alumno2.esta_aprobado()
