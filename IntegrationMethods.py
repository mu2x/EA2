# Integration Methods
# Trapezoidal composite (multiple applications) 
def Trap(f,x): 
    n = len(x)-1; s = 0; 
    for i in range(n):
        f2 = f(x[i+1]); f1=f(x[i]); 
        s = s + (x[i+1]-x[i]) * ( f1+ f2 )/2
        #print(s) 
    return s

# Simpson 1/3 composite (multiple applications) 
# I = h/3 * (f0 + 4*f1 + f2);
def Sim13(f,x):
    h = x[1] - x[0]; n = len(x)-1; I = 0; napp=int(n/2);
    for i in range(napp):
        j=2*i
        I = I + (h/3) * (f(x[0+j]) + 4*f(x[1+j]) + f(x[2+j]))
    return I

# Simpson 3/8 composite (multiple applications) 
# I = 3*h/8 * (f0 + 3*f1 + 3*f2 + f3); 
def Sim38(f,x):
    h = x[1] - x[0]; n = len(x)-1; I = 0; napp=int(n/3);
    for i in range(napp):
        j=3*i
        I = I + (3*h/8) * (f(x[0+j]) + 3*f(x[1+j]) + 3*f(x[2+j]) + f(x[3+j]))
    return I
