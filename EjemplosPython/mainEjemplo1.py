from ejemplo1 import Perro
print("MI PERRO WAU WAU")
dog = Perro()
dog.establecerNombre("Max")
dog.establecerRaza("Pastor aleman")
dog.establecerTamanio(1.32)
nombre = dog.obtenerNombre()
raza = dog.obtenerRaza()
tamanio = dog.obtenerTamanio()
print("El nombre del perro es "+ nombre +" su raza es "+ raza +" y mide "+ str(tamanio)+" metros.")
