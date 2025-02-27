#Create by
#REBECA HCr
import os
import time
def tabla():
    print("<---Dime que tabala de multiplicar quieres--->")
    x=int(input(""))
    a=1
    while a <= 10: #ciclo
        print(f"{x} * {a} = {x*a}")
        a+=1
    time.sleep(1)

def numero():
    x = int(input("Escribe un numero "))
    if x%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    time.sleep(1)


def anidado():
    n1=int(input("Ingresa tu calificacion----->"))
    if n1==100:
        print("Exelente felicidades")
    elif n1<=99 and n1>=90:
        print("Muy bien")
    elif n1<=89 and n1>=80:
        print("Bien")
    elif n1<=79 and n1>=70:
        print("Alumno regular")
    else:
        print("Alumno no aprobado")
    time.sleep(1)


def exponenciales():
    x = int(input("Ingresa un numero "))
    i = 0
    m = 0
    d = 0
    for i in range(1, x+1):
        m = (i**i)*i
        print(f"{i}  ^   {i+1}  =  {m}")
        d+=m

    print(f"{d} / {x} = {d/x}")
    time.sleep(1)


def control():
    import datetime
    import os
    fecha = datetime.datetime.now()
    año = datetime.datetime.strftime(fecha, "%Y")
    d1 = {"Ing Indistrial", "Tic's", "Ing Sistemas", "Ing Quimica", "Ing Civil", "Ing Mecatronica", "Ing Electrica", "Ing Logistica", "Lic Administracion"}
    p="error"
    while p=="error":
        print("Selecciona una opcion ")
        print("1. Provienes de otra escuela")
        print("2. Hiciste examen de admision en el tec o pase por promedio")
        print("3. Salir")
        x = int(input(""))
        match x:
            case 1:
                print("Selecciona tu carrera")
                c=1
                for i in d1:
                    print(c, ".", i)
                    c+=1    
                y = int(input(""))
                if y<1 or y>9:
                    print("Error")
                else:
                    g = int(input("Ingresa tu numero de alumno "))
                    no = (str(año)+str(x)+str(y)+str(g))
                    r = len(no)
                    t=1
                    if g>999 or g<1:
                        print("El numero es incorrecto")
                    else:    
                        for d in range(1,t+1):
                            if r==9:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(y)+str(g))

                            if r==8:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(y)+ "0"+ str(g)) 

                            if r==7:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(y)+ "00"+ str(g)) 
            case 2:
                print("Selecciona tu carrera")
                w=1
                for i in d1:
                    print(w, ".", i)
                    w+=1
                s = int(input(""))
                if s<1 or s>9:
                    print("Error")
                else:
                    h = int(input("Ingresa tu numero de alumno "))
                    nu = (str(año)+str(x)+str(s)+str(h))
                    u = len(nu)
                    j=1
                    if h>999 or h<1:
                        print("El numero es incorrecto")
                    else:
                        for d in range(1,j+1):
                            if u==9:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(s)+ str(h)) 

                            if u==8:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(s)+ "0"+ str(h)) 

                            if u==7:
                                print("Tu numero de control es ")
                                print(str(año)+str(x)+str(s)+ "00"+ str(h))
                time.sleep(1)
            case 3:
                break

            case _:
                os.system("cls")
                print("Operacion invalida")
                p="error"


while True:
    print("")
    print("")
    print("-----> Menu de opciones <-----")
    print("1.- x tabla de multiplicar")
    print("2.- Numero par o impar")
    print("3.- if anidado")
    print("4.- Formula/exponenciales")
    print("5.- Numero de control")
    print("6.- Salir")

    pro = int(input("Elige una opccion-----> "))
    match pro:
        case 1:
            tabla()

        case 2:
            numero()
        
        case 3:
            anidado()
        
        case 4:
            exponenciales()
        
        case 5:
            control()

        case 6:
            os.system("cls")
            break

        case _:
            print("Opcion invalida")
        
