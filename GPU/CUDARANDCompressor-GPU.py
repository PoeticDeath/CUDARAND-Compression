from torch import manual_seed, randint, equal
from torch.cuda import LongTensor
from sys import argv
from sys import exit
from multiprocessing import Process as Thread
from multiprocessing import Manager
manager = Manager()
from time import time
from os import remove
from sys import platform
def Processing(x, y, strrec, v):
    try:
        n = 0
        while (n < v):
            manual_seed(x - n)
            strrec[n + 1] = randint(9, (1, y), device="cuda:0")
            n += 1
    except:
        exit()
def CompressMT(a1, a2, a3, a4, Threads, Done, ANS, CUR):
    try:
        v = 10
        w = -(int(int(Threads) + int(int(a1) - 1) * v))
        strrec = LongTensor([0])
        while equal(strrec, a3) is False:
            if (Done[1] != "0"):
                exit()
            w += int(int(Threads) * v)
            strrec = manager.dict()
            t = Thread(target=Processing, args=(w, a4, strrec, v,))
            t.start()
            t.join()
            b = 0
            n = 0
            while (n < v):
                if (b == 0):
                    if equal(strrec[n + 1], a3) is True:
                        b = 1
                        w = w - n
                        strrec = strrec[n + 1]
                n += 1
            if (b == 0):
                strrec = LongTensor([0])
            CUR[1] = w
        ANS[1] = str(w)
        Done[1] = "1"
    except:
        exit()
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
    z = int(z, 16)
    srtstrlen = Data[1]
    srtstrlen = int(srtstrlen, 16)
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
    SRTSTR = []
    for intr in srtstr:
        SRTSTR = SRTSTR + [int(intr)]
    srtstr = SRTSTR
    del SRTSTR
    srtstr = LongTensor([srtstr])
    n = 1
    if (platform() == "win32"):
        GPUThreads = open("C:\Program Files\CUDARANDCompressor\GPUCUDACores.txt", "r")
        Threads = int(GPUThreads.read()) * n
        GPUThreads.close()
    if (platform() == "linux"):
        GPUThreads = open("/Programs/CUDARANDCompressor/GPUCUDACores.txt", "r")
        Threads = int(GPUThreads.read()) * n
        GPUThreads.close()
    Threads = Threads * n
    try:
        x = int(argv[3]) - (Threads * n)
    except IndexError:
        x = -(Threads * n)
    z = x
    Threadsnm = 1
    Done = manager.dict()
    ANS = manager.dict()
    CUR = manager.dict()
    Done[1] = "0"
    ANS[1] = ""
    CUR[1] = 0
    while (Threadsnm <= Threads):
        Thread(target=CompressMT, args=(Threadsnm, n, srtstr, srtstrlen, Threads, Done, ANS, CUR,)).start()
        print("Thread " + str(Threadsnm) + " started.")
        Threadsnm += 1
    while (ANS[1] == ""):
        print(CUR[1], end="\r")
        pass
    z = int(ANS[1])
    OpenFile.close()
    remove(Filename)
    Filename = Filename + ".CUDARAND"
    z = hex(z)
    srtstrlen = hex(srtstrlen)
    OpenFile = open(Filename, "w")
    OpenFile.write(str("[\"" + str(z)[2:] + "\", \"" + str(srtstrlen)[2:] + "\"]"))
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
