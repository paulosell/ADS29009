import math

'''

Qual a vaz ̃ao e qual a taxa de descarte de pacotes?
Quanto tempo em m ́edia um pacote fica no roteador?
Quantos pacotes em m ́edia ficam no roteador?
Qual a probabilidade de um pacote que chega, encontrar a fila
vazia?
Calcule estes desempenhos da fila usando a fun ̧c ̃ao
qsmm1k
do
octave. Mostre as sa ́ıdas.
Quantos processadores deveriam ser colocados para reduzir o
tempo de um pacote no sistema para abaixo de 1
s
? Use a
fun ̧c ̃ao
qsmmmk
para encontrar esta respost
'''
lamb = 50
mi = 20
k = 100

ro = lamb/mi

p0 = (1-ro) / (1-(ro**(k+1)))

pk = (ro**k)*p0
vazao = lamb * (1-pk)
perdas = lamb*pk

EN = (ro/(1-ro)) - (((k+1)*(ro**(k+1)))/(1-(ro**(k+1))))
EW = EN/(lamb*(1-pk))
ENw = EN - ((ro*(1-(ro**k)))/(1-(ro**(k+1))))

print("A vazão desta fila é {} pacotes por segundo".format(round(vazao,2)))
print("A taxa de perdas dessa fila é de {} pacotes por segundo".format(round(perdas,2)))
print("O tempo médio do sistema é de  {} segundos".format(round(EW,2)))
print("Em média {} pacotes ficam no roteador".format(round(ENw,2)))
print("A probabilidade de ter 0 pacotes no sistema é de {}".format(round(p0,5)))
