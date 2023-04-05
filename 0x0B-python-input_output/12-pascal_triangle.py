#!/usr/bin/python3
""" A function for Pascals triangle """


def pascal_triangle(n):
    """
    Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trio = triangles[-1]
        tmp = [1]
        for i in range(len(trio) - 1):
            tmp.append(trio[i] + trio[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
