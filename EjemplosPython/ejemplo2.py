class Hospital:
    nombreHospital = ""
    numeroCamas = 0
    presupuesto = 0.0
    def __init__(self,nombreHospital,numeroCamas,presupuesto):
           self.nombreHospital = nombreHospital
           self.numeroCamas = numeroCamas
           self.presupuesto = presupuesto 
    def establecerNombreHospital(self,nombreHospital):
        self.nombreHospital = nombreHospital
    def obtenerNombreHospital(self):
        return self.nombreHospital
    def establecerNumeroCamas(self,numeroCamas):
        self.numeroCamas = numeroCamas
    def obtenerNumeroCamas(self):
        return self.numeroCamas
    def establecerPresupuesto(self,presupuesto):
        self.presupuesto = presupuesto
    def obtenerPresupuesto(self):
        return self.presupuesto
    def __str__(self):
        print("El hospital " + self.nombreHospital + " tiene un numero de camas " + str(self.numeroCamas) + " y un presupuesto de " + str(self.presupuesto))
        pass