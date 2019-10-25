class lcm:
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
    


class prng:
      
    def modo(self, **kwargs):
        if kwargs.get('modo') == 'lcm':
            return lcm(seed = kwargs.get('seed'), a = kwargs.get('a'), c = kwargs.get('c'), m= kwargs.get('m'))



class fat:
    
    def fatorial(self, x):
        if x == 0:
            x = 1
        fat = x
        for i in range(x-1,1,-1):
            fat = fat * i
        return fat

fatorial = fat()
class sin:
    
    def seno(self, x):
        return round((x - ((x**3)/fatorial.fatorial(3)) + ((x**5)/fatorial.fatorial(5)) - ((x**7)/fatorial.fatorial(7)) + ((x**9)/fatorial.fatorial(9)) - ((x**11)/fatorial.fatorial(11)) + ((x**13)/fatorial.fatorial(13)) - ((x**15)/fatorial.fatorial(15)) + ((x**17)/fatorial.fatorial(17))) - ((x**19)/fatorial.fatorial(19)) +((x**21)/fatorial.fatorial(21)),2)

seno = sin()
prng = prng()
