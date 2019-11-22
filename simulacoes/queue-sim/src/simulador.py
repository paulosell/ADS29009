from queue import PriorityQueue
class Simulador:

    def __init__(self, simtime=0):
        self.simtime = simtime
        self.eventQueue = PriorityQueue()

    def run(self):
        while not self.eventQueue:            
            nextEvent = self.eventQueue.get()
            self.simtime += nextEvent.time
            nextEvent.processEvent()
    
    def scheduleEvent(self, newEvent):
        self.eventQueue.put((newEvent.time, newEvent))