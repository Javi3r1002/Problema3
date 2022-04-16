import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
import sklearn.cluster as cluster
import pyclustertend
import random
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth
from sklearn.preprocessing import StandardScaler, PowerTransformer
from kneed import KneeLocator
import pandas as pd
from sklearn.cluster import KMeans


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

n = 100000
a = np.linspace(0, 4, n)
L = 1
yo = 1000

Y = []
itera = 100
By = []
Bx = []
G =[]
Temp = []
FgF =[]
Fg=[]
Co = []
Gg = []

def F(a, x):
	if a > 0:
		return np.log(abs(a*L-2*a*x))
	else:
		return 0

def union(Vg, Va):
	return list((zip(Vg, Va)))

def D(A, G):
	return pd.DataFrame(list((zip(A, G))), columns = ['alpha', 'Exponente'])

def Fei(Vg, Va):
	U = union(Vg, Va)
	#print(U)
	Fg2 = []
	Gg2 = []

	for i in range(len(U)-1):
		#if round(U[i][0], 2) == 0:
			#Fg.append(U[i][1])
		if i > 0:
			if (U[i][1] <= 3.5):
				#if (U[i][0] >= -.001) & (U[i][0] <= .001) & (U[i-1][0] <= 0):
				if(round(U[i][0], 1) == 0) & (U[i+1][0] <= 0) & (U[i-1][0] <=0):
					Fg.append(U[i][1])
					Gg.append(U[i][0])
			elif (U[i][1] <= 3.56790):
				#if (U[i][0] >= -.001) & (U[i][0] <= .001) & (U[i-1][0] <= 0):
				#if (round(U[i][0], 3) == 0):
				if(round(U[i][0], 2) == 0) & (U[i+1][0] <= 0) & (U[i-1][0] <=0):
					Fg2.append(U[i][1])
					Gg2.append(U[i][0])
	Fg.pop(0)

	X = D(Fg, Gg)
	X2 = D(Fg2, Gg2)
	km = cluster.KMeans(n_clusters=3).fit(X)
	centroides = km.cluster_centers_
	#print(centroides)
	C = sorted(centroides[:, 0])
	print(C)
	for i in C:
		Co.append(i)

	km1 = cluster.KMeans(n_clusters=2).fit(X2)
	centroides = km1.cluster_centers_
	#print(centroides)
	C2 = sorted(centroides[:, 0])
	print(C2)
	for i in C2:
		Co.append(i)


	for j in range(len(Co)-2):
		print('Constante: ', ((Co[j+1]-Co[j])/(Co[j+2]-Co[j+1])))

np.random.seed(250)
for i in a:
	yo = np.random.random()
	Y.clear()
	for j in range(itera):
		y =(i*yo*(L-yo))
		#print(y)
		yo = y
		Temp.append(F(i, y))
	G.append(np.mean(Temp))
	#G.append(F(i,y))
	Temp.clear()
	Y.append(yo)
	for g in Y:
		By.append(g)
		Bx.append(i)

	#plt.plot(X, Y)

ax1.plot(Bx, By, ',k', alpha = .25)
G = np.array(G)
#a.pop(0)
ax2.plot(a[G < 0], G[G<0], ',k', alpha = .25)
ax2.axhline(0, color='k', lw=.5, alpha=.5)
ax2.plot(a[G >= 0], G[G>=0], ',r', alpha = .25)

Fei(G, a)
for h in Co:
	ax2.axvline(h, color='k', lw=.25, alpha=.25)
print(Co)
plt.show()
	