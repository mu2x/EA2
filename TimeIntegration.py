# Euler Methods

def Euler(t,y0,f):
    n = len(t); dt = t[1]-t[0]; y = np.zeros(n); y[0]=y0;
    for i in range(n-1):
        y[i+1] = y[i] + dt * f(t[i],y[i])
    return y
