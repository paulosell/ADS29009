from src.simuladorFilas import SimuladorFilas
from src.events import Events
from queue import PriorityQueue
from src.rng import prng


exp = prng.modo(modo='exp',seed=141, lamb=0.3)
fila = PriorityQueue()


simulador = SimuladorFilas()

simulador.gera_eventos()
simulador.run()

