import cv2
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread("voynich_folio.jpg")

if img is None:
    print("No se pudo cargar la imagen.")
    exit()

# Escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarización
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Detectar contornos
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar rectángulos
resultado = img.copy()

contador = 0

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filtrar ruido pequeño
    if w > 10 and h > 10:
        cv2.rectangle(resultado, (x, y), (x+w, y+h), (0,255,0), 2)
        contador += 1

# Convertir BGR -> RGB
resultado_rgb = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)

# Mostrar resultado
plt.figure(figsize=(14,14))
plt.imshow(resultado_rgb)
plt.title(f"Glifos detectados: {contador}")
plt.axis("off")
plt.show()

print(f"Glifos detectados: {contador}")