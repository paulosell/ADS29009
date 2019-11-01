from src.simulador import Simulador
from src.rng import prng
from src.events import Events

class SimuladorFilas(Simulador):

    def __init__(self):
        super().__init__()     
        self.u = prng.modo(modo='lcm', seed=116432, a = 1103515245, c = 12345, m = 2147483648)
        self.exp = prng.modo(modo='exp',seed=14511, lamb=0.1)
    
    def gera_eventos(self):
        eventos_gerados = 0
        while eventos_gerados < 100000:           
            self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'chegada'))           
            self.scheduleEvent(Events(self.exp.exp(), 'eventos', 'saida'))
            eventos_gerados = eventos_gerados + 1
        self.scheduleEvent(Events(0, 'eventos', 'chegada'))
        
            

    def run(self):
        eventos = 0
        queue_um_events   = []
        queue_dois_events = []
        queue_um = []
        queue_dois = []
        queue_zero = []
        server_zero = False
        server_um = False
        server_dois= False
        print(self.eventQueue.qsize())
        while not self.eventQueue.empty():
            if len(queue_zero) > 0 and server_zero == False:
                nextEvent = queue_zero[0]
                
                queue_zero.remove(queue_zero[0]) 
            else:
                nextEvent = self.eventQueue.get()[1]
                
            if(nextEvent.tipo == 'chegada'):
                if server_zero == True:
                    queue_zero.append(nextEvent)
                else:
                   server_zero = True
            else:
                eventos = eventos + 1
                server_zero = False
                num = self.u.ulcm()
                if num <= 0.5:
                    chegada, saida = nextEvent.processEvent()
                    queue_um_events.append(chegada)                  
                    queue_um_events.append(saida)
                elif num > 0.5 and num <= 0.8:
                    chegada, saida = nextEvent.processEvent()
                    queue_dois_events.append(chegada)                  
                    queue_dois_events.append(saida)
                else: 
                    pass

        queue_dois_events.append(Events(0, 'fila2', 'chegada'))  
        queue_um_events.append(Events(0, 'fila1', 'chegada'))
        print(len(queue_dois_events))
        print(len(queue_um_events))

        while len(queue_um_events) > 0:
            if len(queue_um) > 0 and server_um == False:
                nextEvent1 = queue_um[0]                
                queue_um.remove(queue_um[0]) 
            else:
                nextEvent1 = queue_um_events[0]
                queue_um_events.remove(queue_um_events[0])
                
            if(nextEvent1.tipo == 'chegada'):
                if server_um == True:
                    queue_um.append(nextEvent1)
                else:
                    server_um = True
            else:
                eventos = eventos + 1
                server_um = False

        while len(queue_dois_events) > 0:    
            if len(queue_dois) > 0 and server_dois== False:
                nextEvent1 = queue_dois[0]                
                queue_dois.remove(queue_dois[0]) 
            else:
                nextEvent1 = queue_dois_events[0]
                queue_dois_events.remove(queue_dois_events[0])
                
            if(nextEvent1.tipo == 'chegada'):
                if server_dois== True:
                    queue_dois.append(nextEvent1)
                else:
                    server_dois= True
            else:
                eventos = eventos + 1
                server_dois= False

     