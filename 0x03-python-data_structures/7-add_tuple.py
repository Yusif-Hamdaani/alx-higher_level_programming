#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Get the first two elements of each tuple, or use 0 if they don't exist
    a = tuple_a[0] if len(tuple_a) >= 1 else 0
    b = tuple_a[1] if len(tuple_a) >= 2 else 0
    c = tuple_b[0] if len(tuple_b) >= 1 else 0
    d = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    # Compute the sum of the corresponding elements and return a new tuple
    return (a + c, b + d)
