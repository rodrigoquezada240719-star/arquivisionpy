# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:56:54 2026

@author: Rodri
"""

import cv2
import numpy as np

def preprocess(img):
    # 1. Escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Suavizado (reduce ruido)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    # 3. Umbralización (limpia fondo)
    _, th = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

    # 4. Operación morfológica (CLOSE)
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

    return morph

def rotate_image(img, angle):
    import cv2

    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated = cv2.warpAffine(
        img,
        matrix,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REPLICATE
    )

    return rotated