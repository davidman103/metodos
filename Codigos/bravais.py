#Programa para generar distintas confiuracciones de redes de Bravais
import numpy as np
import matplotlib.pyplot as plt

def plot_vector(ax, origin, vector, color):
    ax.quiver(*origin, *vector, color=color, scale=1, scale_units='xy', angles='xy')

alfa = float(input("Ingrese el ángulo de lo vectores de la 'base' que va a definir: "))
alfarads = (alfa/180)*np.pi
#generación de vectores base 

e1 = np.array([1,0]) #fijamos el vector unitario i de la base canónica de r2
e2 = np.array([round(np.cos(alfarads),2), round(np.sin(alfarads),2)]) #Este vector dependera del ángulo proporcionado
print(e2)
puntos = []
for i in range(-10,11): #Variamos 2 parametros enteros, para hacer la distinta generación de los puntos. 
    for j in range(-10,11):
        punto = np.dot(e1,j) + np.dot(e2,i) #Generamos las combinaciones lineales
        puntos.append(punto)


fig, ax = plt.subplots()
for punto in puntos: 
    ax.plot(punto[0], punto[1], 'bo')

#Se dibujan los vectores de la base en forma de flechas
ax.annotate('', xy=e1, xytext=(0, 0), arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('', xy=e2, xytext=(0, 0), arrowprops=dict(facecolor='green', shrink=0.05))

ax.set_aspect('equal')
plt.grid(True)
plt.show()
