#!/usr/bin/python3
"""module rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Args:
        matrix (int, int): n x n 2D matrix
    """
    n = len(matrix)
    matrix[:] = [[matrix[n - j - 1][i]
                  for j in range(n)] for i in range(n)]
