import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.array([0, 0, 1])


points = []
for i in [-1,1]:  # Variamos 2 parametros enteros, para hacer la distinta generación de los puntos.
    for j in [-1,1]:
        for x in [-1,1]:
            punto = np.dot(e1, x) + np.dot(e2, j) + np.dot(e3, i)
            points.append(punto)
points.append(np.array([0,0,0]))
# Imprimir los puntos de forma ordenada
print(points)
points = np.array(points)
# Obtener las coordenadas x, y, z de los puntos
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Graficar los puntos en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar los puntos
ax.scatter(x, y, z, c='b', marker='o')

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
