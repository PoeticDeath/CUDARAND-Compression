def compress(num):
    cdata = format(int(num), 'x')
    try:
        int(cdata)
        return cdata
    except ValueError:
        print('Not Compressable.')
        exit()
def decompress(num):
    return int(str(num), 16)
def main(action, filename):
    if action == '0':
        dfile = open(filename, 'rb')
        data = dfile.read()
        dfile.close()
        ddata = int.from_bytes(data, 'big')
        cdata = compress(ddata)
        ccdata = int(cdata).to_bytes((int(cdata).bit_length() + 7) // 8, byteorder='big')
        cfile = open(filename + '.HEXS', 'wb')
        cfile.write(ccdata)
        cfile.close()
    if action == '1':
        cfile = open(filename, 'rb')
        cdata = cfile.read()
        ccdata = int.from_bytes(cdata, 'big')
        ddata = decompress(ccdata)
        dddata = int(ddata).to_bytes((int(ddata).bit_length() + 7) // 8, byteorder='big')
        dfile = open(filename[:-5], 'wb')
        dfile.write(dddata)
        dfile.close()
if __name__ == '__main__':
    action = input('Would you like to compress or decompress? 0 or 1: ')
    if action == '0':
        filename = input('What file would you like to try to compress?: ')
    if action == '1':
        filename = input('What file would you like to decompress?: ')
    main(action, filename)
