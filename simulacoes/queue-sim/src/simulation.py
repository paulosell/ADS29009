from events import events

class simulation:

    def __init__(self, simtime=0):
        self.simtime = simtime
        self.eventQueue = []

    def run(self):
        ev = event(0.1, 'zero', 'chegada')
        self.scheduleEvent(ev)
        while not self.eventQueue:
            nextEvent = self.eventQueue.pop()
            self.simtime += nextEvent.t
            nextEvent.processEvent()
    
    def scheduleEvent(self, newEvent):
        self.eventQueue.append(newEvent)