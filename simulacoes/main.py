import prng

lcm = prng.prng().modo(modo = 'lcm',seed=0, a = 1103515245, c = 12345, m = 2147483648)
for i in range(10):
    print(lcm.lcm())

print(prng.fatorial(5))
