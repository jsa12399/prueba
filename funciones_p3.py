

import msvcrt
import os
import time
import numpy




  



def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 10000000 and rut<= 999999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")       


def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")




def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de dias(1-100): "))
            if cantidad >= 1 and cantidad <= 100:
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DEBE ESTAR ENTRE 1 Y 100!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")








        





def id_unico():
    while True:
        id_unico_ = input("Ingrese su identificador unico: ") 
        if len(id_unico_) == 1:
            return id_unico
        else:
            print("Error debe ingresar un solo caracter")


def validar_nombre_mascota():
    while True:
        nombre = input("Ingrese nombre de su mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")  





