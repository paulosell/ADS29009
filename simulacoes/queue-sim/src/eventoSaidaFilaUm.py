from src.event import Event
from src.rng import prng


class EventoSaidaFilaUm(Event):
    
    def __init__(self,t):
       super().__init__(t) 

    def processEvent(self, simulador):    
        simulador.eventos1 = simulador.eventos1+1    
        simulador.server_um = False



    
        
                
