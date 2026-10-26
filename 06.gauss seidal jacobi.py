import numpy as np
import matplotlib.pyplot as plt
x, y, z = 0, 0, 0

x_new = []
y_new = []
z_new = []

tol = 1e-6
max_iter = 100

a1, b1, c1, d1 = map(float ,input("enter a1 ,b1,c1 , d1").split())
a2, b2, c2, d2 = map(float ,input("enter a2 ,b2,c2 , d2").split())
a3, b3, c3, d3 = map(float ,input("enter a3 ,b3,c3 , d3").split())
if (abs(a1) > abs(b1) + abs(c1) and
    abs(b2) > abs(a2) + abs(c2) and
    abs(c3) > abs(a3) + abs(b3)):

    print("System is diagonally dominant.\n")

    for i in range(max_iter):
        x1 , y1 ,z1 = x , y,z

        x = (d1 - b1 * y - c1 * z) / a1
        y = (d2 - a2 * x - c2 * z) / b2
        z = (d3 - a3 * x - b3 * y) / c3

        x_new.append(x)
        y_new.append(y)
        z_new.append(z)

        print(f"Iteration {i+1}: x = {x1:.6f}, y = {y1:.6f}, z = {z1:.6f}")

    
        if (abs(x1 - x) < tol and
            abs(y1 - y) < tol and
            abs(z1 - z) < tol):

            print("\nDesired solution reached!")     
            break

    print("Final Solution for the system")
    print(f"x = {x1:.6f}")
    print(f"y = {y1:.6f}")
    print(f"z = {z1:.6f}")
else:
    print("System is not diagonally dominant.")
plt.figure()
plt.semilogy(x_new ,marker ="*" , label = "x")
plt.semilogy(y_new ,marker ="o" , label = "y")
plt.semilogy(z_new ,marker ="+" , label = "z")
plt.show()
