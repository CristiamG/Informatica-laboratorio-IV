#****************Busqueda Lineal******************************************

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

#************************Busqueda Binaria************************************

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

#*********************Raices biseccion**********************************

def f(x):
    funcion = x**3 + 2*x**2 - 4*x + 3
    return funcion

iteracion = 0 # Número de veces que se repite el ciclo
a = -4 # Limite inferior
b = -3 # Limite superio
epsilon = 0.01 # Tolerancia

# Evaluación de la función en los limites
f1 = f(a)
f2 = f(b)
x = (b + a)/2.0 # punto medio del intervalo inicial

# Verificar si la raíz está en los limites, existen varias posibilidades:
if f1 == 0:
    print("La raiz es :" ,a)

elif f2 == 0:
    print("La raiz es :" ,b)

else:
    [a,b] # 3. Que la raíz se encuentre en el intervalo

while abs(f(x)) >= epsilon:
    iteracion += 1

    if f(a)*f(x)<0:  # Si f(a)*f(x) < 0 el límite superior se cambia por el punto medio
        b = x

    elif f(a)*f(x)>0:   # Por el contrario, si f(a)*f(x) > 0 el límite inferior se cambia por el punto medio
        a = x

    x = (b + a)/2.0

    print("El valor de la raiz es :" ,x)
    print("Numero de iteraciones :" ,iteracion)

#*********************************Raices_Exhaustivo***************************

def f(x):
    funcion = x**3 + 2*x**2 - 4*x + 3
    return funcion

iter = 0 # Número de veces que se repite el ciclo
a = -4 # Limite inferior
b = -3 # Limite superior
epsilon = 0.01
paso = 0.0001 # Tamaño de paso

# Inicialización de la variable que contendrá el valor de la raíz
x = a

while x < b:
    x += paso
    iter +=1
    print(x)

    if abs(f(x)) <= epsilon:
        print("No fue posible encontrar la raiz")

    else:
        x = round(x,2)
        print("las raices de," , f(x), "son" ,+x,-x)
        print("Numero de iteraciones" ,iter)
        break
#***********************impresion****************************************
print(' -----------------------------------')
print('| Algoritmo | iteraciones promedio |')
print(' -----------------------------------')
print('| lineal    |         ',n+1,'         |')
print('| Binaria   |         ',cont, '          |')
print('| Exahustivo|         ',iter, '          |')
print('| Bisección |         ',iteracion, '          |')
print(' -----------------------------------')
