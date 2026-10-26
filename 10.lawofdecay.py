import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


t,N0,k=sp.symbols('t N0 k')
N=sp.Function('N')

ode=sp.Eq(sp.diff(N(t),t),-k*(N(t)))
sol=sp.dsolve(ode,N(t))
print('General Solution:',sol)

Particularsol=sp.dsolve(ode,N(t),ics={N(0):N0})
print('Particular Solution:N(t)=',Particularsol.rhs)

god=input("growth or decay(1 or 2)")
N0=float(input('Enter Initial Count N0:'))
t=float(input('Enter time t='))
N=float(input('Enter Count N='))
if(god=="2"):
    k=(-1/t)*np.log((N)/(N0))

    print('Constant k=',k)
    N=float(input('Enter count N='))
    t=(-1/k)*np.log((N)/(N0))
    print('time t=',t)
    t=float(input('Enter time t='))
    N=(N0)*np.exp(-k*t)
    print('count T=',N)


    t=np.arange(0,100,0.1)
    N=(N0)*np.exp(-k*t)
elif(god=="1"):
    k=(1/t)*np.log((N)/(N0))

    print('Constant k=',k)
    N=float(input('Enter count N='))
    t=(1/k)*np.log((N)/(N0))
    print('time t=',t)
    t=float(input('Enter time t='))
    N=(N0)*np.exp(k*t)
    print('count N=',N)


    t=np.arange(0,100,0.1)
    N=(N0)*np.exp(k*t)
else:
    print("choose 1 or 2")

plt.figure()
plt.plot(t,N)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Newtons Law of decay")
plt.show()
