# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:56:55 2026

@author: Rodri
"""

import cv2
import numpy as np
from scipy import signal

def detect_edges_canny(img):
    return cv2.Canny(img, 100, 200)

# EXTRA (lo que tú ya haces)
def derivative_x(img):
    Hx = np.array([[0.5, 0, -0.5]])
    return signal.convolve(img, Hx, mode="same")

def derivative_y(img):
    Hy = np.array([[0.5], [0], [-0.5]])
    return signal.convolve(img, Hy, mode="same")