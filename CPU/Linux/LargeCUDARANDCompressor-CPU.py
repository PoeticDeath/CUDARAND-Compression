import os
import subprocess
import fnmatch
import sys
import time
import psutil
global Start
Start = time.time()
global Filename
try:
    Filename = sys.argv[1]
except IndexError:
    Filename = input("What file would you like to compress or decompress? : ")
def check_process_status(process_name):
    process_status = [ proc.status() for proc in psutil.process_iter() if proc.name() == process_name ]
    if process_status:
        return True
    else:
        return False
def LargeCompress():
    Filedir = os.getcwd()
    subprocess.run(["/usr/bin/mkdir", "Data"])
    subprocess.run(["/usr/bin/split", "-b 415", f"{Filename}", f"{Filedir}/Data/{Filename}."])
    List = []
    for root, dirs, files in os.walk(str(Filedir + "/Data/")):
        for name in files:
            filename = os.path.join(root, name)
            if os.stat(filename).st_size == 415:
                List.append(name)
    for Part in List:
        subprocess.run(["python3", "/Programs/CUDARANDCompressor/CUDARANDCompressor-CPU.py", f"1", f"Data/{Part}"])
    End = time.time() - Start
    print("It took a total of " + str(End) + " seconds to Compress.")
def LargeDecompress():
    Filedir = os.getcwd()
    List = fnmatch.filter(os.listdir(str(Filedir + "/Data")), "*.CUDARAND.HEXS")
    List1 = fnmatch.filter(os.listdir(str(Filedir + "/Data")), "*.CUDARAND.HEXS")
    List2 = os.listdir(str(Filedir + "/Data"))
    x = 1
    for Part in List:
        subprocess.Popen(["python3", "/Programs/CUDARANDCompressor/CUDARANDCompressor-CPU.py", f"2", f"Data/{Part}"])
        if (x % 10 == 0):
            time.sleep(10)
            print(str(x / len(List) * 100) + "% Complete", end="\r")
        x += 1
    while (str(List) != "[]"):
        List = fnmatch.filter(os.listdir(str(Filedir + "/Data")), "*.CUDARAND.HEXS")
        pass
    while (len(List2) < len(List1)):
        List2 = os.listdir(str(Filedir + "/Data"))
        pass
    while check_process_status("CUDARANDCompressor-CPU"):
        pass
    List = os.listdir(str(Filedir + "/Data"))
    for Part in List:
        os.system("cat " + "Data/" + Part + " >> " + Filename)
    End = time.time() - Start
    print("It took a total of " + str(End) + " seconds to Decompress.")
try:
    FileAction = sys.argv[2]
except IndexError:
    FileAction = 0
if (FileAction == 0):
    FileAction = input("Would you like to compress or decompress these files? Enter 1 to Compress or 2 to Decompress: ")
if (FileAction == str("1")):
    print("Compressing")
    LargeCompress()
    print("Compressed")
if (FileAction == str("2")):
    print("Decompressing")
    LargeDecompress()
    print("Decompressed")
