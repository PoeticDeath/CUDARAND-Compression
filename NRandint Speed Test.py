# NRandint Speed Test

from numpy.random import seed, randint
from numba import njit
from time import time
@njit
def nrandint(w, x, y, z):
    seed(w)
    v = randint(x, y, z)
    return v[:z]
s = 0
c = 1000000
a = 0
b = 2**(8*7)
seed(s)
randint(a, b, c, dtype='uint64')
nstart = time()
seed(s+1)
numpyrun = randint(a, b, c, dtype='uint64')
nend = time() - nstart
print("numpy finished.")
nrandint(s, a, b, c)
jstart = time()
njitrun = nrandint(s+1, a, b, c)
jend = time() - jstart
print("njit finished.")
print(str("%.16f" % nend) + " seconds for a numpy run.")
print(str("%.16f" % jend) + " seconds for a njit  run.")

# Compare List Speed Test

liststart = time()
if njitrun.tolist() == numpyrun.tolist():
    listend = time()
    print(str("%.16f" % float(listend - liststart)), "seconds for comparing njit and numpy lists.")
else:
    listend = time()
    print(str("%.16f" % float(listend - liststart)), "seconds for comparing njit and numpy lists.")

# Measure Measurement Time Test

st = time()
en = time()
print(str("%.16f" % float(en - st)), "seconds for measuring time.")

# Measure Clock Speed

from psutil import cpu_freq
print(str("%.16f" % float(1 / (max(cpu_freq())*1000000))), "seconds per clock.")

# Bytes Gen Per Sec

print(f'{float(1/jend*c/1_000_000_000):,}', 'GBytes per Second per Core.')
