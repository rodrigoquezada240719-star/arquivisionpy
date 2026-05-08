# -*- coding: utf-8 -*-
"""
Ejemplo de uso de la librería ArquiVisionPy

Este archivo permite usar la librería instalada para detectar líneas,
esquinas e intersecciones en una imagen de plano arquitectónico.

El usuario solo debe modificar:
    - ruta_img
    - ruta_salida
"""

import cv2
import matplotlib.pyplot as plt
import arquivisionpy as av


print("==============================================")
print(" USO DE LA LIBRERÍA ARQUIVISIONPY")
print(" Detección de líneas, esquinas e intersecciones")
print("==============================================\n")

print("Este programa analiza una imagen de un plano arquitectónico.")
print("El sistema aplica preprocesamiento, detección de bordes,")
print("detección de líneas, detección de esquinas e intersecciones.\n")


# ---------------------------------------------------------
# RUTAS DE ACCESO
# ---------------------------------------------------------

# Colocar aquí la ruta de acceso de la imagen que se desea analizar
# Ejemplo:
# ruta_img = r"C:\Users\Rodri\OneDrive\Escritorio\plano_prueba.png"
ruta_img = "Ruta de acceso de la imagen"

# Colocar aquí la ruta donde se desea guardar la imagen procesada
# Ejemplo:
# ruta_salida = r"C:\Users\Rodri\OneDrive\Escritorio\resultado.jpg"
ruta_salida = "Ruta de acceso donde se guardará el resultado"


print("1. Cargando imagen de entrada...")
print("   Ruta de imagen:", ruta_img)

img = cv2.imread(ruta_img)

if img is None:
    raise FileNotFoundError(
        "No se encontró la imagen. Revisa la ruta de acceso, el nombre y la extensión."
    )

print("   Imagen cargada correctamente.\n")


print("2. Aplicando transformación afín...")
print("   Función utilizada: rotate_image()")
print("   Descripción: permite corregir inclinaciones mediante rotación.")

img = av.rotate_image(img, 0)

print("   Transformación aplicada correctamente.\n")


print("3. Aplicando preprocesamiento...")
print("   Función utilizada: preprocess()")
print("   Descripción:")
print("   - Convierte la imagen a escala de grises.")
print("   - Aplica filtrado espacial para reducir ruido.")
print("   - Aplica umbralización.")
print("   - Aplica operación morfológica para mejorar continuidad de líneas.")

gray = av.preprocess(img)

print("   Preprocesamiento terminado correctamente.\n")


print("4. Detectando bordes...")
print("   Función utilizada: detect_edges_canny()")
print("   Descripción: detecta bordes mediante el algoritmo Canny.")

edges = av.detect_edges_canny(gray)

print("   Bordes detectados correctamente.\n")


print("5. Detectando líneas...")
print("   Función utilizada: detect_lines()")
print("   Descripción: utiliza la Transformada de Hough para detectar segmentos rectos.")

lines = av.detect_lines(edges)

if lines is None:
    total_lines = 0
else:
    total_lines = len(lines)

print("   Líneas detectadas:", total_lines)
print("   Detección de líneas terminada.\n")


print("6. Detectando esquinas...")
print("   Función utilizada: detect_corners()")
print("   Descripción: identifica puntos con cambios fuertes de intensidad.")

corners = av.detect_corners(gray)

if corners is None:
    total_corners = 0
else:
    total_corners = len(corners)

print("   Esquinas detectadas:", total_corners)
print("   Detección de esquinas terminada.\n")


print("7. Calculando intersecciones...")
print("   Función utilizada: detect_intersections()")
print("   Descripción: calcula puntos de cruce entre las líneas detectadas.")

intersections = av.detect_intersections(lines)

print("   Intersecciones detectadas:", len(intersections))
print("   Cálculo de intersecciones terminado.\n")


print("8. Dibujando resultados...")
print("   Función utilizada: draw_results()")
print("   Descripción:")
print("   - Líneas detectadas: color verde.")
print("   - Esquinas detectadas: color rojo.")
print("   - Intersecciones detectadas: color azul.")

result = av.draw_results(img, lines, corners, intersections)

print("   Resultados dibujados correctamente.\n")


print("9. Guardando resultado final...")

guardado = cv2.imwrite(ruta_salida, result)

if not guardado:
    raise ValueError(
        "No se pudo guardar la imagen. Revisa la ruta de salida y la extensión del archivo."
    )

print("   Resultado guardado en:", ruta_salida)
print("   Imagen guardada correctamente.\n")


print("10. Mostrando resultados gráficos...")
print("   Se mostrarán tres imágenes:")
print("   - Imagen original")
print("   - Bordes Canny")
print("   - Resultado final con líneas, esquinas e intersecciones\n")


plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap="gray")
plt.title("Bordes Canny")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Resultado")
plt.axis("off")

plt.tight_layout()
plt.show()


print("==============================================")
print(" PROCESO TERMINADO CORRECTAMENTE")
print("==============================================")
print("El programa generó:")
print("- Explicación en la terminal de Spyder")
print("- Visualización de la imagen original")
print("- Visualización de bordes Canny")
print("- Resultado final marcado")
print("- Imagen guardada en la ruta indicada")