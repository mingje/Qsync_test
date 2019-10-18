import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


gmail_user = 'stevenhsu@qnap.com'
gmail_password = 'Qwer!23456' # your gmail password
gmail_to = ['mingje1104@gmail.com']
gmail_cc = ['stevenhsu@qnap.com']
COMMASPACE = ', '
ao = "machine 1"
#msg = MIMEText('content')
msg = MIMEMultipart()
msg['Subject'] = 'ERROR'
msg['From'] = "AT管理員"
msg['To'] = COMMASPACE.join(gmail_to)
msg['cc'] = COMMASPACE.join(gmail_cc)


part = MIMEText(ao + " error")
msg.attach(part)
"""
#---这是附件部分---
#xlsx类型附件

current_path = os.getcwd()
report_title = "testcase.csv"
testpath = current_path + "/" + report_title
print(testpath)

attachments = [testpath]
for file in attachments:
    part = MIMEApplication(open(file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
    msg.attach(part)
"""

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user,gmail_to,msg.as_string())
server.quit()

print('Email sent!')
