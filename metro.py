'''Metro de Valparaíso ofrece su servicio de transporte de lunes a viernes desde las06:00 hasta las 22:30. El horario punta comienza desde las 07:30 hasta las 09:00(incluidos). El resto del tiempo se considera horario normal.Durante el horario normal circulan trenes cada 12 minutos. En el horario puntacirculan trenes cada 6 minutos. Desarrolle un programa en Pseint que, en base ala hora ingresada por el usuario, determine si se encuentra en horariopunta o normal. Además, debe indicar cuántos minutos faltan para que llegue elpróximo tren.
ejemplo:
ingrese hora [0-23]
ingrese minutos [0-59]
hora - el metro se encuentra X en esta hora
horario normal o horario punta .. pasa cada x minutos
el siguiente metro pasa en x minutos
'''
import math
frNormal = 12
frPunta = 6
opcion= 1
while opcion == 1:
    while True:
        try:
            hora = int(input("Ingrese la hora [0-23] : "))
            if hora >=0 and hora <=23:
                break
            else:
                print("Debes ingresar una hora válida")
        except:
            print("Debes ingresar valores numéricos")
    while True:
        try:
            minuto = int(input("Ingrese los minutos [0-59] : "))
            if minuto >=0 and minuto<=59:
                break
            else:
                print("Debes ingresar minutos válidos")
        except:
            print   ("Debes ingresar valores numéricos")

#TRANSFORMAR MINUTO Y HORA A CADENA DE TEXTO PARA UNIRLOS EJ: 23 + 12 = 2312
    if minuto >=0 and minuto <10:
        minutoString = "0" +str(minuto)
    else:
        minutoString =str(minuto)
    horaString = str(hora)
    hora = horaString + minutoString
    horaNumber = int(hora)
    if (horaNumber >900 and horaNumber < 2230) or (horaNumber >600 and horaNumber < 730):
        proximoMetro = (math.ceil(int(minuto)/frNormal) * frNormal)- int(minuto)
        if proximoMetro == 0:
            proximoMetro == frNormal
        print("*"*50)
        print("HORARIO NORMAL")
        print("EL METRO PASA CADA 12 MINUTOS")
        print(f"FALTAN {proximoMetro} MINUTOS PARA EL PROXIMO METRO")
        print("*"*50)
    elif horaNumber > 730 and horaNumber <= 900:
        proximoMetro = (math.ceil(int(minuto)/frPunta) * frPunta)- int(minuto)
        if proximoMetro == 0: 
            proximoMetro = frPunta
        print("*"*50)
        print("HORARIO PUNTA")
        print("EL METRO PASA CADA 6 MINUTOS")
        print(f"FALTAN {proximoMetro} MINUTOS PARA EL PROXIMO METRO")
        print("*"*50)
    else:
        print("EL METRO SE ENCUENTRA CERRADO") 
    while True:   
        try:
            print("1) Si")
            print("2) No")
            opcion = int(input("¿Desea hacer otra consulta?: "))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("Ingrese 1 o 2.")
        except:
            print("Ingrese un valor numérico")
    if opcion == 2:
        print("Has salido del programa")
        break




    