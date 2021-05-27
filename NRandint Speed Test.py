# NRandint Speed Test

from numpy.random import seed, randint
from torch import manual_seed
from torch import randint as rand
from numba import njit
from time import time
@njit
def nrandint(w, x, y, z):
    seed(w)
    v = randint(x, y, z)
    return v[:z]
s = 0
c = 10
a = 0
b = 10
manual_seed(s)
rand(a, (b-1), (1, c))
tstart = time()
manual_seed(s)
torchrun = rand(a, (b-1), (1, c))
tend = time() - tstart
print("torch finished.")
seed(s)
randint(a, b, c)
nstart = time()
seed(s)
numpyrun = randint(a, b, c)
nend = time() - nstart
print("numpy finished.")
nrandint(s, a, b, c)
jstart = time()
njitrun = nrandint(s, a, b, c)
jend = time() - jstart
print("njit finished.")
print(str("%.16f" % tend) + " seconds for a torch run.")
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
