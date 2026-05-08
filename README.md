# ArquiVisionPy

**ArquiVisionPy** es una librería en Python para detectar líneas, esquinas e intersecciones en imágenes de planos arquitectónicos o croquis digitalizados.

La librería utiliza técnicas de procesamiento digital de imágenes como conversión a escala de grises, filtrado espacial, umbralización, transformación afín, detección de bordes, Transformada de Hough, detección de esquinas y marcado visual de resultados.

---

## Instalación

Para instalar la librería directamente desde GitHub, usar:

```bash
pip install git+https://github.com/rodrigoquezada240719-star/arquivisionpy.git
```

También puede instalarse de forma local desde la carpeta del proyecto con:

```bash
pip install -e .
```

---

## Dependencias

La librería utiliza las siguientes dependencias:

opencv
numpy
matplotlib
scipy

Si se desea instalar manualmente las dependencias:


pip install -r requirements.txt


---

## Uso general de la librería

Una vez instalada, la librería se importa en Python o Spyder de la siguiente manera:


import arquivisionpy as av


Después de importarla, sus funciones pueden mandarse llamar usando el prefijo:


av.nombre_de_la_funcion()


Por ejemplo:


av.preprocess()
av.detect_edges_canny()
av.detect_lines()
av.detect_corners()
av.detect_intersections()
av.draw_results()


---

## Funciones principales de la librería

### `av.rotate_image(img, angle)`

Aplica una transformación afín de rotación a una imagen.

Esta función sirve para corregir posibles inclinaciones en planos escaneados o fotografiados. Recibe una imagen y un ángulo de rotación. Si el ángulo es `0`, la imagen se mantiene igual. Si el ángulo es positivo o negativo, la imagen gira según el valor indicado.

**Parámetros:**

- `img`: imagen de entrada.
- `angle`: ángulo de rotación.

**Resultado:**

- Devuelve la imagen rotada.

---

### `av.preprocess(img)`

Realiza el preprocesamiento principal de la imagen.

Esta función prepara la imagen antes de aplicar la detección de bordes, líneas y esquinas. Internamente convierte la imagen a escala de grises, aplica un filtro Gaussiano para reducir ruido, realiza umbralización y usa una operación morfológica para mejorar la continuidad de las líneas.

**Parámetros:**

- `img`: imagen de entrada.

**Resultado:**

- Devuelve una imagen procesada y lista para la detección de características.

---

### `av.to_gray(img)`

Convierte una imagen de color a escala de grises.

Esta función reduce la imagen a una sola capa de intensidad, lo cual facilita el procesamiento y disminuye la cantidad de información innecesaria cuando solo se desean detectar líneas, bordes o esquinas.

**Parámetros:**

- `img`: imagen de entrada.

**Resultado:**

- Devuelve la imagen en escala de grises.

---

### `av.blur(img)`

Aplica un filtro Gaussiano a la imagen.

Esta función permite suavizar la imagen y reducir ruido. Es útil para evitar que pequeñas variaciones o puntos aislados sean detectados como bordes falsos.

**Parámetros:**

- `img`: imagen de entrada.

**Resultado:**

- Devuelve la imagen suavizada.

---

### `av.improve_contrast(img)`

Mejora el contraste de una imagen en escala de grises.

Esta función utiliza ecualización de histograma para resaltar diferencias de intensidad en la imagen. Puede ser útil cuando el plano tiene bajo contraste o cuando las líneas no se distinguen claramente del fondo.

**Parámetros:**

- `img`: imagen en escala de grises.

**Resultado:**

- Devuelve una imagen con contraste mejorado.

---

### `av.detect_edges_canny(img)`

Detecta bordes mediante el algoritmo Canny.

Esta función identifica cambios fuertes de intensidad en la imagen. Los bordes detectados sirven como base para la detección de líneas mediante la Transformada de Hough.

**Parámetros:**

- `img`: imagen preprocesada.

**Resultado:**

- Devuelve una imagen binaria donde los bordes aparecen resaltados.

---

### `av.derivative_x(img)`

Calcula la derivada de la imagen en dirección X.

Esta función detecta cambios de intensidad en sentido horizontal. Sirve como apoyo teórico para comprender la detección de bordes, ya que los bordes se relacionan con variaciones fuertes de intensidad.

**Parámetros:**

- `img`: imagen de entrada.

**Resultado:**

- Devuelve la derivada de la imagen en dirección X.

---

### `av.derivative_y(img)`

Calcula la derivada de la imagen en dirección Y.

Esta función detecta cambios de intensidad en sentido vertical. Al igual que la derivada en X, sirve para analizar variaciones de intensidad dentro de la imagen.

**Parámetros:**

- `img`: imagen de entrada.

**Resultado:**

- Devuelve la derivada de la imagen en dirección Y.

---

### `av.detect_lines(edges)`

Detecta líneas rectas utilizando la Transformada de Hough probabilística.

Esta función trabaja a partir de una imagen de bordes y localiza segmentos rectos relevantes. En planos arquitectónicos, estas líneas pueden representar muros, divisiones internas, bordes de habitaciones o estructuras principales.

**Parámetros:**

- `edges`: imagen de bordes, normalmente obtenida con `av.detect_edges_canny()`.

**Resultado:**

- Devuelve las líneas detectadas en forma de coordenadas.

---

### `av.filter_lines(lines)`

Filtra las líneas detectadas para conservar principalmente líneas horizontales y verticales.

Esta función es útil en planos arquitectónicos, ya que muchos elementos estructurales, como muros y divisiones, suelen estar formados por líneas rectas horizontales o verticales.

**Parámetros:**

- `lines`: conjunto de líneas detectadas.

**Resultado:**

- Devuelve una lista de líneas filtradas.

---

### `av.detect_corners(img)`

Detecta esquinas o puntos relevantes dentro de la imagen.

Esta función identifica puntos donde existen cambios fuertes de intensidad en varias direcciones. En un plano arquitectónico, estos puntos pueden corresponder a uniones de muros, vértices de habitaciones, esquinas de puertas, ventanas o cambios de dirección.

**Parámetros:**

- `img`: imagen preprocesada.

**Resultado:**

- Devuelve las esquinas detectadas.

---

### `av.line_intersection(l1, l2)`

Calcula el punto de intersección entre dos líneas.

Cada línea debe estar representada por cuatro valores: punto inicial y punto final. Esta función aplica una fórmula matemática para obtener el punto donde ambas líneas se cruzan, siempre que no sean paralelas.

**Parámetros:**

- `l1`: primera línea.
- `l2`: segunda línea.

**Resultado:**

- Devuelve el punto de intersección en coordenadas `(x, y)`, o `None` si las líneas no se cruzan.

---

### `av.detect_intersections(lines)`

Detecta intersecciones entre las líneas encontradas.

Esta función toma todas las líneas detectadas y calcula los puntos donde se cruzan entre sí. También puede evitar guardar intersecciones demasiado cercanas para reducir puntos repetidos.

**Parámetros:**

- `lines`: conjunto de líneas detectadas.

**Resultado:**

- Devuelve una lista de puntos de intersección.

---

### `av.draw_results(img, lines, corners, intersections)`

Dibuja los resultados sobre la imagen original.

Esta función genera una imagen final donde se marcan visualmente las líneas, esquinas e intersecciones detectadas. Los resultados se representan con colores para facilitar su interpretación.

**Parámetros:**

- `img`: imagen original.
- `lines`: líneas detectadas.
- `corners`: esquinas detectadas.
- `intersections`: intersecciones detectadas.

**Resultado:**

- Devuelve una imagen final con los resultados marcados.

**Colores utilizados:**

- Líneas detectadas: verde.
- Esquinas detectadas: rojo.
- Intersecciones detectadas: azul.

---

## Flujo recomendado de uso

El flujo general recomendado para utilizar la librería es el siguiente:


1. Cargar la imagen de entrada.
2. Aplicar transformación afín si es necesario.
3. Aplicar preprocesamiento.
4. Detectar bordes con Canny.
5. Detectar líneas con Transformada de Hough.
6. Detectar esquinas.
7. Calcular intersecciones.
8. Dibujar los resultados.
9. Guardar o mostrar la imagen final.


---

## Archivo de ejemplo

El proyecto incluye un archivo de ejemplo en:


examples/demo_spyder.py


Este archivo permite probar la librería desde Spyder. El usuario solo debe modificar las rutas de acceso indicadas dentro del archivo:


ruta_img = r"Ruta de acceso de la imagen"
ruta_salida = r"Ruta de acceso donde se guardará el resultado"


---

## Resultados generados

La librería genera una imagen final donde se visualizan las características detectadas del plano arquitectónico.

La interpretación de los colores es:


Líneas detectadas: verde
Esquinas detectadas: rojo
Intersecciones detectadas: azul


---

## Estructura básica del proyecto


arquivisionpy/
├── __init__.py
├── preprocessing.py
├── edges.py
├── lines.py
├── corners.py
├── intersections.py
└── visualization.py

examples/
└── demo_spyder.py

README.md
pyproject.toml
requirements.txt


---

## Descripción general del funcionamiento

ArquiVisionPy trabaja mediante un pipeline de procesamiento digital de imágenes. Primero, la imagen del plano se prepara mediante preprocesamiento. Después se detectan bordes con Canny y, a partir de esos bordes, se detectan líneas usando la Transformada de Hough. También se identifican esquinas relevantes y se calculan intersecciones entre líneas. Finalmente, los resultados se dibujan sobre la imagen original para generar una salida visual clara.

---

Proyecto desarrollado para la detección de líneas, esquinas e intersecciones en planos arquitectónicos digitalizados.