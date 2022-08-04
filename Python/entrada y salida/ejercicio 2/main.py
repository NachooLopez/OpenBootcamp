import pickle


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


v1 = Vehiculo("rojo", 4)

f = open("vehiculo.bin", "wb")
pickle.dump(v1, f)
f.close()

f = open("vehiculo.bin", "rb")
v2 = pickle.load(f)
f.close()

print(v1)
print(v2)
