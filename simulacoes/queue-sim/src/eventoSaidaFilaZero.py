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
            chegadaFilaUm = EventoChegadaFilaUm(simulador.simtime,self.id)                       
            simulador.scheduleEvent(chegadaFilaUm)
            simulador.eventos1 = simulador.eventos1 + 1
        elif num > 0.5 and num <= 0.8:
            rdn =  simulador.chegada_dois.exp()            
            chegadaFilaDois = EventoChegadaFilaDois(simulador.simtime,self.id)                       
            simulador.scheduleEvent(chegadaFilaDois)
            simulador.eventos2 = simulador.eventos2 + 1
        else: 
            pass
        
        if(len(simulador.queue_zero) > 0):  
            e = simulador.queue_zero.pop(0)
            time = simulador.simtime+simulador.servico_zero.exp()
            saida = EventoSaidaFilaZero(time,e.id)
            simulador.scheduleEvent(saida)  
            simulador.fila_soma.append(time-e.time)
    
        else:
            simulador.server_zero = False
            
        simulador.eventos = simulador.eventos+1
        from src.eventoChegadaFilaZero import EventoChegadaFilaZero
        rdn =  simulador.chegada_zero.exp()
        chegadaFilaZero = EventoChegadaFilaZero(simulador.simtime+rdn,simulador.eventos)                       
        simulador.scheduleEvent(chegadaFilaZero)
""" 
        for ids in simulador.fila_tempos_zero:
            if ids[0] == self.id:
                dif = self.time - ids[1] 
                print(dif)
                simulador.fila_soma.append(dif) """
    
                
