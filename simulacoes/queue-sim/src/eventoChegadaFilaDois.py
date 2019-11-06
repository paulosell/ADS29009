from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaDois import EventoSaidaFilaDois
class EventoChegadaFilaDois(Event):
    
    def __init__(self,t):
      super().__init__(t)
      
    def processEvent(self, simulador):        
        if(len(simulador.queue_dois) > 0 and simulador.server_dois == False):
            nextEvent = simulador.queue_dois[0]            
            simulador.queue_dois.remove(simulador.queue_dois[0])      
            nextEvent.processEvent(simulador)
            simulador.queue_dois.append(self)
        else:
            if simulador.server_dois == True:
                simulador.queue_dois.append(self)
            else:
                simulador.server_dois = True
                saida = EventoSaidaFilaDois(simulador.simtime+simulador.servico_dois.exp())
                simulador.scheduleEvent(saida)
    
