# Busqueda lineal
b = int(input("ingrese un número que desee buscar:   "))

lista = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
ban = False
for n in range(len(lista)):
    if b == lista[n]:
        ban = True
        break
    print("La iteración " ,n+1, " = "   ,lista[n])
if ban:
    print("El número encontrado está ubicado en la posición", n+1, "y es el: ",b)
else:
    print("El número no se encuentra en la lista")
print("La cantidad de ciclos realizados fue de:  ",n+1)


## Variables a emplear
#L = [2, 10, 20, 23, 41, 45, 57, 90] # Lista (cambiar por la lista de la guía)

#'''
#Variable que indica si se encontró la clave en la lista tal que:
#- Ban = False, la clave no esta en la lista
#- Ban = True, la clave esta en la lista
#'''
#ban = False

#num = 57  # Valor de prueba para buscar en la lista

# Imprima un mensaje donde se muestre el valor a buscar

# Ciclo que recorre la lista para buscar

    # Imprima el mensaje en el cual se muestre cada elemendo de la iteración

    # Verifique si la clave se encontró

#''' Imprima el mensaje en el cual se informe la posición
#en la que se encontró el número, o un mensaje indicando que no se encontró'''

# Imprima la cantidad de iteraciones que hizo el ciclo


#****************************** Salida esperada ***********************************#
#
#Número: 57
#
#Iteración: 0, L[0] = 2
#Iteración: 1, L[1] = 10
#Iteración: 2, L[2] = 20
#Iteración: 3, L[3] = 23
#Iteración: 4, L[4] = 41
#Iteración: 5, L[5] = 45
#Iteración: 6, L[6] = 57
#
#Numero encontrado en la posición 6
#
#Cantidad de iteraciones 7
#**********************************************************************************#
