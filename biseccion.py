import math as mt
f = lambda x: mt.e**x - 3*(x)**2

# parametros del ejercicio
err_indx= 0.04
intervalo= (0,1)
number_iter= 6 
def biseccion(f,intervalo, err, number_iter):
    a= intervalo[0]
    b= intervalo[1]
    err_a= 100.0
    iterations= 0
    m_act=0.0
    m_previa=0.0
    while iterations< number_iter and err_a>err:
        m_act= m_previa
        m_previa= (a + b)/2
        if f(m_act)*f(b) <0:
           a = m_act
        else:
           b= m_act
        
        if iterations >1 :
           err_a= abs((m_act-m_previa)/m_act)

        iterations+=1
    
    return (m_act,err_a, iterations)

results= biseccion(f,intervalo, err_indx, number_iter)

print("El punto aproximado es ", results[0], " con un margen de error de ", results[1], 'alcanzado en ', results[2], 'iteraciones')
if __name__== "Main":
   pass

 