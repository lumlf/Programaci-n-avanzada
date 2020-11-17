class Persona:

    def __init__(self): 
        print("Bienvenido, registrese a continuación")
        self.nombre = str(input("Digite su nombre: "))
        while (self.nombre.isalpha()==False):  # Validación para que solo puedan ingresarse letras
            print("Dato inválido, por favor digite sólo letras")
            self.nombre=str(input("Digite su nombre: "))
        self.intentos = 0 
        self.cifras = 0        
        

    def imprimir(self):
            print("Tu nombre es: " , (self.nombre))

    def añadirlist(self, intentos, cifras):
        self.intentos = str(intentos)
        self.cifras = str(cifras)
        f = open("jugador.txt" , "a")
        f.write('Nombre: ' + self.nombre + '\n' + 'Intentos: ' + self.intentos + '\n' + 'Cifras: ' + self.cifras)
        f.close()