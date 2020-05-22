#from ADBMS_Project3_Query3_Index_FIle import *
from datetime import date
import dbm
from ADBMS_Project3_Query3_Read_Disk import *
query3 = dbm.open('query3', 'r')


# Calculates age
def cal(dat):
    today = date.today()
    age = today.year - dat.year -((today.month, today.day) <(dat.month, dat.day))
    return age


i = query3.firstkey()
while i!= None:
    if cal(date(int(i[0:4]), int(i[4:6]), int(i[6:8]))) < 21:
        b = query3[i].decode('utf-8')
        k = b.split(',')
        for each in k:
            block, record = each.split('-')
            binary_file_extract(int(block), int(record))
    i = query3.nextkey(i)
