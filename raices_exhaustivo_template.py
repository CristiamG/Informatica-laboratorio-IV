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
