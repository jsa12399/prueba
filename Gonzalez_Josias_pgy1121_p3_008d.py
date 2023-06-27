import msvcrt
import os
import time
import numpy

import funciones_p3 as fn

def id_unico():
    while True:
        id_unico_ = input("Ingrese su identificador unico: ") 
        if len(id_unico_) == 1:
            return id_unico
        else:
            print("Error debe ingresar un solo caracter")

def validar_nombre_mascota():
    while True:
        nombre_mascota = input("Ingrese nombre de su mascota: ")
        if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
            return nombre_mascota
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")            
contador = 1


lista_ruts=[]
lista_id_unico=[]
lista_cantidad_dias=[]
arreglo_habitacion = numpy.zeros((2,5))


os.system('cls')
while True:
    print("""Menú
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir """)
    opcion = fn.validar_opcion()
    time.sleep(2)
    if opcion == 1:
        os.system('cls')
        rut = fn.validar_rut()
        lista_ruts.append(rut)
        fn.validar_nombre()
        id_unico_ = fn.id_unico()
        lista_id_unico.append(id_unico_)
        nombre_mascota = fn.validar_nombre_mascota()
        cantidad_dias = fn.validar_cantidad()
        lista_cantidad_dias.append(cantidad_dias)
        print(arreglo_habitacion)

        fila= int(input("Ingrese fila que desea: "))
        columna= int(input("Ingrese columna que desea: "))
        arreglo_habitacion= fila-1 and columna-1
        print("Habitacion Comprada")
        
        os.system('cls')
    elif opcion ==2:
        rut = fn.validar_rut()  
        x = rut      
        for x in range (len(lista_ruts)):
            if x in (lista_ruts):
                lista_ruts[x]
                print("Su mascota se encuentra en la habitacion",arreglo_habitacion)


    elif opcion ==3:
        rut = fn.validar_rut()        
        for x in range (len(lista_ruts)):
            posicion = x
            if x in len(lista_ruts):
                print("Su total a pagar es:", cantidad_dias * 15000)
    else:
        print("Gracias por su visita")
        break                
