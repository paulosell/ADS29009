from simulation import simulation

class simuladorFilas(simulation):

    def __init__(self):
        self.queue_zero = []
        self.queue_um   = []
        self.queue_dois = []
        self.server_zero = False
        