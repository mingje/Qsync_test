from sikuli import *
from library_qsync import *
"""
nas_lanip = sys.argv[1]
nas_ac = sys.argv[2]
nas_pwd = sys.argv[3]
"""
nas_lanip = "10.20.241.196"
nas_ac = "admin"
nas_pwd = "dqvts453bt3" 
target = nas_detail(lanip = nas_lanip, ac = nas_ac, pwd = nas_pwd)
print(target)

open_qsync()
wait(2)
click(Pattern(search_path("host_field")).similar(0.70))
wait(1)
type(target["lanip"])
wait(1)
type(Key.TAB)
type(target["ac"])
wait(1)
type(Key.TAB)
type(target["pwd"])
wait(1)
type(Key.ENTER)

waitVanish((Pattern(search_path("pairing_string")).similar(0.70)),120)
if exists(Pattern(search_path("pairing_string")).similar(0.70)):
    print("over 2 mins..")
elif exists(Pattern(search_path("loginfail_string")).similar(0.70)):
    print("login failed")
elif exists(Pattern(search_path("qsyncpath_string")).similar(0.70)):
    print("login success")
else:
    print("unknown status")
wait(5)
click(Pattern(search_path("addfolder_icon")).similar(0.70))
wait(2)
rregion = Region(447,151,387,368)
if rregion.exists(Pattern(search_path("browsefolder_string")).similar(0.70)):
    print("open")
else:
    print("open Failed")
type("M")
wait(1)
type("@Qsync_test")
wait(1)
type(Key.ENTER)
wait(1)
type(Key.ENTER)
wait(1)
click(Pattern(search_path("finish_button")).similar(0.70))
wait(2)
close_qsync()
