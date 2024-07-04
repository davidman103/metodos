import csv
import numpy as np
import matplotlib.pyplot as plt

# Lee los datos del archivo CSV
with open('/home/mrdeivy07/Documentos/codigo/metodos/Asiganacion3/datosmasas.csv', mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    columns = zip(*rows)
    columns = [list(column) for column in columns]

# Extrae las masas y coordenadas
Lista_masas = columns[1]
Lista_coordenadas_x = columns[2]
Lista_coordenadas_y = columns[3]

# Convierte los valores a flotantes
Lista_coordenadas_x_float = [float(valor) for valor in Lista_coordenadas_x]
Lista_coordenadas_y_float = [float(valor) for valor in Lista_coordenadas_y]
lista_masas_float = [float(valor) for valor in Lista_masas]

# Calcula el tensor de inercia
Ixx = np.sum(np.fromiter((m * (y**2) for m, y in zip(lista_masas_float, Lista_coordenadas_y_float)), dtype=float))
Iyy = np.sum(np.fromiter((m * (x**2) for m, x in zip(lista_masas_float, Lista_coordenadas_x_float)), dtype=float))
Ixy = -np.sum(np.fromiter((m * x * y for m, x, y in zip(lista_masas_float, Lista_coordenadas_x_float, Lista_coordenadas_y_float)), dtype=float))
Iyx = Ixy

tensor_inercia = np.array([[Ixx, Ixy], [Iyx, Iyy]])

# Calcula los valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(tensor_inercia)

print("Tensor de Inercia:")
print(tensor_inercia)
print("\nVector Propio:")
print(vectores_propios[0])
print("\nVector Propio:")
print(vectores_propios[1])
print("\nValores Propios:")
print(valores_propios)

# Grafica los puntos de masa
plt.scatter(Lista_coordenadas_x_float, Lista_coordenadas_y_float, s=lista_masas_float, label='Masas')

# Grafica los vectores propios
for i in range(len(valores_propios)):
    plt.quiver(0, 0, vectores_propios[0, i], vectores_propios[1, i], scale=5, color='r', label=f'Vector Propio {i+1}')

plt.axis('equal')
plt.grid(True)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Sistema de Partículas y Vectores Propios')
plt.legend()
plt.show()
