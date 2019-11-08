from src.event import Event
from src.rng import prng


class EventoSaidaFilaDois(Event):

    def __init__(self,t):
        super().__init__(t) 

    def processEvent(self, simulador):  
        print(len(simulador.queue_dois))
        if(len(simulador.queue_dois) > 0):
            simulador.server_dois = True           
            simulador.queue_dois.pop()
            simulador.eventos2 = simulador.eventos2+1    
        else:      
            simulador.eventos2 = simulador.eventos2+1    
            simulador.server_dois = False
        