# Rootfinding methods

def bisec(xL,xU,niter,f):
    for iter in range(niter): 
        xR = (xL + xU)/2
        if(f(xR)*f(xL)>0):
            xL = xR
        else:
            xU = xR
        #print([xL,xR,xU])
    return xR

def False_Position(xL,xU,niter,f):
    for iter in range(niter): 
        xR = xU - f(xU)*(xL-xU)/(f(xL) - f(xU)) # xR = (xL + xU)/2
        if(f(xR)*f(xL)>0):
            xL = xR
        else:
            xU = xR
        #print([xL,xR,xU])
    return xR
def NR(xi,niter,f,df):
    for i in range(niter):
        xi = xi - f(xi)/df(xi) # x(i+1) = xi - f(xi)/df(xi)
    return xi
def Secant(xi,xip1,niter,f):
    for i in range(niter):
        df = (f(xip1) - f(xi))/(xip1-xi)
        xi = xi - f(xi)/df # x(i+1) = xi - f(xi)/df(xi)
    return xi
