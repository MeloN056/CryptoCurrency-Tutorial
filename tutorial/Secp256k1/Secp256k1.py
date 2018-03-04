"""
Python 3.5.4 :: Anaconda, Inc
楕円曲線暗号Secp256k1について
y^2 = x^3 + 7 mod 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1
"""

import math
import numpy as np
from matplotlib import pyplot as plt

mod = 17

xlist = []
ylist = []

for x in range(1,mod+1):
    for y in range(1,mod+1):
        if (((x**3 + 7 - y**2) % mod) == 0):
            xlist.append(x)
            ylist.append(y)


plt.plot(xlist, ylist, ".")

plt.title('Secp256k1 Graph (p = 17)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
