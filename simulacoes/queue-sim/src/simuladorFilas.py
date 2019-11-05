from src.simulador import Simulador
from src.rng import prng
from src.events import Events

class SimuladorFilas(Simulador):

    def __init__(self):
        super().__init__()     
        self.u = prng.modo(modo='lcm', seed=116432, a = 1103515245, c = 12345, m = 2147483648)
        self.exp = prng.modo(modo='exp',seed=14511, lamb=0.1)
        self.eventos = 0
        self.queue_um_events   = []
        self.queue_dois_events = []
        self.queue_um = []
        self.queue_dois = []
        self.queue_zero = []
        self.server_zero = False
        self.server_um = False
        self.server_dois= False
    
    def gera_eventos(self):
        eventos_gerados = 0
        while eventos_gerados < 100000:           
            self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'chegada'))           
            self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'saida'))
            eventos_gerados = eventos_gerados + 1
        self.scheduleEvent(Events(0, 'eventos', 'chegada'))
                    

   def run(self):
        while not self.eventQueue:            
            nextEvent = self.eventQueue.get()
            self.simtime += nextEvent.t
            nextEvent.processEvent(simulador)