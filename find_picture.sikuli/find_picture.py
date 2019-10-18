import os
import sys
from sikuli import *
a = sys.path[0]
b = a.split("\\")
del b[-1]
print(b)
delimiter = "\\"
c = delimiter.join(b) + "\\screenshot\\"
print(c)

def findup(picture_name):
    check_folder = c + picture_name + "\\"
    print(check_folder)
    detail_list = os.listdir(check_folder)
    print(detail_list)
    for i in detail_list:
        print(i)
        finish_p = check_folder + i
        print(finish_p)
        try:
            if exists(finish_p):
                print('okok')
                flag = finish_p
                break
        except:
            print('nono')
            flag = finish_p
       
    return flag
