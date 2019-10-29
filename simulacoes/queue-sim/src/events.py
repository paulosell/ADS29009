from event import event

class events(event):
    
    def __init__(self,t, fila, tipo):
        self.time = t
        self.fila = fila
        self.tipo = tipo
    
    def processEvent(self):
        print("Processando evento no tempo {}".format(self.time))
        if (self.tipo == 'chegada'):
            # se server livre criar evento de saida senao colocar na fila
            # criar evento de entrada