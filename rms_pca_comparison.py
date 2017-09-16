import matplotlib.pyplot as plt
import numpy as np
from numpy import mean, sqrt, square

def get_noise(n):
	return np.random.normal(size=(n))

#Prep channel of X
n = 10000
x = np.arange(n)
X = [ _ for _ in range(8) ]
X[0] = np.sin(2 * np.pi * 3 * x / n)*3+3
X[1] = np.sin(2 * np.pi * 3 * x / n)*4+4
for i in range(2,8):
	X[i] = get_noise(n)
X = np.asarray(X)

#Perform RMS
Y = np.asarray([sqrt(sum(t)) for t in X.T])

plt.plot(x, Y)
plt.savefig('/Users/davidferris/Documents/Personal/Software/miscellaneous/test')