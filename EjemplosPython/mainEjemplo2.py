from ejemplo2 import Hospital
print("INFORMACION HOSPITAL")
nombreHospital = input("Ingrese el nombre del hospital:")
numeroCamas = int(input("Ingrese el numero de camas: "))
presupuesto = float(input("Ingrese el presupuesto:"))
hospital =  Hospital(nombreHospital,numeroCamas,presupuesto)
hospital.__str__()