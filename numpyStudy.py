import numpy as np

x = np.arange(24).reshape(3, 4, 2)
print(x)

s = x[:, 1:3]
s[:] = 10
# print(x)

# print(x.ravel())
