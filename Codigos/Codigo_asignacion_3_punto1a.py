import csv
import numpy as np
import matplotlib.pyplot as plt

# Lee los datos del archivo CSV
with open('/home/xxxxx/Documentos/codigo/metodos/Asiganacion3/datosmasas.csv', mode='r') as file:
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

# Calculamos la masa total del sistema
tamaño = range(len(lista_masas_float))
masa = sum(lista_masas_float)  # siendo igual a 4627


# Calculamos el momento de inercia 1

momento_de_inercia_1 = 0
tamaño = range(len(lista_masas_float))
for i in tamaño:
    momento_de_inercia_1 += lista_masas_float[i] * (Lista_coordenadas_x_float[i]**2 + Lista_coordenadas_y_float[i]**2)

print("Momento de Inercia 1:", momento_de_inercia_1)
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

# Calcular el centro de masa
masa_total = sum(lista_masas_float)
centro_masa_x = np.sum([m * x for m, x in zip(lista_masas_float, Lista_coordenadas_x_float)]) / masa_total
centro_masa_y = np.sum([m * y for m, y in zip(lista_masas_float, Lista_coordenadas_y_float)]) / masa_total

print("Centro de Masa:")
print("X:", centro_masa_x)
print("Y:", centro_masa_y)

# Grafica los puntos de masa
plt.scatter(Lista_coordenadas_x_float, Lista_coordenadas_y_float, s=lista_masas_float, label='Masas')

# Grafica el centro de masa
plt.scatter(centro_masa_x, centro_masa_y, color='k', marker='x', s=100, label='Centro de Masa')

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
