import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    x = np.array(x)
    res = []
    norm = 0
    for i in x:
        norm += i**2
    if norm == 0:
        raise ValueError
    else:
        norm = np.sqrt(norm)
        for i in x:
            res.append(i/norm)
    return res
