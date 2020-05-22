#from ADBMS_Project3_Query4_Index_File import *
from datetime import date
import dbm
from ADBMS_Project3_Query4_Read_Disk import *
query4 = dbm.open('query4', 'r')


# Calculates age
def cal(dat):
    today = date.today()
    age = today.year - dat.year - ((today.month, today.day) < (dat.month, dat.day))
    return age


i = query4.firstkey()
while i!= None:
    if cal(date(int(i[0:4]), int(i[4:6]), int(i[6:8]))) < 21:
        b = query4[i].decode('utf-8')
        k = b.split(',')
        for each in k:
            block, record = each.split('-')
            binary_file_extract(int(block), int(record))
    i = query4.nextkey(i)

query4.close()