#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    
    Args:
        n (int): the number of rows in the Pascal's triangle
    
    Returns:
        list of lists of int: the Pascal's triangle of n
    """
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
