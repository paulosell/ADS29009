from src.simuladorFilas import SimuladorFilas
from src.events import Events
from queue import PriorityQueue
from src.rng import prng
from src.eventoChegadaFilaZero import EventoChegadaFilaZero
from src.eventoChegadaFilaUm import EventoChegadaFilaUm


fila = PriorityQueue()
simulador = SimuladorFilas()
primeiroEvento = EventoChegadaFilaZero(0)
segundoEvento = EventoChegadaFilaUm(1.1)
fila.put((primeiroEvento.time,primeiroEvento))
fila.put((segundoEvento.time, segundoEvento))
simulador.scheduleEvent(primeiroEvento)
simulador.run()
