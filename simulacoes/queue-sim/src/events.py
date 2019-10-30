from src.event import Event
from src.rng import prng

class Events(Event):
    
    def __init__(self,t, fila, tipo):
        self.time = t
        self.fila = fila
        self.tipo = tipo

    
    def criar_chegada(self,fila='eventos'):
        return Events(self.exp.exp(),fila, 'chegada')

    def criar_saida(self, fila='eventos'):
        return Events(self.exp.exp(), fila, 'saida')
    

    def processEvent(self,server):
        num = self.u.ulcm()
        if num < 0.5:
            return self.criar_chegada()
        else:
            return self.criar_saida()
        
                
