import matplotlib.pyplot as plt
import numpy as np
from numpy import mean, sqrt, square

def get_noise(n):
	return np.random.normal(size=(n))

def plot(Y, title=None, filename=None):
	plt.figure(figsize=(15,4))
	plt.plot(x, Y)
	if title != None:
		plt.title(title)
	if filename != None:
		plt.savefig('/Users/davidferris/Documents/Personal/Software/miscellaneous/{}'.format(filename))

def plot_multiple(X, title=None, filename=None):
	f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8, sharex=True, sharey=True, figsize=(15,8))
	
	axes = (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8)
	for i,a in enumerate(axes):
		a.plot(X[i])
		a.get_yaxis().set_visible(False)

	if title != None:
		ax1.set_title(title)
	if filename != None:
		plt.savefig('/Users/davidferris/Documents/Personal/Software/miscellaneous/report_prototypes/{}'.format(filename))

#Prep channel of X
n = 500
x = np.arange(n)
X = [ _ for _ in range(8) ]
X[0] = np.sin(2 * np.pi * 3 * x / n)*2+2.5
X[1] = np.sin(2 * np.pi * 3 * x / n)*2.2 +2.5
for i in range(2,8):
	X[i] = get_noise(n)
X = np.asarray(X)

plot_multiple(X, title='Simulated EMG Channels', filename='channels')

#Perform RMS
Y_rms = np.asarray([sqrt(abs(sum(t))) for t in X.T])

#Perform PCA
C = np.cov(X)
D,W = np.linalg.eigh(C)
X_projected = np.dot(X.T, W)
Y_pca = X_projected.T[-1]
if sum(Y_pca) < 0: 
	Y_pca*=-1
