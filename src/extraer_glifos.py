import cv2
import os

# Crear carpeta salida
output_dir = "glifos_extraidos"
os.makedirs(output_dir, exist_ok=True)

# Cargar imagen
img = cv2.imread("voynich_folio.jpg")

if img is None:
    print("No se pudo cargar imagen.")
    exit()

# Escala grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarización
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Detectar contornos
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contador = 0

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filtrar ruido
    if w > 10 and h > 10:

        # Recortar glifo
        glifo = img[y:y+h, x:x+w]

        # Guardar imagen
        filename = os.path.join(
            output_dir,
            f"glifo_{contador}.png"
        )

        cv2.imwrite(filename, glifo)

        contador += 1

print(f"Glifos guardados: {contador}")