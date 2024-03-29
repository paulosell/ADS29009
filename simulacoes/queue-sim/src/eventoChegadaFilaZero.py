from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaZero import EventoSaidaFilaZero

class EventoChegadaFilaZero(Event):
    
    def __init__(self,t,i):
        super().__init__(t,i)

        

    def processEvent(self, simulador): 
        if simulador.server_zero == True:
            simulador.queue_zero.append(self)
        
        else:
            simulador.server_zero = True
            time = simulador.simtime+simulador.servico_zero.exp()
            saida = EventoSaidaFilaZero(time,self.id)
            simulador.scheduleEvent(saida)
            simulador.fila_soma.append(time-self.time)
      

        
                
