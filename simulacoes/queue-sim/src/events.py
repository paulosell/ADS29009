from src.event import Event
from src.rng import prng

class Events(Event):
    
    def __init__(self,t, fila, tipo):
        self.time = t
        self.fila = fila
        self.tipo = tipo
        self.exp = prng.modo(modo='exp',seed=14511, lamb=0.1)
        

    def processEvent(self):
        chegada = Events(self.exp.exp(), 'eventos', 'chegada')
        saida  = Events(self.exp.exp(), 'eventos', 'saida')
        return chegada, saida
        
        
                
