class Perro:
    nombre = ""
    raza = ""
    tamanio = 0.0
    edad = 0
    def establecerNombre(self,nombre):
        self.nombre = nombre
    def obtenerNombre(self):
        return self.nombre
    def establecerRaza(self, raza):
        self.raza = raza
    def obtenerRaza(self):
        return self.raza
    def establecerTamanio(self,tamanio):
        self.tamanio = tamanio
    def obtenerTamanio(self):
        return self.tamanio
