# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:56:55 2026

@author: Rodri
"""

import cv2
import numpy as np



def detect_corners(img):
    corners = cv2.goodFeaturesToTrack(
        img,
        maxCorners=50,
        qualityLevel=0.05,
        minDistance=20
    )

    if corners is not None:
        corners = np.int32(corners)

    return corners