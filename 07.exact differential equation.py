import sympy as sp
import numpy as np

x,y = sp.symbols('x y')

M=sp.simplify(input('Enter M(x,y)'))
N=sp.simplify(input('Enter N(x,y)'))

dMdy=sp.simplify(sp.diff(M,y))
dNdx=sp.simplify(sp.diff(N,x))

if dMdy==dNdx :
    print("Equation is exact")
    F=sp.integrate(M,x)
    g=sp.integrate(N-sp.diff(F,y),y)
    print("solution:",F+g,"= c")
else:
    print("Equation is non exact")
