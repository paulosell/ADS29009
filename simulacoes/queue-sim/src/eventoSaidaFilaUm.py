from src.event import Event
from src.rng import prng


class EventoSaidaFilaUm(Event):
    
    def __init__(self,t):
       super().__init__(t) 

    def processEvent(self, simulador):  
        if len(simulador.queue_um) > 0:         
            simulador.queue_um.pop()     
            simulador.eventos1 = simulador.eventos1+1    
        else:      
            simulador.eventos1 = simulador.eventos1+1    
            simulador.server_um = False
        print(len(simulador.queue_um))


    
        
                
