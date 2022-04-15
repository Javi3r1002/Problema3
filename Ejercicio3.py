import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
from random import randrange

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

def F(a, x):
	if a > 0:
		return np.log(abs(a*L-2*a*x))
	else:
		return 0

def union(Vg, Va):
	return list((zip(Vg, Va)))

def Fei(Vg, Va):
	U = union(Vg, Va)
	#print(U)

	for i in range(len(U)-1):
		#if round(U[i][0], 2) == 0:
			#Fg.append(U[i][1])
		if i > 0:
			if (U[i-1][0] < 0) & (U[i+1][0] > 0):
				Fg.append(U[i][1])
	Fg.pop(0)
	#print(Fg)
	T = []
	for i in range(len(Fg)):
		print(T)
		if i > 0:
			if round(Fg[i]-T[-1], 1) == 0:
				T.append(Fg[i])
			else:
				FgF.append(np.mean(T))
				T.clear()
				print('Aqui')
				T.append(Fg[i])
		else:
			T.append(Fg[i])

	
	for j in range(len(FgF)-2):
		print('Constante: ', ((FgF[j+1]-FgF[j])/(FgF[j+2]-FgF[j+1])))




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
for h in FgF:
	ax2.axvline(h, color='k', lw=.25, alpha=.25)
print(FgF)
plt.show()
	