import os
import sys
from sikuli import *

sys_path = sys.path[0]
sys_path_split = sys_path.split("\\")
del sys_path_split[-1]
print(sys_path_split)
delimiter = "\\"
picture_path = delimiter.join(sys_path_split) + "\\screenshot\\"
print(picture_path)

def search_path(picture_name):
    check_path = picture_path + picture_name + "\\"
    print(check_path)
    search_list = os.listdir(check_path)
    print(search_list)
    for i in search_list:
        print(i)
        final_path = check_path + i
        try: 
            exists(final_path):
            print("Found picture")
            return final_path
            break
        except:
            print("Not Found picture")
            return 0