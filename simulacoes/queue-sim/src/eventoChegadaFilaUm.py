from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaUm import EventoSaidaFilaUm
class EventoChegadaFilaUm(Event):
    
    def __init__(self,t):
        super().__init__(t)     
        
    def processEvent(self, simulador):     
        if simulador.server_um == True:
            simulador.queue_um.append(self)   
        else:
            simulador.server_um = True
            time = simulador.simtime+simulador.servico_um.exp()
            saida = EventoSaidaFilaUm(time)
            simulador.scheduleEvent(saida)
       
                    
        
        

    
        
        
                
