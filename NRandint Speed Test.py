from numpy.random import seed, randint
from torch import manual_seed
from torch import randint as rand
from numba import njit
from time import time
@njit(parallel=True)
def nrandint(w, x, y, z):
    seed(w)
    v = randint(x, y, z*4)
    return v[:z]
s = 0
n = 1000
tstart = time()
manual_seed(s)
torchrun = rand(0, 9, (1, n))
tend = time() - tstart
print("torch finished.")
nstart = time()
seed(s)
numpyrun = randint(0, 10, n)
nend = time() - nstart
print("numpy finished.")
nrandint(s, 0, 10, n)
jstart = time()
njitrun = nrandint(s, 0, 10, n)
jend = time() - jstart
print("njit finished.")
if (str(numpyrun.tolist()) == str(njitrun.tolist())):
    print("They are equal.")
    print(str("%.16f" % tend) + " seconds for a torch run.")
    print(str("%.16f" % nend) + " seconds for a numpy run.")
    print(str("%.16f" % jend) + " seconds for a njit run.")
else:
    print("They aren't equal.")
    print(str("%.16f" % tend) + " seconds for a torch run.")
    print(str("%.16f" % nend) + " seconds for a numpy run.")
    print(str("%.16f" % jend) + " seconds for a njit run.")
