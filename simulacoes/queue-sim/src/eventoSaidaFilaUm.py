from src.event import Event
from src.rng import prng


class EventoSaidaFilaUm(Event):

    def __init__(self,t):
       super().__init__(t) 

    def processEvent(self, simulador):  
        if len(simulador.queue_um) > 0:      
            simulador.queue_um.remove(simulador.queue_um[0])     
        else:            
            simulador.server_um = False
        
        
        


    
        
                
