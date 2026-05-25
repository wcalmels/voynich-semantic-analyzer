

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

input_dir = "glifos_extraidos"

imagenes = []
imagenes_originales = []

for archivo in os.listdir(input_dir):

	ruta = os.path.join(input_dir, archivo)

	img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

	if img is None:
		continue

	img_resize = cv2.resize(img, (32,32))

	imagenes.append(img_resize.flatten())
	imagenes_originales.append(img)

X = np.array(imagenes)

k = 5

kmeans = KMeans(
	n_clusters=k,
	random_state=42,
	n_init=10
)

labels = kmeans.fit_predict(X)

for cluster_id in range(k):

	plt.figure(figsize=(12,6))

	indices = np.where(labels == cluster_id)[0]

	for i, idx in enumerate(indices[:10]):

		plt.subplot(2,5,i+1)

		plt.imshow(imagenes_originales[idx], cmap='gray')

		plt.axis("off")

	plt.suptitle(f"Cluster {cluster_id}")

	plt.show()

print("Visualización completada.")

