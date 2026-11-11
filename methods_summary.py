import numpy as np


def Newton(f,df,x0,error1,error2):
    x = x0
    while abs(f(x))>error1 or abs(x-x0)>error2:
        x0 = x
        x = x - f(x)/df(x)
    return x


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
