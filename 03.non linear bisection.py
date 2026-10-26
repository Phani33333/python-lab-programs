import numpy as np
import matplotlib.pyplot as plt

def bisection(a,b,tol=1e-6,max_iter=100):
    mids=[]
    funs=[]
    f=lambda x: x-np.cos(x)
    if f(a)*f(b)>0:
        print("Invslid Interval")
        return None
    for i in range(max_iter):
        c=(a+b)/2
        mids.append(c)
        funs.append(abs(f(c)))
        if abs(f(c))<tol or (b-a)<tol:
            print("The desired root reached after",i+1,"iterations")
            return mids,funs,c
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    print("The max iteration reached")
    return mids,funs,(a+b)/2

a=0
b=1
mids,funs,Root = bisection(a,b)
print("The approximate root is",Root)

plt.figure()
plt.plot(mids,marker='*',label='mid points')
plt.plot(funs,marker='o',label='functional values')
plt.legend()
plt.show()
