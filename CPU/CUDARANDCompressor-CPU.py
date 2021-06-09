from numpy.random import seed, randint
from numba import njit
from sys import argv
from sys import exit
from multiprocessing import Process as Thread
from multiprocessing import Manager
from time import time
from os import remove
from psutil import cpu_count
@njit
def nrandint(w, x, y, z):
    seed(w)
    v = randint(x, y, z)
    return v[:z]
def CompressMT(a1, a2, a3, a4, Threads, Done, ANS, CUR):
    manager = Manager()
    try:
        v = 11
        w = -(int(int(Threads) + int(int(a1) - 1) * v))
        strrec = [0]
        while (strrec == a3) is False:
            if (Done[1] != "0"):
                exit()
            w += int(int(Threads) * v)
            strrec = manager.dict()
            n = 0
            while (n < v):
                if str(nrandint(w-n, 0, 10, 1)[0]) == a3[0]:
                    strrec[n + 1] = nrandint(w-n, 0, 10, a4)
                    strrec[n + 1] = [ str(x) for x in strrec[n + 1] ]
                else:
                    strrec[n + 1] = [0]
                n += 1
            b = 0
            n = 0
            while (n < v):
                if (b == 0):
                    if (strrec[n + 1] == a3) is True:
                        b = 1
                        w = w - n
                        strrec = strrec[n + 1]
                n += 1
            if (b == 0):
                strrec = [0]
            CUR[1] += v-1
        ANS[1] = str(w)
        Done[1] = "1"
    except:
        exit()
def Decompress():
    from ast import literal_eval
    from HEXSmash import main
    try:
        Filename = argv[2]
    except IndexError:
        Filename = input("What would you like the file to be called? : ")
    main('1', Filename)
    remove(Filename)
    Filename = Filename[:-5]
    OpenFile = open(Filename, "r")
    HEXSTR = str(str(str(OpenFile.read()).replace("(", "[")).replace(")", "]")).replace("C", ",")
    Data = literal_eval(HEXSTR)
    OpenFile.close()
    z = Data[0]
    z = int(str(z), 16)
    srtstrlen = Data[1]
    srtstrlen = int(str(srtstrlen), 16)
    srtstr = nrandint(int(z), 0, 10, int(srtstrlen))
    srtstr = srtstr.tolist()
    srtstr = str(srtstr)
    srtstr = srtstr.replace("[", "")
    srtstr = srtstr.replace("]", "")
    srtstr = srtstr.replace(", ", "")
    remove(Filename)
    Filename = Filename[:-9]
    OpenFile = open(Filename, "wb")
    Data = int(srtstr).to_bytes((int(srtstr).bit_length() + 7) // 8, byteorder="big")
    OpenFile.write(Data)
    OpenFile.close()
def Compress():
    manager = Manager()
    from HEXSmash import main
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
    for digit in srtstr:
        SRTSTR += [digit]
    srtstr = SRTSTR
    del SRTSTR
    n = 1
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
    OpenFile.write(str("(\"" + str(z)[2:] + "\"C \"" + str(srtstrlen)[2:] + "\")"))
    OpenFile.close()
    main('0', Filename)
    remove(Filename)
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
