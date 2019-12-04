from src.event import Event
from src.rng import prng


class EventoSaidaFilaUm(Event):

    def __init__(self,t,i):
       super().__init__(t,i) 

    def processEvent(self, simulador):
        print('processando saida 1')  
        if len(simulador.queue_um) > 0:      
            simulador.queue_um.remove(simulador.queue_um[0]) 
            time = simulador.simtime+simulador.servico_um.exp()
            saida = EventoSaidaFilaUm(time,self.id)
            simulador.scheduleEvent(saida)    
        else:            
            simulador.server_um = False
        
        
        


    
        
                
