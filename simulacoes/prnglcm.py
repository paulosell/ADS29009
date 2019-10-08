class prnglcm:
    
    def __init__(self, **kwargs):
        self.seed = kwargs.get('seed')
        self.a = kwargs.get('a')
        self.c = kwargs.get('c')
        self.m = kwargs.get('m')

    def setSeed(self, seed):
        self.seed = seed
    
    def setA(self, a):
        self.a = a
    
    def setC(self, c):
        self.c = c

    def setM(self, m):
        self.m = m
    
    def _hasParameters(self):
        return (self.seed is not None and self.a is not None and self.m is not None)


    def ulcm(self):
        if self._hasParameters():
            zn = ((self.a * self.seed)+ self.c) % self.m
            self.seed = zn
            return zn/self.m
        raise Exception('Verifique parametros da classe')
    

    def lcm(self):
        if self._hasParameters():
            zn = ((self.a * self.seed)+ self.c) % self.m
            self.seed = zn
            return zn
        raise Exception('Verifique parametros da classe')
    


