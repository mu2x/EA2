def div_avg_sqrt(a,x0,n):
    x=x0; 
    for i in range(n):
        x = (x + a/x)/2
        print([i,x])
    return x
