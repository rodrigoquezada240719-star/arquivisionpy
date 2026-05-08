# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:42:08 2026

@author: Rodri
"""

import cv2

def draw_results(img, lines=None, corners=None, intersections=None):
    out = img.copy()

    if lines is not None:
        for l in lines:
            x1,y1,x2,y2 = l[0]
            cv2.line(out,(x1,y1),(x2,y2),(0,255,0),2)

    if corners is not None:
        for c in corners:
            x,y = c.ravel()
            cv2.circle(out,(x,y),4,(0,0,255),-1)

    if intersections is not None:
        for x,y in intersections:
            cv2.circle(out,(x,y),4,(255,0,0),-1)

    return out