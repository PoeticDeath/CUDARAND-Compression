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
def CompressMT(a1, a2, a3, Threads, ANS, CUR, x):
    try:
        n = 0
        v = 400
        w = a1 - 1 + x
        strr = [0]
        strrec = [0]
        while strr != a2:
            if (ANS[1] != ""):
                exit()
            w += Threads
            if int(nrandint(w, 0, 256, 1)[0]) == a2[0]:
                strrec = nrandint(w, 0, 256, a3)
                strrec = strrec.tolist()
            else:
                strrec = [0]
            if strrec == a2:
                strr = strrec
            n += 1
            if n % v == 0:
                n = 0
                CUR[1] += v
        ANS[1] = int(w)
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
    srtstr = nrandint(int(z), 0, 256, int(srtstrlen))
    srtstr = srtstr.tolist()
    Data = b''
    for byte in srtstr:
        Data += int(byte).to_bytes(1, "big")
    remove(Filename)
    Filename = Filename[:-9]
    OpenFile = open(Filename, "wb")
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
    srtstr = OpenFile.read()
    srtstr = [srtstr[i] for i in range(0, len(srtstr))]
    srtstrlen = len(srtstr)
    n = 1
    if (cpu_count() == cpu_count(logical=False)):
        Threads = cpu_count() - 1
    else:
        Threads = cpu_count() - cpu_count() / cpu_count(logical=False)
    Threads = Threads * n
    try:
        x = int(argv[3])
    except IndexError:
        x = 0
    Threadsnm = 1
    ANS = manager.dict()
    CUR = manager.dict()
    ANS[1] = ""
    CUR[1] = 0 + x
    Start = time()
    while (Threadsnm <= Threads):
        Thread(target=CompressMT, args=(Threadsnm, srtstr, srtstrlen, Threads, ANS, CUR, x)).start()
        print("Thread " + str(Threadsnm) + " started.")
        Threadsnm += 1
    while (ANS[1] == ""):
        CURTIME = time() - Start
        print(f'{CUR[1]:,}' + ' Checked, ' + f'{int(int(CUR[1]-x)//CURTIME):,}' + ' Checked per Second.', end="\r")
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
        print(str("\n" + "Compression took " + str(int(End)) + " seconds."))
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
