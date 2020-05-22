import struct
import dbm
import collections
from datetime import date
query3_dbm = dbm.open('query3', 'c')
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
        for i in unpack(block):
            key = str(date(i[0].year, i[0].month, i[0].day)).replace('-', '')
            if key in query3_dbm:
                val = query3_dbm[key]
                new_val = str(val.decode('utf-8')) + "," + str(block_number) + str('-') + str(i[1])
                query3_dbm[key] = new_val
            else:
                query3_dbm[key] = str(block_number) + str('-') + str(i[1])


# Reading each block and returning the extracted records
def unpack(block):
    offset = 1
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
        list_of_records.append((Result(*temp_list),offset))
        offset += 1
        block = block[record_size:]
    return list_of_records


binary_file_extract()
bin_file.close()