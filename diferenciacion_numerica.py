import math as mt
def derivada(f,h=0.02):
    def W(x):
        return (f(x+h)-f(x))/h
    return W

if __name__ =="__main__":
    fx = lambda x: (mt.e**x)*(mt.cos(x))
    dfx= derivada(fx)
    aprox = dfx(1)
    print (aprox)
