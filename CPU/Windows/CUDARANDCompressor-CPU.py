from torch import manual_seed
from torch import randint
from sys import argv
from sys import exit
from threading import Thread
from time import time
from os import remove
import subprocess
from os import cpu_count
from os import getpid
import psutil
def Decompress():
    from ast import literal_eval
    try:
        Filename = argv[2]
    except IndexError:
        Filename = input("What would you like the file to be called? : ")
    OpenFile = open(Filename, "r")
    Data = literal_eval(OpenFile.read())
    OpenFile.close()
    z = Data[0]
    srtstrlen = Data[1]
    manual_seed(int(z))
    value = randint(9, (1, int(srtstrlen)), device="cpu")
    value = value.tolist()
    value = str(value)
    value = value.replace("[[", "")
    value = value.replace("]]", "")
    value = value.replace(", ", "")
    value = int(value)
    srtstr = str(value)
    remove(Filename)
    Filename = Filename[:-9]
    OpenFile = open(Filename, "wb")
    Data = int(srtstr).to_bytes((int(srtstr).bit_length() + 7) // 8, byteorder="big")
    OpenFile.write(Data)
    OpenFile.close()
def Compress():
    global x, srtstr, srtstrlen, z
    try:
        Filename = argv[2]
    except IndexError:
        Filename = input("What file would you like to compress? : ")
    OpenFile = open(Filename, "rb")
    Data = OpenFile.read()
    srtstr = int.from_bytes(Data, "big")
    srtstr = str(srtstr)
    srtstrlen = len(srtstr)
    n = 1
    Threads = cpu_count() * n
    try:
        x = int(argv[3]) - (Threads * n)
    except IndexError:
        x = -(Threads * n)
    z = x
    Threadsnm = 1
    Tempfile = open("TempFile", "w")
    Tempfile.write(str(""))
    Tempfile.close()
    while (Threadsnm <= Threads):
        subprocess.Popen(["C:\Program Files\CUDARANDCompressor\Compress-CPU.exe", f"{Threadsnm}", f"{n}", f"{srtstr}", f"{srtstrlen}"], stdout=subprocess.PIPE)
        print("Thread " + str(Threadsnm) + " started.")
        Threadsnm += 1
    TempFile = open("TempFile", "r")
    Data = TempFile.read()
    while (Data == ""):
        Data = TempFile.read()
        pass
    TempFile.close()
    z = int(Data)
    OpenFile.close()
    remove(Filename)
    pid = getpid()
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    remove("TempFile")
    Filename = Filename + ".CUDARAND"
    OpenFile = open(Filename, "w")
    OpenFile.write(str("[" + str(z) + ", " + str(srtstrlen) + "]"))
    OpenFile.close()
def Main():
    try:
        FileAction = argv[1]
    except IndexError:
        FileAction = 0
    if (FileAction == 0):
        FileAction = input("Would you like to compress or decompress the file? Enter 1 to Compress or 2 to Decompress: ")
    if (FileAction == str("1")):
        print("Compressing")
        Start = time()
        Compress()
        End = time() - Start
        print(str("Compression took " + str(int(End)) + " seconds."))
        print("Compressed")
    if (FileAction == str("2")):
        print("Decompressing")
        Start = time()
        Decompress()
        End = time() - Start
        print(str("Decompression took " + str(int(End)) + " seconds."))
        print("Decompressed")
Main()
