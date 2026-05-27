import cv2
import matplotlib.pyplot as plt

# Ruta imagen
imagen_path = "voynich_folio.jpg"

# Cargar imagen
img = cv2.imread(imagen_path)

if img is None:
    print("No se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarización
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Mostrar resultados
plt.figure(figsize=(12,12))
plt.imshow(thresh, cmap='gray')
plt.title("Binarización Voynich")
plt.axis("off")
plt.show()

print("Procesamiento completado.")