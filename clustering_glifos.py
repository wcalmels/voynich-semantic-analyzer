import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carpeta glifos
input_dir = "glifos_extraidos"

# Cargar imágenes
imagenes = []
nombres = []

for archivo in os.listdir(input_dir):

    ruta = os.path.join(input_dir, archivo)

    img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

    if img is None:
        continue

    # Redimensionar uniforme
    img = cv2.resize(img, (32,32))

    # Vectorizar
    vector = img.flatten()

    imagenes.append(vector)
    nombres.append(archivo)

# Convertir a numpy
X = np.array(imagenes)

# Número de clusters
k = 5

# KMeans
kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X)

# Mostrar resultados
for i in range(k):

    print(f"\nCLUSTER {i}")
    print("-" * 30)

    indices = np.where(labels == i)[0]

    for idx in indices[:10]:
        print(nombres[idx])

print("\nClustering completado.")