# Ejercicio en clase tercera semana 
ingreso = str(input("Ingrese la fecha actual: el nombre del día, número de día y mes: "))
ingreso = ingreso.lower()

dia = ingreso[0:ingreso.find(',')]
if(dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes"):
    dia=str("Se produjo un error.")



dd = int(ingreso[ingreso.find(' ')+1 : ingreso.find('/')])
if(dd > 32 or dd < 0):
    dd=str("Se produjo un error.")


mm = int(ingreso[ingreso.find('/')+1 : len(ingreso)])
if(mm>12 or mm<0):
    mm=str("Se produjo un error.")

if(dia == "Se produjo un error." or dd == "Se produjo un error." or mm == "Se produjo un error."):
    print("Se produjo un error, se ingreso la fecha incorrecta")
else:
    print("[", dia,", ", dd, "/", mm, "]")



if(dia == "lunes" or dia == "martes" or dia == "miercoles"):
    exa = str(input("Se tomaron examenes?"))
    exa = exa.lower()
    if(exa == "si"): 
        aprob = int(input("Ingrese la cantidad de aprobados: "))
        desaprob = int(input("ingrese la cantidad de desaprobados: "))
        tt =  aprob + desaprob 
        aprob1 = (aprob*100)/tt
        desaprob1 = (desaprob*100)/tt
        if(aprob1 == 0):
            print("Desaprobó toda la clase.")
        if(desaprob1 == 0 ):
            print("Aprobó toda la clase.")
        if(aprob1 != 0 and desaprob1 != 0):
            print("Aprobó el ", aprob1, "% y desaprobó el ", desaprob1, " % de la clase")

if(dia == "jueves"):
    porcent = int(input("Ingresar el porcentaje de asistencia: "))
    if( porcent > 50):
        print("Asistió la mayoría.")
    else:
        print("No asistió la mayoría.")

if(dia == "viernes"):
    if((dd == 1 and mm == 1) or (dd == 1 and mm == 7)): 
        print("Comienzo de nuevo ciclo")
        cant = int(input("Ingrese la cantidad de alumnos: "))
        aranceles = int(input("Ingrese el valor de arancel por alumno: "))
        print("Con la cantidad de ", cant, " alumnos se va a obtener un ingreso total de ", aranceles*cant, "$." )




