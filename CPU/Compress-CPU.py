from os import cpu_count
from sys import argv
from torch import manual_seed
from torch import randint
def Compress():
    w = -(int(int(cpu_count()) * int(argv[2])) + int(int(argv[1]) - 1))
    strrec = ""
    while (strrec != argv[3]):
        w += int(cpu_count()) * int(argv[2])
        manual_seed(w)
        value = randint(9, (1, int(argv[4])), device="cpu")
        value = value.tolist()
        value = str(value)
        value = value.replace("[[", "")
        value = value.replace("]]", "")
        value = value.replace(", ", "")
        value = int(value)
        strrec = str(value)
    TempFile = open("TempFile", "w")
    TempFile.write(str(w))
    TempFile.close()
Compress()
