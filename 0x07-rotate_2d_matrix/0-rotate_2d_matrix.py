#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates an n by n matrix
    clockwise 90 degrees
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for row in matrix:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
