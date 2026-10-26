import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


t,Ts,T0,k=sp.symbols('t Ts T0 k')
T=sp.Function('T')

ode=sp.Eq(sp.diff(T(t),t),-k*(T(t)-Ts))
sol=sp.dsolve(ode,T(t))
print('General Solution:',sol)

Particularsol=sp.dsolve(ode,T(t),ics={T(0):T0})
print('Particular Solution:T(t)=',Particularsol.rhs)

Ts=float(input('Enter surrounding Temp Ts:'))
T0=float(input('Enter Initial Temp T0:'))
t=float(input('Enter time t='))
T=float(input('Enter Temp T='))

k=(-1/t)*np.log((T-Ts)/(T0-Ts))

print('Constant k=',k)
T=float(input('Enter Temp T='))
t=(-1/k)*np.log((T-Ts)/(T0-Ts))
print('time t=',t)
t=float(input('Enter time t='))
T=Ts+(T0-Ts)*np.exp(-k*t)
print('Temp T=',T)


t=np.arange(0,100,0.1)
T=Ts+(T0-Ts)*np.exp(-k*t)

plt.figure()
plt.plot(t,T)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Newtons Law of Cooling")
plt.show()
