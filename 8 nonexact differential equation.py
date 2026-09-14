import sympy as sp

def isform_yfxy(expr,x,y):
    u=sp.Symbol('u')
    fxy=sp.simplify(expr/y)
    result=sp.simplify(fxy.subs(x,u/y))
    return not (result.has(x) or result.has(y))

def isform_xgxy(expr,x,y):
    u=sp.Symbol('u')
    gxy=sp.simplify(expr/x)
    result=sp.simplify(gxy.subs(x,u/y))
    return not (result.has(x) or result.has(y))

x,y=sp.symbols('x y')

M=sp.simplify(input('Enter M(x,y):'))
N=sp.simplify(input('Enter N(x,y):'))

Mdeg=sp.homogeneous_order(M,x,y)
Ndeg=sp.homogeneous_order(N,x,y)

dMdy=sp.simplify(sp.diff(M,y))
dNdx=sp.simplify(sp.diff(N,x))

fx=sp.simplify((dMdy-dNdx)/N)
gy=sp.simplify((dNdx-dMdy)/M)

if dMdy==dNdx:
    print('Equation is Exact')
    F=sp.integrate(M,x)
    g=sp.integrate(N-sp.diff(F,y),y)
    print('Solution:',F+g,'=c')
else:
    print('Equation is non-Exact')
    if Mdeg is not None and Ndeg is not None:
        print('Equation is Homogeneous')
        mu=sp.simplify(1/(M*x+N*y))
    elif (isform_yfxy(M,x,y) is not None and isform_xgxy(N,x,y) is not None):
          print('Equation is of the form yf(xy)+xg(xy)')
          mu=sp.simplify(1/(M*x-N*y))
    elif not fx.has(y):
        mu=sp.simplify(sp.exp(sp.integrate(fx,x)))
    elif not gy.has(x):
        mu=sp.simplify(sp.exp(sp.integrate(gy,y)))
    else:
        print('These methods are not applicable')
        exit()
    print("I.F=",mu)
    M1=M*mu
    N1=N*mu

    F=sp.simplify(sp.integrate(M1,x))
    g=sp.simplify(sp.integrate(N1-sp.diff(F,y),y))
    print('Solution:',sp.simplify(F+g),'=c')
