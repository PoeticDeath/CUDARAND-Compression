from torch import manual_seed
from torch import randint
from sys import argv
from sys import exit
from threading import Thread
from time import time
from os import remove
def CompressMMT(strrec, w, a2, a3, a4, Threads):
    while (strrec != a3):
        w += int(Threads) * int(a2)
        manual_seed(w)
        strrec = randint(9, (1, int(a4)), device="cuda:0")
        strrec = strrec.tolist()
        strrec = str(strrec)
        strrec = strrec.replace("[[", "")
        strrec = strrec.replace("]]", "")
        strrec = strrec.replace(", ", "")
    TempFile = open("TempFile", "w")
    TempFile.write(str(w))
    TempFile.close()
def CompressMT(a1, a2, a3, a4, Threads):
    w = -(int(int(Threads) * int(a2) + int(int(a1) - 1)))
    strrec = ""
    CompressMMT(strrec, w, a2, a3, a4, Threads)
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
    srtstr = randint(9, (1, int(srtstrlen)), device="cuda:0")
    srtstr = srtstr.tolist()
    srtstr = str(srtstr)
    srtstr = srtstr.replace("[[", "")
    srtstr = srtstr.replace("]]", "")
    srtstr = srtstr.replace(", ", "")
    remove(Filename)
    Filename = Filename[:-9]
    OpenFile = open(Filename, "wb")
    Data = int(srtstr).to_bytes((int(srtstr).bit_length() + 7) // 8, byteorder="big")
    OpenFile.write(Data)
    OpenFile.close()
def Compress():
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
    GPUThreads = open("C:\Program Files\CUDARANDCompressor\GPUCUDACores.txt", "r")
    Threads = int(GPUThreads.read()) * n
    GPUThreads.close()
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
        Thread(target=CompressMT, args=(Threadsnm, n, srtstr, srtstrlen, Threads,), daemon=True).start()
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
if __name__ == '__main__':
    Main()
