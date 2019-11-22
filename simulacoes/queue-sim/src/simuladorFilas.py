from src.simulador import Simulador
from src.rng import prng

class SimuladorFilas(Simulador):

    def __init__(self):
        super().__init__()     
        self.u = prng.modo(modo='lcm', seed=5560, a = 1103515245, c = 12345, m = 2147483648)
        self.chegada_zero = prng.modo(modo='exp',seed=0, lamb=0.1)
        self.chegada_um = prng.modo(modo='exp',seed=1, lamb=0.2)
        self.chegada_dois = prng.modo(modo='exp',seed=2, lamb=0.3)
        self.servico_zero = prng.modo(modo='exp',seed=3, lamb=0.7)
        self.servico_um = prng.modo(modo='exp',seed=4, lamb=0.8)
        self.servico_dois = prng.modo(modo='exp',seed=5, lamb=0.9)        
        self.queue_um = []
        self.queue_dois = []
        self.queue_zero = []
        self.server_zero = False
        self.server_um = False
        self.server_dois= False
        self.eventos = 0
        self.eventos1 = 0
        self.eventos2 = 0 
        

    def run(self):
        while self.eventos  < 1000:
            nextEvent = self.eventQueue.get()[1]
            self.simtime = (nextEvent.time - self.simtime) + self.simtime
            nextEvent.processEvent(self)
        
        print(self.eventos)
        print(self.eventos1)
        print(self.eventos2)
      
     
            
 
