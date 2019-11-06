from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaUm import EventoSaidaFilaUm
class EventoChegadaFilaUm(Event):
    
    def __init__(self,t):
        super().__init__(t)     
        
    def processEvent(self, simulador):        
        if(len(simulador.queue_um) > 0 and simulador.server_um == False):
            nextEvent = simulador.queue_um[0]            
            simulador.queue_um.remove(simulador.queue_um[0])      
            nextEvent.processEvent(simulador)
            simulador.queue_um.append(self)
        else:
            if simulador.server_um == True:
                simulador.queue_um.append(self)
            else:
                simulador.server_um = True
                time = simulador.simtime+simulador.servico_um.exp()
                saida = EventoSaidaFilaUm(time)
                simulador.scheduleEvent(saida)
                
        
        

    
        
        
                
