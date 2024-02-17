import math as mt
def riemman(f,a, b, n):
    h = (b-a)/n
    acum=0
    x=a
    for i in range(n):
        acum = acum + f(x)*h
        x = x + h
    return acum

def trapecio(f,a,b,n):
    h = (b-a)/n
    acum = 0
    x=a
    for i in range(n):
        acum = acum +((f(x)+f(x+h))*h/2)
        x = x + h
    return acum

if __name__ == "__main__":
    f = lambda x: x*(((x**2)+1)**0.5)
    print(riemman(f,1,2,4))
    print(trapecio(f,1,2,4))