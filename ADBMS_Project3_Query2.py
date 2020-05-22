import struct
import collections
import dbm
from datetime import date
query2_dbm = dbm.open('query2', 'c')
bin_file = open("small.bin", 'rb')     # Open the file in read binary mode
size_of_blocks = 40960
buffer_factor = 10
block_size = int(size_of_blocks/buffer_factor)
fmt = '20s20s70s40s80s25s3i12s25s50s50s'
record_size = struct.calcsize(fmt)


# Reading the file as block by block
def binary_file_extract():
    block_number = 0
    while True:
        block = bin_file.read(block_size)  # reading each block of size 4096 bytes
        if not block:                      # Terminates if block doesnt find 4096 bytes
            break
        block_number += 1
        dbm_create(unpack(block), block_number)


# Reading each block and returning the extracted records
def unpack(block):
    list_of_records = []
    Result = collections.namedtuple('Result', 'fname lname job company address phone day month year ssn username email url')
    while True:
        if not block[record_size:]:                    # Terminates if record doesnt find 4096 bytes
            break
        temp_list = []
        record = struct.unpack(fmt, block[:record_size])  # Unpack each record
        for each_value in record:
            if type(each_value) != type(1):
                k = each_value.decode('utf-8')
                temp_list.append(str(k).replace('\x00', ''))
            else:
                temp_list.append(each_value)
        list_of_records.append(Result(*temp_list))
        block = block[record_size:]
    return list_of_records


def dbm_create(records, block_number):
    for i in records:
        if i.ssn in query2_dbm:
            print("Duplicate Found: BLock Number - ", block_number, "SSN-", i.ssn)
        query2_dbm[i.ssn] = str(block_number)


def main():
    binary_file_extract()


if __name__ == '__main__':
    main()

bin_file.close()
query2_dbm.close()
