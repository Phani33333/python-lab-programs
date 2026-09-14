import numpy as np
import matplotlib.pyplot as plt
s=input("enter the maatrix")
A=np.asmatrix(s)
print(A)
print("order of the matrix",np.shape(A))
if A.shape[0]==A.shape[1]:
    print("given matrix is a square matrix")
    ev1,ev2=np.linalg.eig(A)
    print("eigen values are:\n",ev1)
    print("eigen vectors are:\n",ev2)
else:
    print("given matrix is not square matrix")

Colors=['red','blue']
labels=['$X_1$','$X_2$']
origin=[0,0]
plt.axhline(0)
plt.axvline(0)
for i in range(len(ev1)):
  v=ev2[:,i]
  plt.quiver(origin[0],origin[1],v[0],v[1],angles='xy',scale_units='xy',scale=1,color=Colors[i],label=labels[i])
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.gca().set_aspect('equal')
plt.title("eigen values 2d")
plt.legend()
plt.show()
