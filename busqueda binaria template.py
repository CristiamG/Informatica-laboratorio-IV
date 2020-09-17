# Busqueda binaria

B = int(input("Ingrese el numero a buscar :"))
Lista = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
cont = 0
ban = False
bajo = 0
alto = len(Lista) - 1
central = (bajo + alto)//2
print('El número a buscar es: ',B)
while bajo <= alto:
    cont = cont + 1
    if Lista[central] == B:
        ban = True
        break
    elif Lista[central] > B:
        alto = central-1
    else:
        bajo = central+1
    central = (bajo + alto)//2
    print(cont , central , Lista[central] , Lista[bajo:alto+1] )
if ban:
    print("en" ,cont, "esta el número")
    print ("El número esta en la posicion" ,central, )
else:
    print("No se encontró el número que ingresó")


        # Imprima: La iteración, el valor de central, el valor de L[central] y el intervalo actual de busqueda (consulte cómo indicar un intervalo de una lista en Python)

    # Imprima la cantidad de iteraciones que hizo el ciclo

    #****************************** Salida esperada ***********************************#
# Número: 57
#
#Iteración: 1, central = 3, L[central] = 23, Intevalo: [2, 10, 20, 23, 41, 45, 57, 90]
#Iteración: 2, central = 5, L[central] = 45, Intevalo: [41, 45, 57, 90]
#Iteración: 3, central = 6, L[central] = 57, Intevalo: [57, 90]
#
#Numero encontrado en la posición 6
#
#Cantidad de iteraciones 3
#**********************************************************************************#
