import sympy as sp

x=sp.symbols('x')
y=sp.Function('y')

lhs=sp.simplify(input("Enter lhs of DE:"))
rhs=sp.simplify(input("Enter lhs of DE:"))

ode=sp.Eq(lhs,rhs)

x0=float(input("Enter x0:"))
y0=float(input("Enter y0:"))
y0d=float(input("Enter y0d:"))

initialcds={y(x0):y0,sp.diff(y(x),x).subs(x,x0):y0d}
sol=sp.dsolve(ode,y(x),ics=initialcds)

print('General Solution:y(x)=',sol.rhs)
