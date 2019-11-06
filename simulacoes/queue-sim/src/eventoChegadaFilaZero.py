from src.event import Event
from src.rng import prng
from src.eventoSaidaFilaZero import EventoSaidaFilaZero

class EventoChegadaFilaZero(Event):
    
    def __init__(self,t):
        super().__init__(t)

    def processEvent(self, simulador):   
        if(len(simulador.queue_zero) > 0 and simulador.server_zero == False):
            nextEvent = simulador.queue_zero[0]            
            simulador.queue_zero.remove(simulador.queue_zero[0])      
            nextEvent.processEvent(simulador)
            simulador.queue_zero.append(self)
        else:
            if simulador.server_zero == True:
                simulador.queue_zero.append(self)
            else:
                simulador.server_zero = True
                time = simulador.simtime+simulador.servico_zero.exp()
                
                saida = EventoSaidaFilaZero(time)
                simulador.scheduleEvent(saida)
    
        
                
