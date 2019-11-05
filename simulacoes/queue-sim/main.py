from src.simuladorFilas import SimuladorFilas
from src.events import Events
from queue import PriorityQueue
from src.rng import prng
from src.eventoChegadaFilaZero import EventoChegadaFilaZero

exp = prng.modo(modo='exp',seed=141, lamb=0.3)
fila = PriorityQueue()


simulador = SimuladorFilas()
primeiroEvento = EventoChegadaFilaZero(0)
simulador.scheduleEvent((primeiroEvento.time, primeiroEvento))
simulador.run()

