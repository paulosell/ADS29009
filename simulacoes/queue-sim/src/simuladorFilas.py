from src.simulador import Simulador
from src.rng import prng
from src.events import Events

class SimuladorFilas(Simulador):

    def __init__(self):
        super().__init__()
        self.queue_zero = []
        self.queue_um_events   = []
        self.queue_dois_events = []
        self.queue_um = []
        self.queue_dois = []
        self.server_zero = False
        self.server_um = False
        self.server_dois = False
        self.u = prng.modo(modo='lcm', seed=116432, a = 1103515245, c = 12345, m = 2147483648)
        self.exp = prng.modo(modo='exp',seed=14511, lamb=0.1)
    
    def first_run(self):
        eventos_gerados = 0
        while eventos_gerados < 100000:
            num = self.u.ulcm()
            if num < 0.5:
                self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'chegada'))
            else:
                self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'saida'))
            eventos_gerados = eventos_gerados + 1
        
            

    def run(self):
        eventos = 0
        print(self.eventQueue.qsize())
        while not self.eventQueue.empty():
            if len(self.queue_zero) > 0 and self.server_zero == False:
                nextEvent = self.queue_zero[0]
                
                self.queue_zero.remove(self.queue_zero[0]) 
            else:
                nextEvent = self.eventQueue.get()[1]
                
            if(nextEvent.tipo == 'chegada'):
                if self.server_zero == True:
                    self.queue_zero.append(nextEvent)
                else:
                    self.server_zero = True
            else:
                eventos = eventos + 1
                self.server_zero = False
                num = self.u.ulcm()
                if num <= 0.5:
                    num = self.u.ulcm()
                    if num < 0.5:
                        self.queue_um_events.append(Events(self.exp.exp(), 'fila1', 'chegada'))
                    else:
                        self.queue_um_events.append(Events(self.exp.exp(), 'fila1', 'saida'))
                elif num > 0.5 and num <= 0.8:
                    num = self.u.ulcm()
                    if num < 0.5:
                        self.queue_dois_events.append(Events(self.exp.exp(), 'fila2', 'chegada'))
                    else:
                        self.queue_dois_events.append(Events(self.exp.exp(), 'fila2', 'saida'))
                else: 
                    pass

        self.queue_dois_events.append(Events(0, 'fila2', 'chegada'))  
        self.queue_um_events.append(Events(0, 'fila1', 'chegada'))
        
        while len(self.queue_um_events) > 0:

            if len(self.queue_um) > 0 and self.server_um == False:
                nextEvent1 = self.queue_um[0]                
                self.queue_um.remove(self.queue_um[0]) 
            else:
                nextEvent1 = self.queue_um_events[0]
                self.queue_um_events.remove(self.queue_um_events[0])
                
            if(nextEvent1.tipo == 'chegada'):
                if self.server_um == True:
                    self.queue_um.append(nextEvent1)
                else:
                    self.server_um = True
            else:
                eventos = eventos + 1
                self.server_um = False

        while len(self.queue_dois_events) > 0:
    
            if len(self.queue_dois) > 0 and self.server_dois == False:
                nextEvent1 = self.queue_dois[0]                
                self.queue_dois.remove(self.queue_dois[0]) 
            else:
                nextEvent1 = self.queue_dois_events[0]
                self.queue_dois_events.remove(self.queue_dois_events[0])
                
            if(nextEvent1.tipo == 'chegada'):
                if self.server_dois == True:
                    self.queue_dois.append(nextEvent1)
                else:
                    self.server_dois = True
            else:
                eventos = eventos + 1
                self.server_dois = False

        print(eventos)
        print(len(self.queue_um_events))
        print(len(self.queue_dois_events))
            