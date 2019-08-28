'''
    27/08/2019
    Autor: Paulo Fylippe Sell
    Disciplina: ADS29009
                .>.>.> Cadeias de Markov <.<.<.
    Função PMFdata adaptada de Steven Kay Springer, 2006
    Função dtmcfpt adaptada do pacote queueing, do software Octave

'''

import numpy as np
import random

def dtmcfpt(X, dim_x, dim_y):
    matrix = np.zeros(shape=(dim_x,dim_y))
    for x in range(dim_x):  
        for y in range(dim_y):   
            counter = 0
            flag = 0      
            array = []     
            for state in X:
                if state - 1  == x and flag == 0:
                    counter = 0
                    flag = 1
                elif state - 1 == y and flag == 1:
                    counter = counter + 1      
                    array.append(counter)
                    counter = 0            
                    flag = 0
                elif state != y:
                    if flag == 1:
                        counter = counter + 1
            matrix[x][y] = sum(array)/len(array)
    return matrix

def PMFdata(N,xi,pX):
    bi = []
    x = 0
    M = len(xi)
    for k in range(M):        
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

N = 100000
p0 = [1,0,0,0,0,0,0,0,0,0]

P =           [[0.2, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.2, 0.3, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.1, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.7, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.8],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2],
		 	  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.2, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2]]

xi = [1,2,3,4,5,6,7,8,9,10]
XO = PMFdata(1,xi,p0)
i = XO 
X = []
X.append(PMFdata(1,xi,P[i]))
i = X[0]+1

for n in range(1,N-1):
    i = X[n-1]-1 
    X.append(PMFdata(1,xi,P[i]))

states = [0,0,0,0,0,0,0,0,0,0]

for state in X:
    states[state-1] = states[state-1] + 1

states = np.array(states)

matrix = dtmcfpt(X,10,10)

print('Vetor pi de estados em regime permanente:', np.round(states/N,3))
print()
print('Estado com maior ocupação: {}, com {} %  do tempo'.format(np.where(states==np.amax(states))[0], round(max(states)/N*100,3)))
print()
print('Estado com menor ocupação: {}, com {} %  do tempo'.format(np.where(states==np.amin(states))[0], round(min(states)/N*100,3)))
print()
print('Tempo médio de recorrência entre os estados 0 e 5 é de {} épocas'.format(round(matrix[0][5],3)))
print()

#print(np.round(matrix,3)) #descomente esta linha para imprimir a matriz de recorrencia

