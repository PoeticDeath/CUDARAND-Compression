import timeit
import subprocess
import os
def setup():
    File = open("Test.txt.CUDARAND", "w")
    File.write("[\"270f\", \"7530\"]")
    File.close()
    subprocess.run(["python3", "/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU.py", "2", "Test.txt.CUDARAND"])
def run():
    subprocess.run(["python3", "/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU.py", "1", "Test.txt"])
    subprocess.run(["python3", "/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU.py", "2", "Test.txt.CUDARAND"])
os.mkdir("/Programs/CUDARANDCompressor/Test")
os.chdir("/Programs/CUDARANDCompressor/Test")
setup()
Before = float(1000000000)
After = float(999999999)
Cores = int(0)
while (After < Before):
    Before = After
    Cores += 1
    CUDA = open("/Programs/CUDARANDCompressor/GPUCUDACores.txt", "w")
    CUDA.write(str(Cores))
    CUDA.close()
    After = timeit.timeit(run, number=1)
    print(str(After))
CUDA = open("/Programs/CUDARANDCompressor/GPUCUDACores.txt", "w")
CUDA.write(str(int(Cores - 1)))
CUDA.close()
os.remove("Test.txt")
os.chdir("/Programs/CUDARANDCompressor")
os.rmdir("/Programs/CUDARANDCompressor/Test")
