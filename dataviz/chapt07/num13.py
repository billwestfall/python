import numpy as np

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

a = np.arange(6)
print("The array")
csum = np.cumsum(a)
print(csum)

csum[3:] = csum[3:] - csum[:-3]
print(csum)

a = np.arange(10)
print(moving_average(a, 4))
