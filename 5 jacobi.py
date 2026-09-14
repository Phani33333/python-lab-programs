import matplotlib.pyplot as plt

tol = 1e-6
max_iter = 100
x, y, z = 0, 0, 0
xnew, ynew, znew = [], [], []

a1, b1, c1, d1 = map(float,input("Enter a1,b1,c1,d1").split())
a2, b2, c2, d2 = map(float,input("Enter a2,b2,c2,d2").split())
a3, b3, c3, d3 = map(float,input("Enter a3,b3,c3,d3").split())

if abs(a1) > abs(b1) + abs(c1) and abs(b2) > abs(a2) + abs(c2) and abs(c3) > abs(a3) + abs(b3):
    print("System is diagonally dominant")
    for i in range(max_iter):
        x1 = (d1 - b1*y - c1*z) / a1
        y1 = (d2 - a2*x - c2*z) / b2
        z1 = (d3 - a3*x - b3*y) / c3

        xnew.append(x1)
        ynew.append(y1)
        znew.append(z1)

        print(f'Iteration {i+1}: x={x:0.6f}, y={y:0.6f}, z={z:0.6f}')

        if abs(x1-x) < tol and abs(y1-y) < tol and abs(z1-z) < tol:
            print('Desired solution reached')
            print(f'Iteration {i+1}: x={x:0.6f}, y={y:0.6f}, z={z:0.6f}')
            break
        else:
            x, y, z = x1, y1, z1
else:
    print("System is not diagonally dominant")

plt.figure()
plt.plot(xnew,marker='*',label='x')
plt.plot(ynew,marker='o',label='y')
plt.plot(znew,marker='+',label='z')
plt.legend()
plt.show()
