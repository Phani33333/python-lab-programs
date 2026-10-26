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
    
Colors=['red','blue','green']
labels=['$X_1$','$X_2$','$X_3$']
origin=[0,0,0]
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
for i in range(len(ev1)):
    v=ev2[:,i]
    ax.quiver(origin[0],origin[1],origin[2],v[0],v[1],v[2],color=Colors[i],label=labels[i])
plt.xlim(-2,2)
plt.ylim(-2,2)
ax.set_zlim(-2,2)
plt.gca().set_aspect('equal')
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.title("Eigen values 3d")
plt.legend()
plt.show()
