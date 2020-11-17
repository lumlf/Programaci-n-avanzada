class Juego():
    import random

    control = 1
    
    while control == 1:
        from jugador import Persona
        jugador=Persona()
        # Elección de la dificultad del juego. 
        print("Elige con cuantas cifras quieres jugar: \n 1 = 3 cifras \n 2 = 4 cifras \n 3 = 5 cifras")
        while True:
            try:
                dificultad = int(input("Digita la dificultad del juego: "))
                break
            except:
                print("Error, digita de nuevo")
        if (dificultad == 1):
            num = 3
            while True:
                try:
                    user = int(input(" Para inciar Digita un numero de 3 digitos "))
                    if(user > 100 and user <= 999):
                        break
                except:
                    print("Error, digita de nuevo")
        elif (dificultad == 2):
            num = 4
            while True:
                try:
                    user = int(input("Para inciar Digita un numero de 4 digitos "))
                    if(user > 1000 and user <= 9999):
                        break
                except:
                    print("Error, digita de nuevo")
        elif (dificultad == 3):
            num = 5
            while True:
                try:
                    user = int(input(" Para inciar Digita un numero de 5 digitos "))
                    if(user > 10000 and user <= 99999):
                        break
                except:
                    print("Error, digita de nuevo")
        numeros = ('1','2','3','4','5','6','7','8','9')  # Separación de dígitos.
        adivinar = ''  # Generación de variable donde se almacena el número aleatorio.
        for i in range (num):  # Ciclo donde se genera el número aleatoriamente. 
            elegido = random.choice(numeros)
            while elegido in adivinar:
                elegido = random.choice(numeros)
            adivinar = adivinar + elegido
        print("Adivina el número de: " , num , "dígitos diferentes")

        propuesta = input("¿Cuál es el número?:")  # Almacenamiento del número ingresado por el usuario
        prop = ''
        prop = propuesta
        repetidos = 0
        intentos = 0
        nivel = str(num)
        inten = str(intentos)


        # Ciclo de comparación del número ingresado por el usuario y el número generado aleatoriamente.
        while (propuesta != adivinar): 
            intentos = intentos + 1
            fijas = 0
            picas = 0
            for i in range(num):
                if (propuesta[i] == adivinar[i]):
                    fijas = fijas + 1
                elif propuesta[i] in adivinar:
                    picas = picas + 1
            print("El numero " , (propuesta) , " tiene " , (picas) , " Picas y " , (fijas) , " Fijas")

            # Agrega los valores almacenados en las variables indicadas al archivo historial.txt 
            fij = str(fijas)
            pic = str(picas)
            inten = str(intentos)
            propu = str(propuesta)
            f = open("historial.txt", "a")
            f.write(jugador.nombre + "," + nivel + "," + propu + "," + inten + "," + pic + "," + fij + "\n")
            f.close()

            propuesta = input("Coloca otro numero")
            
        # Agrega en el archivo historial.txt el último registro de cuándo adivinó el número 
        if (propuesta == adivinar):
            adiv = str(adivinar)
            f = open("historial.txt", "a")
            f.write(jugador.nombre + "," + nivel + "," + adiv + "," + inten + "," + "0" + "," + nivel + "\n")
            f.close() 

        print ("¡¡Felicitaciones," + jugador.nombre + " has adivinado el numero en", (intentos),"intentos!!")

        jugador.añadirlist(intentos , num)  # Añade al jugador al archivo jugador.txt

        mejorpj = ""        # Muestra la tabla de jugadores
        menor_intentos = 100

        mejorpj2 = ""
        menor_intentos2 = 100

        mejorpj3 = ""
        menor_intentos3 = 100


        f = open("historial.txt","r")
        for linea in f.readlines():
            elementos = [str(x) for x in linea.split(",")]

            if(int(elementos[1])==3):
                if(int(elementos[5])==3):
                    if(int(elementos[3]) < menor_intentos):

                        #print ("entro a 1")
                        #print("el numero de intentos fue" + elementos[3])
                        menor_intentos = int(elementos[3])
                        mejorpj = elementos[0]

            elif(int(elementos[1])==4):
                if(int(elementos[5])==4):
                    if(int(elementos[3]) < menor_intentos2):

                        #print ("entro a 2")        
                        #print("el numero de intentos fue" + elementos[3])
                        menor_intentos2 = int(elementos[3])
                        mejorpj2 = elementos[0]
    
    
            elif(int(elementos[1])==5):
                if(int(elementos[5])==5):
                    if(int(elementos[3]) < menor_intentos3):

                        #print ("entro a 3")        
                        #print("el numero de intentos fue" + elementos[3])
                        menor_intentos3 = int(elementos[3])
                        mejorpj3 = elementos[0]
    


            #for i in range(len(elementos)):
                #print(elementos[i])


        if int(menor_intentos) !=100:
            print("el record de nivel 1 lo realizo:"+mejorpj)        
            print("el numero de intentos del  record es:"+str(menor_intentos))

        if int(menor_intentos2) !=100:
            print("el record de nivel 2 lo realizo:"+mejorpj2)        
            print("el numero de intentos del  record es:"+str(menor_intentos2))

        if int(menor_intentos3) !=100:
            print("el record de nivel 3 lo realizo:"+mejorpj3)        
            print("el numero de intentos del  record es:"+str(menor_intentos3))
            
        f.close()


        control = int(input("¿Desea continuar? \n 1 = Si \n 0 = No \n"))
        if control == 0:
            print("Gracias por jugar")
            exit()


        


