def integracion(f,a, b, n):
    h = (b-a)/n
    acum=0
    x=a
    for i in range(n):
        acum = acum +f(x)*h
        x = x + h
    return acum

if __name__ == "__main__":
    f = lambda x: x*(((x**2)+1)**0.5)
    print(integracion(f,0,1,10000))