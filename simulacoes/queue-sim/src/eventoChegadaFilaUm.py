from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaUm import EventoSaidaFilaUm
class EventoChegadaFilaUm(Event):
    
    def __init__(self,t,i):
        super().__init__(t,i)     
        
    def processEvent(self, simulador):     
        if simulador.server_um == True:
            simulador.queue_um.append(self)   
        else:
            simulador.server_um = True
            time = simulador.simtime+simulador.servico_um.exp()
            saida = EventoSaidaFilaUm(time,self.id)
            simulador.scheduleEvent(saida)
            simulador.fila_soma_um.append(time-self.time)
       
                    
        
        

    
        
        
                
