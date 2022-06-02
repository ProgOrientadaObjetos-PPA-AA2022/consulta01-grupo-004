class AreaRectangulo:
    base = 0.0
    altura = 0.0
    area = 0.0
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def establecerAltura(self,altura):
        self.altura = altura
    def obtenerAltura(self):
        return self.altura
    def establecerBase(self,base):
        self.base = base
    def obtenerBase(self):
        return self.base
    def establecerArea(self):
        self.area = self.altura * self.base
    def obtenerBase(self):
        return self.area
    def __str__(self):
        print("El area del rectangulo es: " + str(self.area))
        pass 