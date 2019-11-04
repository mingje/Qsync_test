from sikuli import *
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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
        print(final_path) 
        if exists(final_path):
            print("Found picture")
            flag = final_path
            break
        else:
            print("Not Found picture")
            flag = final_path
    return flag

def nas_detail(**kwargs):
    nas = {}   
    nas["lanip"] = kwargs.get("lanip")   
    nas["ac"] = kwargs.get("ac")
    nas["pwd"] = kwargs.get("pwd")
    return nas

def send_mail(test_pc):
    gmail_user = 'stevenhsu@qnap.com'
    gmail_password = 'Qwer!23456' # your gmail password
    gmail_to = ['mingje1104@gmail.com', 'danielhuang@qnap.com', 'rexhchsu@qnap.com']
    gmail_cc = ['stevenhsu@qnap.com']
    COMMASPACE = ', '
    #msg = MIMEText('content')
    msg = MIMEMultipart()
    msg['Subject'] = 'ERROR'
    msg['From'] = "AT manager"
    msg['To'] = COMMASPACE.join(gmail_to)
    msg['cc'] = COMMASPACE.join(gmail_cc)
    part = MIMEText(test_pc + " error")
    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,gmail_to,msg.as_string())
    server.quit()
    print('Email sent!')

def open_qsync():
    flag = 0
    for i in range(3):
        os_bit = os.popen("echo %PROCESSOR_ARCHITECTURE%").read()
        if "64" in os_bit: 
            qsync = "C:\Program Files (x86)\QNAP\Qsync\Qsync.exe"
        else:
            qsync = "C:\Program Files\QNAP\Qsync\Qsync.exe"
        openApp(qsync)
        wait(5)
        if exists(Pattern(search_path("delete_button")).similar(0.70)):
            click(Pattern(search_path("delete_button")).similar(0.70))
        else:
            print("No warning")
        if "64" in os_bit:
            os.system('"C:\\Program Files (x86)\\QNAP\\Qsync\\Qsync.exe"')
        else:
            os.system('"C:\\Program Files\\QNAP\\Qsync\\Qsync.exe"')
        wait(5)
        if exists(Pattern(search_path("minwindow_icon")).similar(0.80)):
            click(Pattern(search_path("minwindow_icon")).similar(0.80))
        elif exists(Pattern(search_path("maxwindow_icon")).similar(0.70)):
            print("Max Qsync window")
        else:
            print("Max Qsync window failed")
        wait(5)
        if exists(Pattern(search_path("qsync_logo")).similar(0.70)):
            print("Open Qsync success")
            flag = 1
            break
        else:
            flag = 0
    assert flag == 1, "Open Qsync failed"

def close_qsync():
    os.system("taskkill /f /im Qsync.exe")
    if exists(Pattern(search_path("qsync_logo")).similar(0.70)):
        flag = 0
    else:
        print("Close Qsync success")
        flag = 1
    assert flag == 1, "Close Qsync failed"

def remove_nas_profile():
    click(Pattern(search_path("more_button")).similar(0.70))
    wait(2)
    click(Pattern(search_path("removeNAS_option")).similar(0.70))
    wait(2)
    click(Pattern(search_path("option_button")).similar(0.70))
    wait(1)
    type(Key.DOWN)
    wait(1)
    type(Key.ENTER)
    wait(1)
    waitVanish((Pattern(search_path("pleasewait_string")).similar(0.70)),240)
    if exists(Pattern(search_path("host_field")).similar(0.70)):
        print("Remove NAS success")
        flag = 1
    else:
        flag = 0
    assert flag == 1, "Remove NAS failed"
