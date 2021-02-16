import timeit
import subprocess
import os
def setup():
    File = open("Test.txt.CUDARAND", "w")
    File.write("[9999, 30000]")
    File.close()
    subprocess.run(["/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU", "2", "Test.txt.CUDARAND"])
def run():
    subprocess.run(["/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU", "1", "Test.txt"])
    subprocess.run(["/Programs/CUDARANDCompressor/CUDARANDCompressor-GPU", "2", "Test.txt.CUDARAND"])
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
