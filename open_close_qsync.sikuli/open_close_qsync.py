from sikuli import *
from library_qsync import *

current_user = os.popen("whoami").read()
print(current_user)
r = str(current_user)
print(r)
rr = r.split("\\")
pc_name = rr[0]

x = 1                         
for i in range(2):
    print("Execute " + str(x) + " Times")
    open_qsync()
    wait(5)
    if exists(Pattern(search_path("syncdone_icon")).similar(0.70)):
        print("Sync success")
    elif exists(Pattern(search_path("syncing_icon")).similar(0.70)):
        print("Syncing...")
    else:
        print("Sync failed")
        send_mail(pc_name)
        break
    wait(2)
    close_qsync()
    wait(2)
    x = x + 1

"""
keyDown(Key.ALT)
keyDown(Key.F4)
"""