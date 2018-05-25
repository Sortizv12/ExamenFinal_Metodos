# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sigma=10.
beta=2.67
rho=28.0

dt=0.01
n=int(5/dt)

x=np.zeros(n)
y=np.zeros(n)
z=np.zeros(n)
x[0]=1
y[0]=0
z[0]=0

i=1
while i<n:
    x[i]=dt*(sigma*(y[i-1]-x[i-1])) +x[i-1] 
    y[i]=dt*((rho*x[i-1])- y[i-1] - (x[i-1]*z[i-1])) + y[i-1]
    z[i]=dt*((-beta*z[i-1])+(x[i-1]*x[i-1])) + z[i-1]
    i+=1
print(x)
plt.plot(x,y)
plt.savefig('xy.png')
plt.close()
plt.plot(x,z)
plt.savefig('xz.png')








