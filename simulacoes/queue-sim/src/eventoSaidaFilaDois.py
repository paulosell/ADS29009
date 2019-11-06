from src.event import Event
from src.rng import prng


class EventoSaidaFilaDois(Event):

    def __init__(self,t):
        super().__init__(t) 

    def processEvent(self, simulador):  
        simulador.eventos2 = simulador.eventos2+1      
        simulador.server_dois = False

    
        