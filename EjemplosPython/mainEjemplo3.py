from ejemplo3 import AreaRectangulo
print("CALCULO AREA RECTANGULO")
base = float(input("Cual es la base del rectangulo: "))
altura = float(input("Cual es la altura del rectangulo: "))
areaRectangulo = AreaRectangulo(base,altura)
areaRectangulo.establecerArea()
areaRectangulo.__str__()