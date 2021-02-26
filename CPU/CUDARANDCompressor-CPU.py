from torch import manual_seed, randint, equal, LongTensor
from sys import argv
from sys import exit
from multiprocessing import Process as Thread
from multiprocessing import Manager
manager = Manager()
from time import time
from os import remove
from psutil import cpu_count
def Processing(x, y, strrec):
    try:
        manual_seed(x)
        strrec[1] = randint(9, (1, y), device="cpu")
        manual_seed(x - 1)
        strrec[2] = randint(9, (1, y), device="cpu")
        manual_seed(x - 2)
        strrec[3] = randint(9, (1, y), device="cpu")
        manual_seed(x - 3)
        strrec[4] = randint(9, (1, y), device="cpu")
        manual_seed(x - 4)
        strrec[5] = randint(9, (1, y), device="cpu")
        manual_seed(x - 5)
        strrec[6] = randint(9, (1, y), device="cpu")
        manual_seed(x - 6)
        strrec[7] = randint(9, (1, y), device="cpu")
        manual_seed(x - 7)
        strrec[8] = randint(9, (1, y), device="cpu")
        manual_seed(x - 8)
        strrec[9] = randint(9, (1, y), device="cpu")
        manual_seed(x - 9)
        strrec[10] = randint(9, (1, y), device="cpu")
        manual_seed(x - 10)
        strrec[11] = randint(9, (1, y), device="cpu")
    except:
        exit()
def CompressMT(a1, a2, a3, a4, Threads, Done, ANS, CUR):
    try:
        w = -(int(int(Threads) + int(int(a1) - 1) * 11))
        strrec = LongTensor([0])
        while equal(strrec, a3) is False:
            if (Done[1] != "0"):
                exit()
            w += int(int(Threads) * 11)
            strrec = manager.dict()
            t = Thread(target=Processing, args=(w, a4, strrec))
            t.start()
            t.join()
            b = 0
            if (b == 0):
                if equal(strrec[1], a3) is True:
                    b = 1
                    w = w - 0
                    strrec = strrec[1]
            if (b == 0):
                if equal(strrec[2], a3) is True:
                    b = 1
                    w = w - 1
                    strrec = strrec[2]
            if (b == 0):
                if equal(strrec[3], a3) is True:
                    b = 1
                    w = w - 2
                    strrec = strrec[3]
            if (b == 0):
                if equal(strrec[4], a3) is True:
                    b = 1
                    w = w - 3
                    strrec = strrec[4]
            if (b == 0):
                if equal(strrec[5], a3) is True:
                    b = 1
                    w = w - 4
                    strrec = strrec[5]
            if (b == 0):
                if equal(strrec[6], a3) is True:
                    b = 1
                    w = w - 5
                    strrec = strrec[6]
            if (b == 0):
                if equal(strrec[7], a3) is True:
                    b = 1
                    w = w - 6
                    strrec = strrec[7]
            if (b == 0):
                if equal(strrec[8], a3) is True:
                    b = 1
                    w = w - 7
                    strrec = strrec[8]
            if (b == 0):
                if equal(strrec[9], a3) is True:
                    b = 1
                    w = w - 8
                    strrec = strrec[9]
            if (b == 0):
                if equal(strrec[10], a3) is True:
                    b = 1
                    w = w - 9
                    strrec = strrec[10]
            if (b == 0):
                if equal(strrec[11], a3) is True:
                    b = 1
                    w = w - 10
                    strrec = strrec[11]
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
    srtstr = randint(9, (1, int(srtstrlen)), device="cpu")
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
    n = 0.5
    if (cpu_count() == cpu_count(logical=False)):
        Threads = cpu_count() - 1
    else:
        Threads = cpu_count() - cpu_count() / cpu_count(logical=False)
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
