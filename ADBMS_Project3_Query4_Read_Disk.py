import struct
import collections
from datetime import date
size_of_blocks = 40960
buffer_factor = 10
block_size = int(size_of_blocks/buffer_factor)
fmt = '20s20s70s40s80s25s3i12s25s50s50s'
record_size = struct.calcsize(fmt)


# Reading the file as block by block
def binary_file_extract(block_no, offset):
    bin_file = open("new_file.bin", 'rb')
    d = bin_file.read(block_size * block_no)
    g = d[block_size * (block_no - 1): block_size * block_no]
    unpacked_records = unpack(g)
    print(unpacked_records[offset - 1])


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


def main():
    binary_file_extract(block, offset)


if __name__ == '__main__':
    main()
