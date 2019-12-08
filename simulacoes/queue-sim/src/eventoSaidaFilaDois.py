from src.event import Event
from src.rng import prng


class EventoSaidaFilaDois(Event):

    def __init__(self,t,i):
        super().__init__(t,i) 

    def processEvent(self, simulador):  
        if(len(simulador.queue_dois) > 0):        
            e = simulador.queue_dois[0]
            simulador.queue_dois.remove(simulador.queue_dois[0])
            time = simulador.simtime+simulador.servico_dois.exp()
            saida = EventoSaidaFilaDois(time,self.id)
            simulador.scheduleEvent(saida)
            simulador.fila_soma_dois.append(time-e.time)
        else:       
            simulador.server_dois = False
        
       
      