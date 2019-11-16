from src.event import Event
from src.rng import prng


class EventoSaidaFilaDois(Event):

    def __init__(self,t):
        super().__init__(t) 

    def processEvent(self, simulador):  
        if(len(simulador.queue_dois) > 0):        
            simulador.queue_dois.remove(simulador.queue_dois[0])
        else:       
            simulador.server_dois = False
        
        