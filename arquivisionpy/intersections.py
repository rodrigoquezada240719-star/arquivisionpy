# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:40:54 2026

@author: Rodri
"""

# -*- coding: utf-8 -*-

def line_intersection(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

    if den == 0:
        return None

    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / den
    py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / den

    return int(px), int(py)


def detect_intersections(lines):
    points = []

    if lines is None:
        return points

    line_list = [line[0] for line in lines]

    for i in range(len(line_list)):
        for j in range(i + 1, len(line_list)):
            point = line_intersection(line_list[i], line_list[j])
            if point is not None:
                points.append(point)

    return points