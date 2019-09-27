'''
Ex1 - Lei de little
Calcular tempo médio que uma pessoa permanece no sistema com lambda = 5 e PMF(N) 
dada pelas variaveis N e pn
'''

N = [0,1,2,3,4,5]
pn = [1/10, 2/10, 5/10, 1/10, 1/20, 2/5]
lamb = 5
En = 0

for i in range (len(N)):
    En += N[i]*pn[i]



W = En/lamb
print("Tempo médio que uma pessoa permanece no sistema é de {} horas".format(W))

''' 
Computar o desempenho de uma fila de um posto de correio com um atendente onde chegam
λ = 13 pessoas por hora e a taxa de servico ́e μ de 17 pessoas por hora. 
Aproxime a uma fila MM1. Computar:
- a probabilidade de ter 0 pessoas no sistema;
- a probabilidade de ter 5 ou mais pessoas no sistema;
- n ́umero m ́edio de pessoas no sistema;
- tempo m ́edio de uma pessoa no sistema;
- a utilizaç̃ao do sistema.
-qual taxa de servi ̧co que poderia reduzir o tempo de espera medio no sistema pela metade?
'''

lamb = 13
mi = 17
p = lamb/mi

pi_0 = 1-p
pi_5 = 1 -((p**4) * pi_0) - ((p**3) * pi_0 ) - ((p**2) * pi_0) - ((p**1) * pi_0) - pi_0
En = lamb/(mi-lamb)
Er = En/lamb
U = p
mi_metade = (lamb/(Er/2*lamb)) + lamb

print()
print("Probabilidade de ter 0 pessoas na fila {}".format(round(pi_0,2)))
print("Probabilidade de ter 5 pessoas na fila {}".format(round(pi_5,2)))
print("Número médio de pessoas no sistema {}".format(En))
print("Tempo médio de uma pessoa no sistema {}".format(Er))
print("Utilização do sistema {}".format(round(U,2)))
print("Taxa de serviço que reduz o tempo de espera médio no sistema pela metade {}".format(mi_metade))
print()