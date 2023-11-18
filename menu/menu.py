from class_usuario import Usuario
import sys
import os

global switch
switch = False
usr = Usuario()

def menu():
    global switch
    opc = 0

    if not switch:
        os.system("clear")
        opc = 1
        switch = True
    else:
        print ('_________________________________________')
        print ("\n")
        print ('    1-Capturar nuevo usuario ')
        print ('    2-Imprimir en pantalla ')
        print ('    3-Editar Usuario ')
        print ('    4-Salir ')
        print ("\n")
        while opc < 1 or opc > 4:
            opc = int (input ('Ingrese una opcion: '))
            if opc >= 1 and opc <= 4:
                switch = True
                ejecutar(opc)
    return opc 

def ejecutar(opc):
    if opc == 1:
        regUser()
        os.system("clear")
        menu()
    elif opc == 2:
        os.system("clear")
        print ("\n")
        usr.imprimir()
        print ("\n")
        menu()
    elif opc == 3:
        editUser()
        os.system("clear")
        menu()
    elif opc == 4:
        sys.exit()
        

def regUser():
    nombre = input('Ingrese nombre: ')
    direccion = input('Ingrese dirección: ')
    telefono = input('Ingrese teléfono: ')
    usr.capturar(nombre, direccion, telefono)

def editUser():
    print("\n".join(['', ' 1-Nombre ', ' 2-Direccion', ' 3-Telefono ', ' 4-Volver al menu ', '']))
    old = 0
    while old < 1 or old > 4:
            old = int (input ('  Elija una opcion:  '))
            if old >= 1 and old <= 3:
                new = input ('  Capture el nuevo dato:  ')
                usr.modificar(old, new )
            elif old == 4:
                os.system("clear")
                menu()
    

ejecutar(menu())