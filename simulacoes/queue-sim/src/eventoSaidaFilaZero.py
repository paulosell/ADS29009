from src.event import Event
from src.rng import prng
from src.eventoChegadaFilaUm import EventoChegadaFilaUm
from src.eventoChegadaFilaDois import EventoChegadaFilaDois

class EventoSaidaFilaZero(Event):
    
    def __init__(self,t):
        super().__init__(t)
    
    def processEvent(self, simulador):       
        simulador.server_zero = False   
        num = simulador.u.ulcm()            
        if num <= 0.5:                
            chegadaFilaUm = EventoChegadaFilaUm(simulador.simtime+simulador.exp.exp())                       
            simulador.scheduleEvent((chegadaFilaUm.time, chegadaFilaUm))
        elif num > 0.5 and num <= 0.8:
            chegadaFilaDois = EventoChegadaFilaDois(simulador.simtime+simulador.exp.exp())                       
            simulador.scheduleEvent((chegadaFilaDois.time, chegadaFilaDois))
        else: 
            pass
    
    
                
