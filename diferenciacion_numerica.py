def derivada(f,h=0.02):
    def W(x):
        return (f(x+h)-f(x))/h
    return W


