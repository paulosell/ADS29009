import numpy as np
import random

def PMFdata(states, Pi):
	u = np.random()
    


N = 100000

initial_state = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

P = np.matrix([[0.2, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.2, 0.3, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.1, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.7, 0.0, 0.0, 0.0],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.8],
			  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2],
		 	  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
			  [0.2, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2]])

states = np.arange(10)+1
state = 1
a = 0
for i in range(N):
	dado = round(random.uniform(0,1), 1)
	print((dado))
	if state == 1:
		print(state)
	elif state == 2:
		print(state)
	elif state == 3:
		print(state)
	elif state == 4:
		print(state)

	elif state == 5:
		print(state)	
	elif state == 6:
		print(state)	
	elif state == 7:
		print(state)
	elif state == 8:
		print(state)
	elif state == 9:
		print(state)	
	elif state == 10:
		print(state)	
	

print(np.random()) 
