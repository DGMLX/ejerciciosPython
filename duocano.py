''' 
La sanguchería “El Duocano” ha tenido un crecimiento explosivo este 2023 y necesita que usted desarrolle un algoritmo
que le permita hacer las siguientes tareas:
a) Realizar Venta
b) Cerrar Turno
c) Salir
La opción a) debe mostrar el siguiente menú:
1.-DuocChoripan $1200
2.- DuocItaliano $1500
3.- DuocVegano $2000
4.- Salir
El cajero debe digitar la opción y el programa debe ir sumando hasta que la opción sea 4 y ahí debe entregar el total a pagar por un
cliente y volver al menú principal.
La opción b) será utilizada para cerrar la caja al cierre del turno entregando la recaudación acumulada de la caja hasta ese
momento y luego debe reiniciar la recaudación para el nuevo turno.
'''
opcion = 1
subtotal = 0
total = 0
while opcion != 3:
    opcionMenu=1
    print("1) Realizar venta")
    print("2) Cerrar caja")
    print("3) Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1 or opcion == 2 or opcion ==3:
                break
            else:
                print("Ingrese una opcion dentro del rango")
        except:
            print("Ingrese un valor numérico")
    if opcion == 1:
        while opcionMenu != 4:
            print("1) CHORIPAN 1200")
            print("2) COMPLETO ITALIANO 1200")
            print("3) PAN VEGANO")
            print("4) SALIR")
            while True:
                try:
                    opcionMenu = int(input("Ingrese una opcion: "))
                    if opcionMenu >0 and opcionMenu<5:
                        break
                    else:
                        print("Seleccione una opcion valida")
                except:
                    print("Ingresa un valor numerico")
            if opcionMenu == 1:
                subtotal += 1200
            elif opcionMenu == 2:
                subtotal += 1200
            elif opcionMenu == 3:
                subtotal += 1500
            else:
                print(f"El total recaudado es de {subtotal} pesos")
                break
    elif opcion == 2:
        print(f"Se cerro la caja con un valor de {subtotal}")
        total += subtotal
        subtotal = 0
    else:
        print(f"total al cerrar la caja fue de {total} pesos")