# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:56:55 2026

@author: Rodri
"""

import cv2
import numpy as np

def detect_lines(edges):
    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi/180,
        threshold=120,
        minLineLength=80,
        maxLineGap=50
    )
    return lines