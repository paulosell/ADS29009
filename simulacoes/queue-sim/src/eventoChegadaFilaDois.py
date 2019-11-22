from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaDois import EventoSaidaFilaDois
class EventoChegadaFilaDois(Event):
    
    def __init__(self,t,i):
      super().__init__(t,i)
      
    def processEvent(self, simulador):    
        if simulador.server_dois == True:
            simulador.queue_dois.append(self.time)
        else:
            simulador.server_dois = True
        saida = EventoSaidaFilaDois(simulador.simtime+simulador.servico_dois.exp(),self.id)
        simulador.scheduleEvent(saida)

