#!/usr/bin/python3
"""a module for the pascal triangle"""


def pascal_triangle(n):
    """this function returns a pascal tringle"""
    triangle = []

    if (n <= 0):
        return triangle
    for i in range(1, n + 1):
        arr = []
        for j in range(1, i + 1):
            # corner conditions
            if i <= 2 or j == i or j == 1:
                val = 1
            else:
                val = triangle[i - 2][j - 1] + triangle[i - 2][j - 2]
            arr.append(val)
        triangle.append(arr)
    return triangle
