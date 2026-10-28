import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""

    a = np.array(a)
    b = np.array(b)

    dot = np.dot(a,b)
    mag_a = 0
    mag_b = 0
    for x in a:
        mag_a += x**2
    mag_a = np.sqrt(mag_a)

    for x in b:
        mag_b += x**2
    mag_b = np.sqrt(mag_b)

    res = dot/(mag_a*mag_b)

    return res
