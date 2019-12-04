from src.event import Event
from src.rng import prng


class EventoSaidaFilaDois(Event):

    def __init__(self,t,i):
        super().__init__(t,i) 

    def processEvent(self, simulador):  
        print('processando saida 2')
        if(len(simulador.queue_dois) > 0):        
            simulador.queue_dois.remove(simulador.queue_dois[0])
            saida = EventoSaidaFilaDois(simulador.simtime+simulador.servico_dois.exp(),self.id)
            simulador.scheduleEvent(saida)
        else:       
            simulador.server_dois = False
        
        