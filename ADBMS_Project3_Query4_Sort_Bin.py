import struct
import collections
import datetime
from operator import attrgetter
import pickle
li = []

file = open("small.bin", 'rb')
new_file = open("new_file.bin", 'wb')


# Reading each block and returning the list of 10 records
def unpack(blockSize):
    recordSize = struct.calcsize('20s20s70s40s80s25s3i12s25s50s50s')
    Records = []
    Result = collections.namedtuple('Res', 'fname lname job company address phone date month year ssn username email url')
    while True:
        if not blockSize[recordSize:]:
            break
        records = []
        g = struct.unpack('20s20s70s40s80s25s3i12s25s50s50s',blockSize[:recordSize])
        for i in g:
            if (type(i) != type(1)):
                records.append(str(i.decode('utf-8')).replace('\x00', ''))
            else:
                records.append(i)
        Records.append(Result(*records))
        blockSize = blockSize[recordSize:]

    return Records


# Reading whole file and moving each block to unpack function
def read_binary():
    blockCount = 0
    blockSize = 4096
    while True:
        requiredBlockSize = file.read(blockSize)
        if not requiredBlockSize:
            break
        blockCount += 1
        Records = unpack(requiredBlockSize)
        for i in Records:
            li.append(i)
    return Records


def create_new_bin(Records):
    s = '\x00'
    sorted_rec = sorted(Records, key=attrgetter('year', 'month', 'date'))
    record_count = 0
    for i in sorted_rec:
        record_count += 1
        d = struct.pack('20s20s70s40s80s25s3i12s25s50s50s', i[0].encode('utf-8'), i[1].encode('utf-8'),
                        i[2].encode('utf-8'), i[3].encode('utf-8'), i[4].encode('utf-8'), i[5].encode('utf-8'), i[6],
                        i[7], i[8], i[9].encode('utf-8'), i[10].encode('utf-8'), i[11].encode('utf-8'),
                        i[12].encode('utf-8'))
        new_file.write(d)
        if record_count % 10 == 0:
            y = struct.pack('46s', s.encode('utf-8'))
            new_file.write(y)


def main():
    read_binary()
    create_new_bin(li)
    file.close()
    new_file.close()


if __name__ == '__main__':
    main()
