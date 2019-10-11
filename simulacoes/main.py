from rng import prng, seno
import datetime

lcm = prng.modo(modo = 'lcm',seed=0, a = 1103515245, c = 12345, m = 2147483648)

def computar_desloc_x():
    return 10 + (20 * lcm.ulcm())

def computar_lateral(yy,xx):
    return  (seno.seno(0.042 * xx) * 50)- yy

x = 0
y = 0
max_x = 150
ev1 = datetime.datetime.now().microsecond/1000000

while(x < max_x):
    desloc_x = computar_desloc_x()
    x = desloc_x + x
    for i in range(0,10):
        print('andando em x')
    desloc_y = computar_lateral(y,x)
    y = desloc_y + y
    for i in range(0,10):
        print('andando em y')
    print(x,y)
    print(datetime.datetime.now().microsecond/1000000 - ev1)