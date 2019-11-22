from src.event import Event
from src.rng import prng
from src.eventoChegadaFilaUm import EventoChegadaFilaUm
from src.eventoChegadaFilaDois import EventoChegadaFilaDois


class EventoSaidaFilaZero(Event):
    
    def __init__(self,t,i):
        super().__init__(t,i)
    
    def processEvent(self, simulador):  
        num = simulador.u.ulcm()                   
        if num <= 0.5:
            rdn =  simulador.chegada_um.exp()
            chegadaFilaUm = EventoChegadaFilaUm(simulador.simtime+rdn,self.id)                       
            simulador.scheduleEvent(chegadaFilaUm)
            simulador.eventos1 = simulador.eventos1 + 1
        elif num > 0.5 and num <= 0.8:
            rdn =  simulador.chegada_dois.exp()            
            chegadaFilaDois = EventoChegadaFilaDois(simulador.simtime+rdn,self.id)                       
            simulador.scheduleEvent(chegadaFilaDois)
            simulador.eventos2 = simulador.eventos2 + 1
        else: 
            pass
        
        if(len(simulador.queue_zero) > 0):  
           simulador.queue_zero.pop(0)
        else:
            simulador.server_zero = False
            
        simulador.eventos = simulador.eventos+1
        from src.eventoChegadaFilaZero import EventoChegadaFilaZero
        rdn =  simulador.chegada_zero.exp()
        chegadaFilaZero = EventoChegadaFilaZero(simulador.simtime+rdn,simulador.eventos)                       
        simulador.scheduleEvent(chegadaFilaZero)
    
                
