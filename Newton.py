import numpy as np

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

def Newton(f,df,x0,error1,error2):
    x = x0
    while abs(f(x))>error1 or abs(x-x0)>error2:
        x0 = x
        x = x - f(x)/df(x)
    return x

Newton(f,df,2,10**(-4),10**(-5))

# Pour une version plus robuste:
# * Mettre itération max 
# * Vérifier dérivée non nulle