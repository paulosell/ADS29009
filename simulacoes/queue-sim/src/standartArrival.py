from event import event

class standartArrival(event):
    
    def __init__(self,t):
        self.time = t
    
    def processEvent(self):
        print("Processando evento no tempo {}".format(t))
