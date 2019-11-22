from src.simuladorFilas import SimuladorFilas
from queue import PriorityQueue
from src.rng import prng
from src.eventoChegadaFilaZero import EventoChegadaFilaZero
from src.eventoChegadaFilaUm import EventoChegadaFilaUm

simulador = SimuladorFilas()
primeiroEvento = EventoChegadaFilaZero(0,simulador.eventos)
simulador.scheduleEvent(primeiroEvento)
simulador.run()
