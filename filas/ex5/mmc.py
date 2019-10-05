'''
O servidor Web do IFSC-SJ (com un ́unico processador) tem a
capacidade de processar em media 60 paginas por minuto. Ele
esta recebendo em media 30 requisicoes por minuto.
Pergunta-se: em termos de tempo de espera mdio no sistema e
na fila, seria melhor manter esta configuracao ou (i) dividir as
requisis entre tres servidores (cada um com 10 requisicoes
por minuto) e com poder de processar 20 requisioes ou (ii) usar
um ́unico servidor com tres processadores servindo a fila ́unica
(cada um servindo a 20 paginas por minuto).
'''

import math


lamb = [30, 10,30]
mi = [60,20,20]
c = [1,1,3]


p0 = []
EWq = []
EW = []


for i in range(3):  ## loop geral
    pi = 0
    ro = lamb[i]/(c[i]*mi[i])
    for k in range(c[i]):
        pi = pi + (c[i]*ro)**k/math.factorial(k)
    pi = 1/(pi + ( (c[i]*ro)**c[i] / (math.factorial(c[i]) * (1-ro))) )
    p0.append(round(pi,2))

    ENq = pi * (((ro * c[i])**(c[i]+1)/c[i]) / (math.factorial(c[i]) * ((1-ro)**2)))
    ewq = ENq/lamb[i]
    ew = ewq + (1/mi[i])

    EWq.append(round(ewq,2))
    EW.append(round(ew,2))

print()

print('Tempos no sistema: {}'.format(EW))
print('Tempos na fila: {}'.format(EWq))


