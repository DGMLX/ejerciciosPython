'''Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Generalmente, realiza ventas por correo. La empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado. Considere crear un menú para hacer el càlculo en reiteradas ocasiones. No olvide validar.'''

pesoPayaso = 112
pesoMuneca = 75

while True:
    try:
        cantPayasos = int(input("Ingrese cantidad de payasos a enviar: "))
        cantMunecas = int(input("Ingrese cantidad de muñecas a enviar: "))
        if cantPayasos == 0 and cantMunecas == 0:
            print("Paquete de envio sin productos, no se puede realizar el calculo de peso.")
        else:
            pesoTotal = (cantPayasos*pesoPayaso) + (cantMunecas*pesoMuneca)
            print(f"El peso total del paquete es de {pesoTotal} gramos")
        opcion = int(input("Ingrese número 1 para seguir en el programa o 0 para salir: "))
        if opcion == 0:
            break
    except:
        print("No ingreso un Número ")    
        opcion = int(input("Ingrese número 1 para seguir en el programa o 0 para salir: "))
        if opcion == 0:
            break
print("Has salido del programa.")

