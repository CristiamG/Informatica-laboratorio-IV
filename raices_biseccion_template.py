# Función
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
if abs(f1) <= epsilon:
    print("La raiz es :" ,a)

elif abs(f2) <= epsilon:
    print("La raiz es :" ,b)

else:
     # 3. Que la raíz se encuentre en el intervalo

    while abs(f(x)) >= epsilon:
        iteracion += 1

        if f(a)*f(x)<0:  # Si f(a)*f(x) < 0 el límite superior se cambia por el punto medio
            b = x

        elif f(a)*f(x)>0:   # Por el contrario, si f(a)*f(x) > 0 el límite inferior se cambia por el punto medio
            a = x

        x = (b + a)/2.0

print("El valor de la raiz es :" ,x)
print("Numero de iteraciones :" ,iteracion)
