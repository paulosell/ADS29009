from src.event import Event
from src.rng import prng

class Events(Event):
    
    def __init__(self,t, fila, tipo):
        self.time = t
        self.fila = fila
        self.tipo = tipo
        self.exp = prng.modo(modo='exp',seed=14511, lamb=0.1)
        
        
        

    def processEvent(self, simulador, num):        
        if(self.tipo == 'chegada'):
            if simulador.server_zero == True:
                simulador.queue_zero.append(self)
            else:
                simulador.server_zero = True
        else:
            simulador.eventos = simulador.eventos + 1
            simulador.server_zero = False
               
            if num <= 0.5:                
                chegada = Events(self.exp.exp(), 'fila1', 'chegada')
                saida = Events(self.exp.exp(), 'fila1', 'saida')
                simulador.queue_um_events.append(chegada)                  
                simulador.queue_um_events.append(saida)
            elif num > 0.5 and num <= 0.8:
                
                chegada = Events(self.exp.exp(), 'fila2', 'chegada')
                saida = Events(self.exp.exp(), 'fila2', 'saida')
                simulador.queue_dois_events.append(chegada)                  
                simulador.queue_dois_events.append(saida)
            else: 
                pass
        
        
                
