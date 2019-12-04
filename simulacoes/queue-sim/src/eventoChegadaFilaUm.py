from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaUm import EventoSaidaFilaUm
class EventoChegadaFilaUm(Event):
    
    def __init__(self,t,i):
        super().__init__(t,i)     
        
    def processEvent(self, simulador):     
        print('processando chegada 1')
        if simulador.server_um == True:
            simulador.queue_um.append(self.time)   
        else:
            simulador.server_um = True
            time = simulador.simtime+simulador.servico_um.exp()
            saida = EventoSaidaFilaUm(time,self.id)
            simulador.scheduleEvent(saida)
       
                    
        
        

    
        
        
                
