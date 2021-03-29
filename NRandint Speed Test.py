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
n = 1000
c = n // 10
a = 10**9
b = 10**10
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
#print(torchrun.tolist())
#print(numpyrun.tolist())
#print(njitrun.tolist())
#if (numpyrun.tolist() == njitrun.tolist()):
#    print("They are the same.")
#else:
#    print("They are different.")
