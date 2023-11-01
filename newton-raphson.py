# Método de Newton-Raphson
# Ejemplo 1 (Burden ejemplo 1 p.51/pdf.61)
import math as m
import numpy as np

# INGRESO
fx  = lambda x: (m.e**(-x**2))-2*x+1
dfx = lambda x: -2*x*(m.e**(-x**2))-2

x0 = 2 #SERIA 0.80, pero partiendo desde 2 parece obtener una mayor precision
tolera = 0.001# seria 0.02 pero con esta se llega mas lejos 
def newton_raphson(fx, dfx, x0= 2, tolera= 0.001):
    # PROCEDIMIENTO
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        xi = xnuevo

    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n = len(tabla)
    
    #retorno una tupla con toda la informacion necesaria
    return (xi, tramo, tabla)

# SALIDA
def salida_newton_raphson(tupla):
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tupla[2])
    print('raiz en: ', tupla[0])
    print('con error de: ',tupla[1])

Z= newton_raphson(fx, dfx)
salida_newton_raphson(Z)