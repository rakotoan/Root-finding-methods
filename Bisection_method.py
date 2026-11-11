import numpy as np

def f(x):
    return x**2 - 2

def dichotomie(f,a,b,tol):

    if f(a)*f(b)<0:
        return False

    else:

        while (b-a) > tol:  

            m = (a+b)/2
            
            if f(m)==0:
                return m

            elif f(m)*f(b)>0:
                b = m

            else:
                a = m 

        return (a+b)/2
