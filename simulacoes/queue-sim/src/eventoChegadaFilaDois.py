from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaDois import EventoSaidaFilaDois
class EventoChegadaFilaDois(Event):
    
    def __init__(self,t,i):
      super().__init__(t,i)
      
    def processEvent(self, simulador):    
        if simulador.server_dois == True:
            simulador.queue_dois.append(self)
        else:
            simulador.server_dois = True
            time = simulador.simtime+simulador.servico_dois.exp()
            saida = EventoSaidaFilaDois(time,self.id)
            simulador.scheduleEvent(saida)
            simulador.fila_soma_dois.append(time-self.time)

