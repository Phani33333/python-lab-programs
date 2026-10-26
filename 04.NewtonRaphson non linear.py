import numpy as np
import matplotlib.pyplot as plt

def newtonraphson(x0,tol=1e-10,max_iter=100):
    guess=[]
    funs=[]
    f=lambda x: np.sin(x)-1+x
    fd=lambda x: np.cos(x)+1
    if f(x0)==0:
        print("Invalid Initial condition")
        return None
    for i in range(max_iter):
        guess.append(x0)
        funs.append(abs(f(x0)))
        x1=x0-(f(x0)/fd(x0))
        if abs(f(x1))<tol:
            print("The desired root reached after",i+1,"iterations")
            return guess,funs,x0
        x0=x1
    print("The max iteration reached")
    return mids,funs,x0

x0=1
guess,funs,Root = newtonraphson(x0)
print("The approximate root is",Root)

plt.figure()
plt.plot(guess,marker='*',label='Approximated Roots')
plt.plot(funs,marker='o',label='functional values')
plt.legend()
plt.show()
