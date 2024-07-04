import numpy as np
import pandas as pd
from numpy import linalg as LA

"""def read_file(file_path):
    data = pd.read_excel(file_path)
    columnCOL = data['Data Source']
    data_frame = pd.DataFrame(columnCOL)
    row_COL_index = data_frame.index[data_frame['Data Source'] == 'Colombia'].tolist()[0]
    #Recuperar todos los datos de la fila row_COL
    data_all = pd.DataFrame(data)
    row_COL = data_all.iloc[row_COL_index]

    return row_COL

path = 'data\DefensaCO.xls'
print(read_file(path))
"""

#Normalizados

data_defensa: 'x1'= [3027922793,3264438192,3347522602,3278369503,4056896991,4914190182,5326664238,6775762767,9051130502,9033202673,10422054494,10306578506,11706271913,12503812627,11845950895,9127165375,8675980823,10018029818,10134719591,10167547856,9554131505]
data_health: 'x2' = [134.2853699,138.0442352,131.783844,129.3348694,159.1937103,209.2530212,239.3891144,309.0366516,378.1841126,383.4328308,452.1530151,501.2650757,546.5491333,579.9136963,586.6782227,468.5885315,447.2358093,495.2969971,517.1584473,522.5492554,477.2748108]
data_Education: 'x3' = [62.75518671,63.12793039,63.5182468,63.9223608,64.34171087,64.77318956,65.21735679,65.66845388,66.11137526,66.54207187,66.95213025,67.33191677,67.6764903,67.98938664,68.26257483,68.49477145,68.71255108,68.96950644,69.24974869,69.46792817,69.60532764]
data_Tech: 'x4' = [5695900.024,3183080.017,5101630.615,7557583.13,8725411.621,11285508.06,13071194.09,32690171.88,54104212.89,48221626.95,72661187.5,83017587.89,138714017.6,141459716.8,116382418,101196816.4,99122533.2,134001691.4,143866519.5,127065630.9,123030173.8]

print(len(data_defensa), len(data_health), len(data_Education), len(data_Tech))


data_defensa = np.asarray(data_defensa)
data_health = np.asarray(data_health)
data_Education = np.asarray(data_Education)
data_Tech = np.asarray(data_Tech)

#Aprovechamos la simetría de la matriz de varianza-covarianza

cov12:'x_1, x_2' = np.cov(data_defensa, data_health)[0,1]
cov13: 'x_1, x_3' = np.cov(data_defensa, data_Education)[0,1]
cov14: 'x_1, x_4' = np.cov(data_defensa, data_Tech)[0,1]
cov23: 'x_2, x_3' = np.cov(data_health, data_Education)[0,1]
cov24: 'x_2, x_4' = np.cov(data_health, data_Tech)[0,1]
cov34: 'x_3, x_4' = np.cov(data_Education, data_Tech)[0,1]

#print(cov12, cov13, cov14, cov23, cov24, data34)

#Varianza de la diagonal

cov11:'x_1' = np.cov(data_defensa)
cov22:'x_2' = np.cov(data_health)
cov33:'x_3' = np.cov(data_Education)
cov44: 'x_4' = np.cov(data_Tech)

# Construir la matriz de covarianza
cov_matrix = np.array([[cov11, cov12, cov13, cov14],
                       [cov12, cov22, cov23, cov24],
                       [cov13, cov23, cov33, cov34],
                       [cov14, cov24, cov34, cov44]])

#print("Matriz de covarianza:")
#print(cov_matrix)


# Crear una matriz de correlación
correlation_matrix = np.corrcoef([data_defensa, data_health, data_Education, data_Tech])
#print(correlation_matrix)

#Hallar los autovalores
autovalores = LA.eigvals(cov_matrix)
# Convertir los autovalores en una lista de NumPy
autovalores_lista = autovalores
print(autovalores_lista)

#Hallar los autovectores
autovectores = LA.eig(cov_matrix)
print(autovectores)
