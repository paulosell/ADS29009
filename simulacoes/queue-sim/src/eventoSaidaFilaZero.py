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
            print('foi pra fila 1')
            rdn =  simulador.chegada_um.exp()
            chegadaFilaUm = EventoChegadaFilaUm(simulador.simtime+rdn)                       
            simulador.scheduleEvent(chegadaFilaUm)
        elif num > 0.5 and num <= 0.8:
            print('foi pra fila 2')
            rdn =  simulador.chegada_dois.exp() 
            time =  simulador.simtime+simulador.chegada_dois.exp()            
            chegadaFilaDois = EventoChegadaFilaDois(simulador.simtime+rdn)                       
            simulador.scheduleEvent(chegadaFilaDois)
        else: 
            print('descarte')
            
        simulador.eventos = simulador.eventos+1
        from src.eventoChegadaFilaZero import EventoChegadaFilaZero
        rdn =  simulador.chegada_zero.exp()
        chegadaFilaZero = EventoChegadaFilaZero(simulador.simtime+rdn)                       
        simulador.scheduleEvent(chegadaFilaZero)
    
                
