import numpy as np
import random

def PMFdata(N,xi,pX):
    bi = []
    x = 0
    M = len(xi)
    for k in range(M-1):        
        if k == 0:
            bi.append(pX[k])
        else:
            bi.append(bi[k-1]+pX[k])  
    u = np.random.random()
    if (u > 0) and u <= bi[0]:
        x = xi[0]
    for k in range(1,M):
        if u > bi[k-1] and u <= bi[k]:
            x = xi[k]
    return x

N = 1000000
p0 = [1,0,0,0,0,0,0,0,0,0]

P = [[0.2, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.2, 0.3, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.1, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.7, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.8],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2],
		 	  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.2, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2]]

xi = [1,2,3,4,5,6,7,8,9,10,11]
XO = PMFdata(1,xi,p0)
i = XO 
X = []
X.append(PMFdata(1,xi,P[i]))
i = X[0]+1
for n in range(1,N-1):
    i = X[n-1]   -1 
    X.append(PMFdata(1,xi,P[i]))

estados = [0,0,0,0,0,0,0,0,0,0]

for estado in X:
    estados[estado-1] = estados[estado-1] + 1

estados = np.array(estados)
